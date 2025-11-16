# Configuration for RAG Service

MEDICAL_KNOWLEDGE_BASE = [
    {
        "id": "drug_1",
        "text": "Paracetamol (Acetaminophen) is an analgesic and antipyretic used to treat fever and mild to moderate pain. Typical adult dose is 500-1000mg every 4-6 hours, maximum 4g per day. Generally safe but can cause liver damage with overdose. Avoid alcohol while taking paracetamol. Safe to take with most medications.",
        "category": "drug_info"
    },
    {
        "id": "drug_2",
        "text": "Ibuprofen is a nonsteroidal anti-inflammatory drug (NSAID) used for pain relief, fever reduction, and inflammation. Adult dose: 200-400mg every 4-6 hours, maximum 1200mg per day. Should be taken with food to reduce stomach upset. Can interact with blood pressure medications and increase bleeding risk.",
        "category": "drug_info"
    },
    {
        "id": "drug_3",
        "text": "Aspirin is an NSAID used for pain relief and blood thinning. Typical dose: 75-300mg daily for heart protection, 300-900mg every 4-6 hours for pain. Should not be given to children under 16. Can cause stomach irritation and bleeding.",
        "category": "drug_info"
    },
    {
        "id": "drug_4",
        "text": "Cetirizine is an antihistamine used for allergies, hay fever, and hives. Adult dose: 10mg once daily. Non-drowsy formula available. Safe for long-term use. Few drug interactions.",
        "category": "drug_info"
    },
    {
        "id": "drug_5",
        "text": "Amoxicillin is an antibiotic used to treat bacterial infections. Typical dose: 250-500mg every 8 hours or 500-875mg every 12 hours. Complete full course even if feeling better. Can cause allergic reactions in penicillin-sensitive individuals.",
        "category": "drug_info"
    },
    {
        "id": "interaction_1",
        "text": "Paracetamol and Ibuprofen can be taken together safely as they work differently. However, always maintain recommended dosages for each medication.",
        "category": "interaction"
    },
    {
        "id": "interaction_2",
        "text": "Aspirin and Ibuprofen should NOT be taken together as both are NSAIDs and increase risk of gastrointestinal bleeding and stomach ulcers.",
        "category": "interaction"
    },
    {
        "id": "interaction_3",
        "text": "Ibuprofen can reduce effectiveness of blood pressure medications like ACE inhibitors and beta-blockers. Consult doctor if taking both.",
        "category": "interaction"
    },
    {
        "id": "interaction_4",
        "text": "Alcohol and Paracetamol together increase risk of liver damage. Avoid alcohol while taking paracetamol, especially with regular use.",
        "category": "interaction"
    },
    {
        "id": "faq_1",
        "text": "For fever in adults, paracetamol 500-1000mg or ibuprofen 200-400mg every 4-6 hours is recommended. Stay hydrated and rest. See doctor if fever persists beyond 3 days or exceeds 103°F (39.4°C).",
        "category": "faq"
    },
]

# Perplexity API Configuration
PERPLEXITY_MODEL = "sonar"
PERPLEXITY_MAX_TOKENS = 1024
PERPLEXITY_TEMPERATURE = 0.3

# Flask Configuration
FLASK_ENV = "development"
DEBUG = True
