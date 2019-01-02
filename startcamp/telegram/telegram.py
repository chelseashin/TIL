import requests
from bs4 import BeautifulSoup
import os

token = os.getenv("TELEGRAM_BOT_TOKEN")
method_name = "getUpdates"
url = f"https://api.telegram.org/bot{token}/{method_name}"
# chat_id = 540753224

update = requests.get(url).json()
# print(update)
chat_id = update["result"][0]["message"]["chat"]["id"]
print(chat_id)

# msg = "안녕하세요~"
naver = "https://finance.naver.com/sise/"
req = requests.get(naver).text
soup = BeautifulSoup(req, 'html.parser')
kospi = soup.select_one("#KOSPI_now")
msg = kospi.text
print(msg)

method_name = "sendmessage"
msg_url = f"https://api.telegram.org/bot{token}/{method_name}?chat_id={chat_id}&text={msg}"

# print(msg_url)
# bot으로 메세지 보내기
print(requests.get(msg_url))

