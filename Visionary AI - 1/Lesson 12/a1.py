import requests
from PIL import Image
from io import BytesIO

api_token="" #paste your api token inside the double  quote

print("Welcome to AI Art Buddy🖼️")
user_input = input("Enter a description for the image: ")
url = "https://api.monsterapi.ai/v1/generate/txt2img"
headers = {"Authorization": f"Bearer {api_token}"}
response = requests.post(url, json={"prompt": user_input, "safe_filter": True}, headers=headers)

if response.status_code == 200:
    print("Loading... The image may take a few seconds.")
    process_id = response.json().get("process_id")

    while True:
        status_data = requests.get(f"https://api.monsterapi.ai/v1/status/{process_id}", headers=headers).json()
        status = status_data.get("status")
        # print(status_data)

        if status == "COMPLETED":
            image_url = status_data['result']['output'][0]
            img = Image.open(BytesIO(requests.get(image_url).content))
            img.show()
            print()
            break
        elif status == "FAILED":
            print("Image generation failed.")
            break
else:
    print(f"Error: {response.status_code}")



