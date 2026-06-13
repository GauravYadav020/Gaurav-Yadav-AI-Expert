import requests

# Replace with your Hugging Face API token
API_TOKEN = "hf_YOUR_API_TOKEN_HERE"
API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"

headers = {"Authorization": f"Bearer {API_TOKEN}"}

def classify_text(text):
    payload = {"inputs": text}
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        result = response.json()
        label = result[0]['label']
        score = result[0]['score']
        return label, score
    else:
        return None, None

def main():
    print("📝 Hugging Face Text Classification")
    print("Type 'exit' to quit.\n")

    while True:
        text = input("Enter text to classify: ")
        if text.lower() == 'exit':
            break

        label, score = classify_text(text)
        if label:
            print(f"Sentiment: {label} (Confidence: {score:.2f})\n")
        else:
            print("Error: Could not classify text.\n")

if __name__ == "__main__":
    main()
