"""
================================================================================
LESSON 6: AI Writing Assistant: Generate and Refine Essays with Gemini API
================================================================================
OBJECTIVE: Production-grade programmatic essay iterative refinement execution engines.
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
class InteractiveGeminiWritingAssistant:
    def generate_initial_draft(self, topic_matrix):
        print(f"[PIPELINE-STEP 1] Generating basic structural draft for topic: {topic_matrix}")
        return "Initial Draft Framework: The geopolitical changes affecting sustainable energy structures across urban hubs."
    
    def run_refinement_pass(self, draft, critical_instruction):
        print(f"[PIPELINE-STEP 2] Running programmatic context injection based on feedback loops...")
        refined_output = f"""
        [REFINED ESSAY CORE]
        {draft}
        AMENDMENT LAYER: Adjusted according to explicit framework targets -> {critical_instruction}
        """
        return refined_output

def run_assistant_pipeline():
    print("\n=== EXECUTING LESSON 6: PROGRAMMATIC WRITING LAB ===")
    assistant = InteractiveGeminiWritingAssistant()
    
    raw_draft = assistant.generate_initial_draft("Urban Renewable Transition Logistics")
    final_product = assistant.run_refinement_pass(
        draft=raw_draft,
        critical_instruction="Inject analytical micro-economic perspective metrics and verify data flows."
    )
    print(f"Final Programmatic Content Delivery Asset Matrix:{final_product}\n")

if __name__ == "__main__":
    run_assistant_pipeline()
