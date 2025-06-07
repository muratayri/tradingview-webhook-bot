from flask import Flask, request
import requests

app = Flask(__name__)

# Bot bilgilerini buraya gir
BOT_TOKEN = '7353388216:AAH0N_8DgQeWT1QWXmT_nhnxQn6AHi1wCPs'
CHAT_ID = 'YOUR_CHAT_ID'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = f"🔔 Sinyal Geldi!\nParite: {data.get('pair', 'bilinmiyor')}\nYön: {data.get('type', 'bilinmiyor')}\nFiyat: {data.get('price', 'yok')}"
    send_telegram(message)
    return 'ok', 200

def send_telegram(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {'chat_id': CHAT_ID, 'text': text}
    requests.post(url, data=payload)

if __name__ == '__main__':
    app.run()
