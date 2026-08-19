import os

import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Document Q&A", page_icon="📄")
st.title("📄 Document Q&A")
st.caption("Ask questions about a text document using an LLM API.")

api_key = os.getenv("OPENAI_API_KEY")

uploaded_file = st.file_uploader("Upload a .txt document", type=["txt"])
question = st.text_input("Ask a question about the document")


def get_answer(context: str, question: str) -> str:
    if not api_key:
        return "Add OPENAI_API_KEY to your .env file to enable answers."

    response = requests.post(
        "https://api.openai.com/v1/responses",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": "gpt-4o-mini",
            "input": [
                {
                    "role": "system",
                    "content": (
                        "Answer only from the supplied document context. "
                        "If the answer is not present, say you cannot find it in the document."
                    ),
                },
                {
                    "role": "user",
                    "content": f"Document context:\n{context}\n\nQuestion: {question}",
                },
            ],
        },
        timeout=60,
    )
    response.raise_for_status()
    data = response.json()
    return data.get("output_text", "No answer returned.")


if uploaded_file and question:
    text = uploaded_file.read().decode("utf-8", errors="ignore")
    # This first version intentionally uses a simple bounded context.
    context = text[:12000]

    with st.spinner("Generating answer..."):
        try:
            answer = get_answer(context, question)
            st.subheader("Answer")
            st.write(answer)
        except requests.RequestException as exc:
            st.error(f"API request failed: {exc}")
else:
    st.info("Upload a text file and enter a question to begin.")
