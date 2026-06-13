"""
M12 Lesson 5 – Building a Multi-Tool AI App – Part 1
"""

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
# ////////////
import streamlit as st

def main():
    st.title("🛠️ Multi-Tool AI Assistant")
    st.sidebar.title("Tools")
    
    tool = st.sidebar.selectbox("Choose Tool", 
        ["Teaching Assistant", "Math Solver", "Image Generator", "Translator"])
    
    st.write(f"**Selected Tool:** {tool}")
    # Basic structure - Part 1 focuses on navigation and UI
    
    if tool == "Teaching Assistant":
        st.write("Chat interface here...")
    elif tool == "Math Solver":
        st.write("Math problems...")
    
    st.subheader("Activity 1: Add More Tools")
    st.write("Implement Translator using Gemini")
    
    st.subheader("Activity 2: Sidebar Customization")
    st.write("Add icons and descriptions")
    
    st.subheader("Activity 3: Theme Toggle")
    st.write("Dark/Light mode")

if __name__ == "__main__":
    main()