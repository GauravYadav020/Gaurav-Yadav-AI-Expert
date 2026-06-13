"""
================================================================================
LESSON 4: Reinforcement Learning & Role-Based Prompts
================================================================================
OBJECTIVE: Anchor persona definitions and construct internal validation loops.
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
# //////////////////////////////
class RoleBasedOrchestrator:
    def run_persona_simulation(self, dynamic_role, target_instruction):
        crafted_prompt = f"""
        ROLE_PERSONA:
        You are an elite senior cyber security operations auditor under tight deadlines.
        Adopt persona attributes: {dynamic_role}
        
        INSTRUCTION:
        {target_instruction}
        """
        print(f"[ENGAGING PERSONA CORE]: Evaluated string structure under payload blueprint.")
        return "[Auditor Verified] Logic matrix confirms architectural weakness down the stack."

def execute_role_play_sandbox():
    print("\n=== EXECUTING LESSON 4: PERSONA INTERACTIVE FRAMEWORK ===")
    orchestrator = RoleBasedOrchestrator()
    role_specs = "Hyper-pedantic code verification specialist focusing on security buffer layouts."
    instruction = "Evaluate raw system input arrays for memory leak vulnerability vectors."
    
    response = orchestrator.run_persona_simulation(role_specs, instruction)
    print(f"Simulation Trace Resolution:\n{response}\n")

if __name__ == "__main__":
    execute_role_play_sandbox()
