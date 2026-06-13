"""
================================================================================
LESSON 2: Advanced Prompt Engineering: Temperature & Instruction-Based Prompts
================================================================================
OBJECTIVE: Understand deterministic vs. creative responses via hyperparameter routing.
"""

import json

class HyperparameterPromptEngine:
    def call_gemini_with_config(self, prompt, generation_config):
        temp = generation_config.get("temperature", 0.7)
        print(f"[METRIC] Processing inference loop under Temperature parameter: {temp}")
        if temp == 0.0:
            return "Deterministic Result: Code logic validation complete. No variance allowed."
        else:
            return "Creative Result: Spontaneous metaphor mapping deployed across contextual boundaries."

def run_hyperparameter_evaluation():
    print("\n=== EXECUTING LESSON 2: PARAMETER DRIVEN ROUTING ===")
    engine = HyperparameterPromptEngine()
    system_prompt = "Task: Generate code refactoring alternative structural maps."
    
    # Scenario A: Low Temperature for exact, non-creative structural outputs
    config_low = {"temperature": 0.0, "max_output_tokens": 512}
    response_a = engine.call_gemini_with_config(system_prompt, config_low)
    print(f"[Low Temp Config] {response_a}")
    
    # Scenario B: High Temperature for multi-angle theoretical ideation
    config_high = {"temperature": 0.9, "max_output_tokens": 512}
    response_b = engine.call_gemini_with_config(system_prompt, config_high)
    print(f"[High Temp Config] {response_b}\n")

if __name__ == "__main__":
    run_hyperparameter_evaluation()


# //////////////////////

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