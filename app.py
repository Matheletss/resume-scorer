import streamlit as st
from resume_parser import parse_resume
from scorer import score_resume
import os

def load_role_description(role):
    with open(f"roles/{role}.txt", "r") as f:
        return f.read()

st.set_page_config(page_title="Resume Scorer", layout="centered")
st.title("📄 AI Resume Scorer")
st.write("Upload a PDF resume and select a job role to see your matching score.")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

available_roles = [f.split(".")[0] for f in os.listdir("roles") if f.endswith(".txt")]
job_role = st.selectbox("Select Job Role", available_roles)

if uploaded_file and job_role:
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    parsed_data = parse_resume("temp_resume.pdf")
    resume_text = " ".join([str(parsed_data.get(field, "")) for field in ["skills", "experience", "company_names", "designation", "degree", "college_name"]])

    role_desc = load_role_description(job_role)
    score = score_resume(resume_text, role_desc)

    st.markdown(f"### 🎯 Match Score: `{score:.2f} / 100`")
    st.progress(score / 100)

    with st.expander("📋 Extracted Resume Data"):
        st.json(parsed_data)
