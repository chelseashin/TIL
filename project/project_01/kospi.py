# import requests
# from bs4 import BeautifulSoup
# req = requests.get("https://google.com")

# print(req)
# print(req.text)
# print(req.status_code)

# soup = BeautifulSoup(req, 'html.parser')
# kospi = soup.select_one('경로')

import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'
req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')
kospi = soup.select_one('#KOSPI_now')

print('현재 코스피 지수는', kospi.text, '입니다!')