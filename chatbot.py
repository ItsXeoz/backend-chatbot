import json
import numpy as np
from utils import embed_sentences
from sentence_transformers import SentenceTransformer, util

# Load Q-table dan data
q_table = np.load("q_table.npy")
with open("Data/cleaned_all_datasets_shorten.json", "r", encoding="utf-8") as f:
    data = json.load(f)

questions = [item["question"] for item in data]
answers = [item["answer"] for item in data]

question_embeddings = embed_sentences(questions)
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

def respond(user_input):
    input_embedding = model.encode(user_input, convert_to_tensor=True)
    similarities = util.cos_sim(input_embedding, question_embeddings)[0]
    top_indices = similarities.argsort(descending=True)

    for idx in top_indices:
        answer = answers[idx]
        if len(answer.split()) <= 100:
            return answer
    return "I'm still learning to answer that properly. Please ask something else."
