"""
M12 Lesson 2 – AI Teaching Assistant with Conversation History
"""

import streamlit as st
from collections import deque

def main():
    st.title("📚 AI Tutor with Memory")
    
    # Initialize session state for history
    if 'history' not in st.session_state:
        st.session_state.history = deque(maxlen=10)
    
    query = st.text_input("Ask your tutor:")
    if st.button("Send"):
        if query:
            # Simulate response
            response = f"Answer to: {query} (with context from previous chats)"
            st.session_state.history.append({"q": query, "a": response})
            st.write(response)
    
    st.subheader("Conversation History")
    for item in st.session_state.history:
        st.write(f"**Q:** {item['q']}")
        st.write(f"**A:** {item['a']}")
    
    # 3 Activities
    st.subheader("Activity 1: Persistent Storage")
    st.write("Save history to JSON file")
    
    st.subheader("Activity 2: Context-aware Responses")
    st.write("Pass full history to Gemini API")
    
    st.subheader("Activity 3: Clear History Button")
    st.write("Implement reset functionality")

if __name__ == "__main__":
    main()

    # /////////////

    # groq.py  (pip install openai)
import config
from openai import OpenAI

GROQ_URL = "https://api.groq.com/openai/v1"
MODELS = getattr(config, "GROQ_MODELS", ["llama-3.1-8b-instant", "mixtral-8x7b-32768"])

def generate_response(prompt: str, temperature: float = 0.3, max_tokens: int = 512) -> str:
    key = getattr(config, "GROQ_API_KEY", None)
    if not key:
        return "Error: GROQ_API_KEY missing in config.py"
    c = OpenAI(api_key=key, base_url=GROQ_URL)

    last_err = None
    for m in MODELS:
        try:
            r = c.chat.completions.create(
                model=m,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=max_tokens,
            )
            return r.choices[0].message.content
        except Exception as e:
            last_err = e

    return (
        "Groq model failed.\n"
        f"Tried models: {MODELS}\n"
        "Fix:\n"
        "1) Switch to hf by importing hf.py in main.py OR\n"
        "2) Replace Groq model in groq.py (GROQ_MODELS).\n"
        f"Details: {type(last_err).__name__}: {last_err}"
    )