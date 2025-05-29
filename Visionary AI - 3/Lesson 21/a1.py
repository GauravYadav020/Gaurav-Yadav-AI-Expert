import requests
import time

def get_useless_fact():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    try:
        response = requests.get(url)
        data = response.json()
        return data.get("text", "No useless fact found.")
    except Exception as e:
        return f"Error: {e}"

def get_cat_fact():
    url = "https://catfact.ninja/fact"
    try:
        response = requests.get(url)
        data = response.json()
        return data.get("fact", "No cat fact found.")
    except Exception as e:
        return f"Error: {e}"

def get_dog_fact():
    url = "https://dog-api.kinduff.com/api/facts"
    try:
        response = requests.get(url)
        data = response.json()
        return data.get("facts", ["No dog fact found."])[0]
    except Exception as e:
        return f"Error: {e}"

def main():
    print("🔍 Exploring Random Facts from Multiple APIs 🔍\n")
    
    for i in range(3):
        print(f"Useless Fact #{i+1}: {get_useless_fact()}\n")
        time.sleep(1)
        
        print(f"Cat Fact #{i+1}: {get_cat_fact()}\n")
        time.sleep(1)
        
        print(f"Dog Fact #{i+1}: {get_dog_fact()}\n")
        time.sleep(2)

if __name__ == "__main__":
    main()
