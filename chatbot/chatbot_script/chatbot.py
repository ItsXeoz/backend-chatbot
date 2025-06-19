import json
import numpy as np
from sentence_transformers import SentenceTransformer

# Load data asli
with open("Data/cleaned_all_datasets_shorten.json", "r", encoding="utf-8") as f:
    data = json.load(f)

questions = [item["question"] for item in data]
answers = [item["answer"] for item in data]

# Gunakan model SentenceTransformer
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
question_embeddings = model.encode(questions, convert_to_tensor=False)

# Simpan ke file JSON
chatbot_data = []
for q, a, emb in zip(questions, answers, question_embeddings):
    chatbot_data.append({
        "question": q,
        "answer": a,
        "embedding": emb.tolist()
    })

# Simpan file
with open("chatbot_data.json", "w", encoding="utf-8") as f:
    json.dump(chatbot_data, f, ensure_ascii=False, indent=2)

print("✅ chatbot_data.json berhasil dibuat.")
