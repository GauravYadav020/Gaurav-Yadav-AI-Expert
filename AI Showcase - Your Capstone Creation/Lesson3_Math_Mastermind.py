"""
M12 Lesson 3 – Math Mastermind: Interactive AI-Powered Math Problem Solver
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

# ////////////////
import streamlit as st
import random

def generate_math_problem(difficulty="medium"):
    if difficulty == "easy":
        a, b = random.randint(1,10), random.randint(1,10)
        return f"{a} + {b} = ?", a+b
    elif difficulty == "medium":
        a, b = random.randint(10,50), random.randint(10,50)
        return f"{a} * {b} = ?", a*b
    else:
        return "Solve 2x + 3 = 11", 4

def main():
    st.title("🧠 Math Mastermind")
    st.write("AI-Powered Math Tutor")
    
    difficulty = st.selectbox("Difficulty", ["easy", "medium", "hard"])
    problem, answer = generate_math_problem(difficulty)
    
    st.write("**Problem:**", problem)
    user_answer = st.number_input("Your Answer", value=0)
    
    if st.button("Submit"):
        if user_answer == answer:
            st.success("Correct! 🎉")
        else:
            st.error(f"Wrong. Correct answer is {answer}")
    
    # Activities
    st.subheader("Activity 1: Add Algebra Solver")
    st.write("Use sympy to solve equations")
    
    st.subheader("Activity 2: Step-by-Step Solution")
    st.write("Show explanation using Gemini")
    
    st.subheader("Activity 3: Progress Tracker")
    st.write("Track accuracy over sessions")

if __name__ == "__main__":
    main()