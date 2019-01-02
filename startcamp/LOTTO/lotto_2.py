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

