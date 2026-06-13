"""
M12 Lesson 1 – Building an AI Teaching Assistant with Streamlit and Gemini API
Advanced AI Capstone Project
"""

import streamlit as st
# Note: For Gemini API, use google-generativeai
# pip install streamlit google-generativeai

def main():
    st.title("🤖 AI Teaching Assistant")
    st.write("Your personal tutor powered by Gemini")
    
    # API Key input (in production use secrets)
    api_key = st.text_input("Enter Gemini API Key", type="password")
    
    if api_key:
        # Here you would initialize Gemini
        st.success("Connected to Gemini!")
        
        query = st.text_area("Ask me anything (Math, Science, History, etc.)")
        if st.button("Get Answer"):
            if query:
                # Simulate Gemini response
                response = f"Gemini would answer: This is a detailed explanation for '{query}'"
                st.write(response)
            else:
                st.warning("Please enter a question.")

    # Activity 1
    st.subheader("Activity 1: Customize the Tutor")
    st.write("Modify the code to add subject selection (Math, Physics, etc.)")
    
    # Activity 2
    st.subheader("Activity 2: Add Voice Input")
    st.write("Integrate speech_recognition library for voice queries")
    
    # Activity 3
    st.subheader("Activity 3: Save Conversation")
    st.write("Add functionality to save Q&A to a text file")

if __name__ == "__main__":
    main()

print("Run with: streamlit run M12_Lesson1_AI_Teaching_Assistant_Streamlit_Gemini.py")


# ///////////////////////

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