from bs4 import BeautifulSoup
import requests
import random

# trial and error

# numbers = random.sample(range(800,838), 8)
# print(numbers)
# for num in numbers:
#     url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={num}"
#     req = requests.get(url).text
#     soup = BeautifulSoup(req, 'html.parser')
#     lucky = soup.select("ball_645")
#     for tag in soup.select('.ball_645'):
#         print(tag.text, end = " ")
    #     lucky = tag.select('.ball_645')
    # print(f"{num}회차 당첨번호 : {lucky}")

"""
로또 num회차 당첨번호 구하기
1 2 3 4 5 6 + 7
"""

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



