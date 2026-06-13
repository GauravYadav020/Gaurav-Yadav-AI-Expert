"""
================================================================================
MODULE: Prompt Playground - Mastering AI with Gemini
LESSON 1: Prompt Engineering: Clarity, Specificity, and Contextual Information
================================================================================
OBJECTIVE: Master structural clarity, strict boundaries, and explicit dynamic injection.
"""

import os
# Simulated Gemini API Wrapper for standalone local testing
class MockGeminiClient:
    def generate_content(self, prompt):
        # Simulating analytical prompt extraction based on layout markers
        if "CONTEXT:" in prompt and "STRICT_CONSTRAINT:" in prompt:
            return "[Gemini Output] Structurally sound response aligning with injected framework rules."
        return "[Gemini Output] Baseline completion without rigorous contextual structuring."

def run_clarity_and_context_sandbox():
    print("\n=== EXECUTING LESSON 1: CLARITY & CONTEXT SANDBOX ===")
    client = MockGeminiClient()
    
    # Structuring highly descriptive, contextual frameworks instead of vague sentences
    dynamic_context = "Target audience: Data science freshmen. Topic: Multi-variate calculus foundations."
    structured_prompt = f"""
    CONTEXT:
    {dynamic_context}
    
    TASK:
    Generate a brief, 3-sentence summary introducing derivatives.
    
    STRICT_CONSTRAINT:
    Do not use complex jargon. Avoid referencing advanced theorem labels.
    """
    
    print("--> Forwarding Structured Injections to LLM Layout Engine...")
    response = client.generate_content(structured_prompt)
    print(f"Engine Telemetry Execution Result:\n{response}\n")

if __name__ == "__main__":
    run_clarity_and_context_sandbox()


# /////////////////

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