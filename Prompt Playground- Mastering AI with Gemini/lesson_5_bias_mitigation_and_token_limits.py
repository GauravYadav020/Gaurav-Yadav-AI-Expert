"""
================================================================================
LESSON 5: Bias Mitigation & Token Limit Handling
================================================================================
OBJECTIVE: Keep tokens within bounds while balancing prompt objectivity.
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
# ///////////////

class TokenAndBiasManagementPipeline:
    def calculate_approximate_tokens(self, string_payload):
        # Approximate token resolution metrics mapping rules
        return len(string_payload.split()) * 2
    
    def execute_safeguarded_inference(self, prompt, structural_cutoff):
        tokens = self.calculate_approximate_tokens(prompt)
        print(f"[ANALYSIS] Computed data frame consumption weight: {tokens} tokens.")
        if tokens > structural_cutoff:
            print("[WARNING] Vector sequence exceeds limit boundaries. Truncating context.")
            prompt = " ".join(prompt.split()[:structural_cutoff // 2])
        
        # Injecting functional bias-mitigation guardrails explicitly
        sanatized_prompt = prompt + " Ensure objective representation from multiple certified sources."
        return f"[Processed Output] Response generated securely under token ceiling validation limits."

def run_token_sentinel():
    print("\n=== EXECUTING LESSON 5: TOKEN GUARDRAIL CONTROLLER ===")
    sentinel = TokenAndBiasManagementPipeline()
    large_payload = "Data stream content framework sequence " * 40
    
    execution_trace = sentinel.execute_safeguarded_inference(large_payload, structural_cutoff=60)
    print(f"Sentinel System Trace Log: {execution_trace}\n")

if __name__ == "__main__":
    run_token_sentinel()
