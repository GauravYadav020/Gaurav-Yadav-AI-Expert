import requests

API_TOKEN = "hf_YOUR_API_TOKEN_HERE"  # Replace with your Hugging Face API token
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

headers = {"Authorization": f"Bearer {API_TOKEN}"}

def summarize_text(text):
    payload = {
        "inputs": text,
        "parameters": {
            "max_length": 150,
            "min_length": 30,
            "do_sample": False
        }
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        result = response.json()
        summary = result[0]['summary_text']
        return summary
    else:
        return f"Error: {response.status_code} - {response.text}"

def main():
    print("📝 Text Summarization Using Hugging Face LLM\n")
    print("Enter text to summarize (type 'exit' to quit):\n")

    while True:
        text = input("Your text: ")
        if text.lower() == "exit":
            break
        if len(text.strip()) == 0:
            print("Please enter some text to summarize.\n")
            continue

        summary = summarize_text(text)
        print(f"\nSummary:\n{summary}\n")

if __name__ == "__main__":
    main()
