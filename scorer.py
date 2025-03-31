from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def score_resume(resume_text, role_description):
    resume_emb = model.encode(resume_text, convert_to_tensor=True)
    role_emb = model.encode(role_description, convert_to_tensor=True)
    similarity = util.cos_sim(resume_emb, role_emb)
    return round(float(similarity[0][0]) * 100, 2)
