## Python_05

date : 2018-12-21

author : chaewonshin

title : Lotto/Telegram

----

#### Lotto 1

```python
"""
로또 num회차 당첨번호 구하기
1 2 3 4 5 6 + 7
"""

from bs4 import BeautifulSoup
import requests
import random

numbers = random.sample(range(800,838), 8)
for num in numbers:
    count = 0
    url = f"https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={num}"
    req = requests.get(url).text
    soup = BeautifulSoup(req, "html.parser")
    lucky = soup.select(".ball_645")
    print(f"{num}회차 당첨번호")
    for i in lucky:
        print(i.text, end = " ")
        count += 1
        if count == 6:
            print("+", end = " ")
    print()
```



#### Lotto 2

```python
import random
import requests
import json
from pprint import pprint

# pprint(lotto)
# print(type(lotto))

"""
0. random 으로 로또번호 생성합니다.
1. API를 통해 우승 번호를 가져옵니다
2. 0번과 1번을 비교하여 나의 등수를 알려줍니다.
-----------

1) url요청 보내서 정보를 가져옵니다.
    - json으로 받는다.(딕셔너리로 접근 가능)
2) API의 당첨번호와 보너스 번호를 저장하고,
3) 뽑은 게 몇 등인지 하는 거 뽑기!
"""


url = "https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
res = requests.get(url)
lotto = res.json()

winner = []
for i in range(1, 7):
    winner.append(lotto[f"drwtNo{i}"])
print(winner)

bonus = lotto["bnusNo"]
print("이번 주 당첨번호 : " + str(winner))
print("보너스 번호 : "+ str(bonus))

count = 0
while True:
    count += 1   # 들어올 때마다 더해짐
    my_numbers = sorted(random.sample(range(1, 46), 6))
    matched = len(set(winner) & set(my_numbers))

    if matched == 6:
        print("1등입니다")
        # print(count, "번만에 당첨되셨습니다.")
        # money = format(count*1000, ',')
        # print(money, "원 써서 받았습니다.")
        # break
    elif matched == 5:
        if bonus in my_numbers:
            print("2등입니다")
        else:
            print("3등입니다")
    elif matched == 4:
        print("4등입니다")
    elif matched == 3:
        print("5등입니다")
        print(count, "번만에 당첨되셨습니다.")
        money = format(count*1000, ',')
        print(money, "원 써서 받았습니다.")
        break
    else:
        print("꽝!") 
```



#### Telegram

- Chatbot

  ```python
  import requests
  from bs4 import BeautifulSoup
  import os
  
  token = os.getenv("TELEGRAM_BOT_TOKEN")
  method_name = "getUpdates"
  url = f"https://api.telegram.org/bot{token}/{method_name}"
  # chat_id = 540753224
  
  # json파일에서 내 id 가져오기
  update = requests.get(url).json()
  # print(update)
  chat_id = update["result"][0]["message"]["chat"]["id"]
  print(chat_id)
  
  # msg = "안녕하세요~"
  # 메세지로 네이버 코스피를 가져와 메세지로 보내기
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
  ```


