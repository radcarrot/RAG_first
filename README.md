🏥 RAG Medical Assistant

A Retrieval-Augmented Generation (RAG) powered medical knowledge assistant that combines local medical facts with AI to provide accurate, grounded health information.








📋 Table of Contents

About

Features

How It Works

Tech Stack

Installation

Usage

Project Structure

Configuration

API Endpoints

Testing

Roadmap

Contributing

License

Author

Acknowledgments

🎯 About

The RAG Medical Assistant is an intelligent healthcare information system that retrieves relevant medical facts from a local knowledge base and augments them with Perplexity AI's language model to generate accurate, contextual answers to medical queries.

This system is designed for:

🏥 Medical information lookup

💊 Drug interaction checking

🔍 Symptom analysis

📚 Educational purposes

⚠️ Disclaimer: This is an educational project and should not replace professional medical advice.

✨ Features

🔎 Smart Retrieval from a local medical knowledge base

🤖 AI-Powered Generation via Perplexity Sonar

💉 Medical Knowledge Base with drug info & interactions

🔒 Secure API Key Handling

📊 JSON Responses with retrieved context

⚡ Fast REST API using Flask

🧪 Unit & Integration Tests Included

🧠 How It Works
User Query → Retriever (search KB) → Augment Prompt → LLM (Perplexity) → Answer


System retrieves relevant information from the knowledge base

Adds retrieved facts to the model prompt

Perplexity AI generates a grounded answer

Response includes both the final answer + context used

🛠️ Tech Stack
Technology	Purpose
Python 3.8+	Backend logic
Flask	REST API
Perplexity AI API	LLM generation
requests	API calls
python-dotenv	Env variable management
📦 Installation
Prerequisites

Python 3.8+

Git

Perplexity API key

1. Clone the repository
git clone https://github.com/radcarrot/RAG_first.git
cd RAG_first

2. Create Virtual Environment
python -m venv venv


Activate it:

Windows

.\venv\Scripts\activate


macOS/Linux

source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Create .env file
PERPLEXITY_API_KEY=your_api_key_here

5. Run the app
python app.py


API runs at:

http://127.0.0.1:5000

🚀 Usage
Health Check
curl http://127.0.0.1:5000/health

Query the RAG system
curl -X POST http://127.0.0.1:5000/api/rag-query \
  -H "Content-Type: application/json" \
  -d '{"query": "Is paracetamol safe for fever?"}'

Example Response
{
  "query": "Is paracetamol safe for fever?",
  "answer": "Paracetamol is generally safe and commonly used...",
  "retrieved_context": [
    "Paracetamol is an analgesic and antipyretic...",
    "Adult dosage is 500-1000mg..."
  ]
}

📁 Project Structure
RAG_first/
├── app.py
├── config.py
├── requirements.txt
├── .env
├── README.md
├── routes/
│   ├── health_routes.py
│   └── rag_routes.py
├── utils/
│   ├── retriever.py
│   ├── perplexity_client.py
│   └── response_formatter.py
├── tests/
│   ├── test_rag.py
│   └── test_perplexity.py
└── logs/
    └── app.log

⚙️ Configuration
Knowledge Base (inside config.py)
MEDICAL_KNOWLEDGE_BASE = [
    {
        "id": "drug_1",
        "text": "Your medical fact here...",
        "category": "drug_info"
    }
]

Model Settings
PERPLEXITY_MODEL = "sonar"
PERPLEXITY_MAX_TOKENS = 1024
PERPLEXITY_TEMPERATURE = 0.3

🔌 API Endpoints
GET /health

Returns:

{
  "status": "healthy",
  "service": "RAG Medical Knowledge Service",
  "version": "1.0.0"
}

POST /api/rag-query

Request:

{
  "query": "Your question here"
}


Response:

{
  "query": "User question",
  "answer": "AI-generated answer",
  "retrieved_context": ["Fact 1", "Fact 2"]
}

🧪 Testing

Run all tests:

pytest tests/

🗺️ Roadmap

 Add encyclopedia-based medical dataset

 Add embeddings + semantic search

 Frontend UI (React/Streamlit)

 User authentication

 Cloud deployment

 Caching layer

 Multi-turn conversation memory

🤝 Contributing

Fork

Create branch

Commit changes

Push

Submit PR

📄 License

MIT License

👤 Author

radcarrot
GitHub: https://github.com/radcarrot/RAG_first

🙏 Acknowledgments

Perplexity AI

Flask community

Medical contributors

Made with ❤️ for the healthcare community