"""
Lesson: Introduction to Text-to-Image Generation

This lesson introduces the basics of generating images from text prompts using AI models like Stable Diffusion.
"""
"""
Simple Text-to-Image Generator
Uses primary model, automatically falls back to alternatives only if needed

INSTALLATION:
    pip install huggingface-hub pillow
"""
from huggingface_hub import InferenceClient
from datetime import datetime
from PIL import Image
from config import HF_API_KEY

# MODEL PRIORITY LIST - Primary model first, fallbacks only if it fails
MODELS = [
    "ByteDance/SDXL-Lightning",
    "stabilityai/stable-diffusion-xl-base-1.0",
    "stabilityai/sdxl-turbo",
    "runwayml/stable-diffusion-v1-5", # Fallback 2
]

# Initialize client
client = InferenceClient(api_key=HF_API_KEY)

print(f"Primary model: {MODELS[0]}")
print("Type 'quit' to exit\n")

while True:
    prompt = input("Enter prompt: ").strip()
    if prompt.lower() in ["quit", "exit", "q"]:
        break
    if not prompt:
        continue

    print("Generating...")
    image = None

    # Try each model in order until one works
    for model in MODELS:
        try:
            image = client.text_to_image(prompt, model=model)
            break  # Success! Exit the loop
        except Exception:
            print(f"  Executing next...")
            continue

    # If we got an image, save and display it
    if image:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"generated_{timestamp}.png"
        image.save(filename)
        print(f"✓ Saved: {filename}")
        image.show()
        print()
    else:
        print("Error: All models failed. Check your API key.\n")

print("Goodbye!")



# Example using Hugging Face (requires diffusers library)
# pip install diffusers torch transformers

def basic_text_to_image_prompt():
    """Basic function to demonstrate prompt engineering"""
    prompt = "A beautiful sunset over mountains, digital art style"
    print("Prompt:", prompt)
    print("This prompt would be fed to a model like Stable Diffusion to generate an image.")
    return prompt

# Activity 1: Basic Prompt Creation
def activity_1_create_prompts():
    print("\n--- Activity 1: Create Effective Prompts ---")
    prompts = [
        "A cyberpunk city at night with neon lights",
        "A peaceful Japanese garden with cherry blossoms",
        "A futuristic robot reading a book in a library"
    ]
    for i, p in enumerate(prompts, 1):
        print(f"Prompt {i}: {p}")
    print("Try creating 3 more detailed prompts yourself!")

# Activity 2: Negative Prompts
def activity_2_negative_prompts():
    print("\n--- Activity 2: Negative Prompts ---")
    positive = "A majestic lion in the savanna"
    negative = "blurry, low quality, deformed, ugly"
    print("Positive Prompt:", positive)
    print("Negative Prompt:", negative)
    print("Negative prompts help avoid unwanted elements in generated images.")

# Activity 3: Parameter Exploration
def activity_3_parameters():
    print("\n--- Activity 3: Understanding Parameters ---")
    print("Common parameters:")
    print("- Guidance Scale: How closely the image follows the prompt")
    print("- Steps: Number of denoising steps (higher = better quality)")
    print("- Seed: For reproducible results")

# After Class Project
def after_class_project():
    print("\n--- After Class Project ---")
    print("Create 5 unique text prompts across different themes (nature, fantasy, sci-fi, etc.)")
    print("Experiment with adding styles like 'oil painting', 'watercolor', 'cinematic'.")
    print("Document which prompts give the best results and why.")

if __name__ == "__main__":
    basic_text_to_image_prompt()
    activity_1_create_prompts()
    activity_2_negative_prompts()
    activity_3_parameters()
    after_class_project()
    print("\nLesson completed! Experiment with real AI image generators.")
