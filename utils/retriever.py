# utils/retriever.py
from config import MEDICAL_KNOWLEDGE_BASE

def simple_keyword_search(query, top_n=3):
    """
    Simple keyword-based retrieval from local knowledge base.
    Searches through medical facts and returns top matches.
    """
    results = []
    query_words = query.lower().split()
    
    for entry in MEDICAL_KNOWLEDGE_BASE:
        text = entry['text'].lower()
        # Count how many query words appear in this entry
        match_count = sum(1 for word in query_words if word in text)
        if match_count > 0:
            results.append({
                'text': entry['text'],
                'category': entry['category'],
                'matches': match_count
            })
    
    # Sort by number of matches (descending) and return top_n
    results.sort(key=lambda x: x['matches'], reverse=True)
    return [item['text'] for item in results[:top_n]]
