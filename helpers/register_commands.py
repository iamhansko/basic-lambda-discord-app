import requests
from time import sleep

########################################
APPLICATION_ID = ''
BOT_TOKEN = ''
########################################

HEADERS = {"Authorization": f"Bot {BOT_TOKEN}"}
global_url = f"https://discord.com/api/v8/applications/{APPLICATION_ID}/commands"

def publish_command(url, commands):
    r = requests.post(url, headers=HEADERS, json=commands)
    if r.status_code != 200:
        sleep(20)
        print(f"Post to {url} failed; retrying once")
        r = requests.post(url, headers=HEADERS, json=commands)
    print(f"Response from {url}: {r.text}")

def get_all_commands(url):
    existing_commands = requests.get(url, headers=HEADERS).json()
    if not existing_commands:
        return []

def delete_command(url):
    r = requests.delete(url, headers=HEADERS)
    print(r.text)

def run():
    commands = [
        {
            "name": "cat",
            "description": "Call your Cat",
        }
    ]
    for command in commands:
        publish_command(global_url, command)
        print()
    print(f"{len(commands)} published")

if __name__ == "__main__":
    run()