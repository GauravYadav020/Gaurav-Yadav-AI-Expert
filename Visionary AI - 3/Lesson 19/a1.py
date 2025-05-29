import requests

# Your Hugging Face API token (replace with your own if needed)
API_TOKEN = "hf_YOUR_API_TOKEN_HERE"
API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"

# Headers for authentication
headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

# Text to analyze
user_text = "I love learning Python and AI. It's amazing!"

# Create a request payload
payload = {
    "inputs": user_text
}

# Send POST request to Hugging Face API
response = requests.post(API_URL, headers=headers, json=payload)

# Parse the JSON response
result = response.json()

# Print response
print("API Response:", result)

# Extract and display the label
label = result[0]['label']
confidence = result[0]['score']
print(f"\nSentiment: {label} (Confidence: {confidence:.2f})")
