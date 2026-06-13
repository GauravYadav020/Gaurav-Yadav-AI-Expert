"""
M12 Lesson 4 – Safe AI Image Generation with Gemini API
"""


import config
from huggingface_hub import InferenceClient

MODELS = getattr(
    config,
    "HF_MODELS",
    ["meta-llama/Llama-3.1-8B-Instruct"],
)

def generate_response(prompt: str, temperature: float = 0.3, max_tokens: int = 512) -> str:
    key = getattr(config, "HF_API_KEY", None)
    if not key:
        return "Error: HF_API_KEY missing in config.py"

    last_err = None
    for m in MODELS:
        try:
            c = InferenceClient(model=m, token=key)
            r = c.chat_completion(
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=max_tokens,
            )
            return r.choices[0].message.content
        except Exception as e:
            last_err = e

    return (
        "Hugging Face model failed.\n"
        f"Tried models: {MODELS}\n"
        "Fix:\n"
        "1) Switch to Groq by importing groq.py in main.py OR\n"
        "2) Replace HF model in hf.py (HF_MODELS).\n"
        f"Details: {type(last_err).__name__}: {last_err}"
    )

# //////////////
import streamlit as st

def main():
    st.title("🎨 Safe AI Image Generator")
    st.write("Powered by Gemini - with safety filters")
    
    prompt = st.text_area("Describe the image you want to generate")
    style = st.selectbox("Style", ["Realistic", "Cartoon", "Abstract", "Oil Painting"])
    
    if st.button("Generate Image"):
        if prompt:
            safe_prompt = f"Safe, family-friendly image: {prompt} in {style} style"
            st.write("Generating:", safe_prompt)
            # In real app: Use Gemini's image generation API
            st.image("https://picsum.photos/600/400", caption="Generated Image (Placeholder)")
            st.success("Image generated safely!")
        else:
            st.warning("Please enter a prompt")
    
    st.subheader("Activity 1: Content Safety Filter")
    st.write("Implement keyword blocking for inappropriate content")
    
    st.subheader("Activity 2: Multiple Styles")
    st.write("Add variation options")
    
    st.subheader("Activity 3: Gallery")
    st.write("Save and display previous generations")

if __name__ == "__main__":
    main()