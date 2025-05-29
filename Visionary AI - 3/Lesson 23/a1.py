import requests

API_TOKEN = "hf_YOUR_API_TOKEN_HERE"  # Replace with your Hugging Face API token
API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"

headers = {"Authorization": f"Bearer {API_TOKEN}"}

def analyze_sentiment(text):
    payload = {"inputs": text}
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        results = response.json()
        return results
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def main():
    print("🧠 Sentiment Analysis Tool with Hugging Face")
    print("Enter multiple sentences, separated by a blank line. Type 'exit' to quit.\n")

    while True:
        print("Enter your text (or type 'exit'):")
        lines = []
        while True:
            line = input()
            if line.strip().lower() == "exit":
                return
            if line == "":
                break
            lines.append(line)

        text = " ".join(lines).strip()
        if not text:
            print("No input detected. Please enter some text.\n")
            continue

        results = analyze_sentiment(text)
        if results:
            for i, res in enumerate(results):
                label = res.get("label", "N/A")
                score = res.get("score", 0)
                print(f"Sentence {i+1} Sentiment: {label} (Confidence: {score:.2f})")
            print()
        else:
            print("Failed to analyze sentiment.\n")

if __name__ == "__main__":
    main()
