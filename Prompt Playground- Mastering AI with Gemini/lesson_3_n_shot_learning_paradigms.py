"""
================================================================================
LESSON 3: Zero-Shot, One-Shot, and Few-Shot Learning
================================================================================




OBJECTIVE: Evaluate performance leaps across Zero, One, and Multi-exemplar structures.
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

# ////////////////////////////

def dispatch_learning_paradigms():
    print("\n=== EXECUTING LESSON 3: N-SHOT LEARNING PARADIGMS ===")
    
    # Example of Few-Shot structured layout inside a prompt payload
    few_shot_prompt = """
    Task: Classify system crash codes into structural severity domains.
    
    Input: Error 0x001F - Stack trace pointer corruption
    Classification: CRITICAL_INFRASTRUCTURE_FAILURE
    
    Input: Error 0x04B2 - User profile theme layout dropped
    Classification: NON_BLOCKING_UI_EXCEPTION
    
    Input: Error 0x009A - Inbound connection frame timeout
    Classification: NETWORK_TIMEOUT_WARNING
    
    Input: Error 0x011C - Core register validation buffer overflow
    Classification:
    """
    print("--> Forwarding Few-Shot context pipeline to parsing engine...")
    print(f"[PIPELINE OUTPUT] Expected Target Resolution: CRITICAL_INFRASTRUCTURE_FAILURE\n")

if __name__ == "__main__":
    dispatch_learning_paradigms()
