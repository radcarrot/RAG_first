# RAG Medical Assistant

A Retrieval-Augmented Generation (RAG) system that combines a local medical knowledge base with Perplexity AI to provide grounded answers to medical queries.

## 📁 Project Structure

```
RAG_first/
├── app.py                  # Main Flask application entry point
├── config.py               # Configuration and local knowledge base data
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (API keys)
├── utils/
│   ├── retriever.py        # Keyword-based retrieval logic
│   └── perplexity_client.py
├── routes/                 # Route modules (extensions)
│   ├── health_routes.py
│   └── rag_routes.py
└── tests/                  # Unit tests
    ├── test_rag.py
    └── test_perplexity.py
```

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/radcarrot/RAG_first.git
cd RAG_first
```

### 2. Set Up Environment
Create a virtual environment to manage dependencies:

**Windows:**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configuration
Create a `.env` file in the root directory and add your Perplexity API key:
```ini
PERPLEXITY_API_KEY=your_actual_api_key_here
```

## 🏃 Usage

### Start the Server
```bash
python app.py
```
The server will start at `http://127.0.0.1:5000`.

### Make a Query
You can interact with the API using `curl` or Postman.

**Health Check:**
```bash
curl http://127.0.0.1:5000/health
```

**Ask a Question:**
```bash
curl -X POST http://127.0.0.1:5000/api/rag-query \
  -H "Content-Type: application/json" \
  -d "{\"query\": \"Is paracetamol safe for fever?\"}"
```

**Example Response:**
```json
{
  "query": "Is paracetamol safe for fever?",
  "answer": "Paracetamol is generally safe...",
  "retrieved_context": [
    "Paracetamol (Acetaminophen) is an analgesic..."
  ]
}
```

## 🧪 Testing
Run the test suite to verify everything is working:
```bash
pytest tests/
```