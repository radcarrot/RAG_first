import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import requests
from utils.retriever import simple_keyword_search

# Load environment variables from .env file
load_dotenv()

# Initialize Flask
app = Flask(__name__)
CORS(app)

# Perplexity API Key from .env
PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")
PERPLEXITY_MODEL = "sonar"

# Main route (health check)
@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'healthy',
        'service': 'RAG Medical Knowledge Service',
        'version': '1.0.0'
    }), 200

# RAG query route
@app.route('/api/rag-query', methods=['POST'])
def rag_query():
    data = request.get_json()
    query = data.get('query')
    if not query:
        return jsonify({'error': 'No query provided'}), 400

    # RETRIEVAL STEP (RAG!)
    retrieved_facts = simple_keyword_search(query, top_n=3)
    context = "\n".join(retrieved_facts) if retrieved_facts else "No relevant facts found in local knowledge base."

    # Augmented system prompt with retrieved facts
    system_prompt = f"""You are a medical information assistant. 
    
Here are relevant facts from our local medical knowledge base:
---
{context}
---

Use these facts to answer the user's question. If the knowledge base doesn't have info, you can use your general knowledge but mention that it's not in our local facts.
Provide accurate, evidence-based information.
Always recommend consulting a doctor for serious concerns.
Be cautious with medical advice and include disclaimers."""

    # Call Perplexity API
    api_url = "https://api.perplexity.ai/chat/completions"
    response = requests.post(
        api_url,
        headers={
            "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": PERPLEXITY_MODEL,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": query}
            ],
            "max_tokens": 1024,
            "temperature": 0.3
        }
    )

    if response.status_code == 200:
        result = response.json()
        answer = result['choices'][0]['message']['content']
        return jsonify({
            'query': query,
            'answer': answer,
            'retrieved_context': retrieved_facts  # Optional: show what was retrieved
        }), 200
    else:
        print("Perplexity API returned:", response.text)
        return jsonify({'error': 'Perplexity API error'}), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
