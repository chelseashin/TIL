import requests
from bs4 import BeautifulSoup

# req = requests.get("https://finance.naver.com/sise/").text
# soup = BeautifulSoup(req, 'html.parser')
# kospi = soup.select_one("#KOSPI_now")
# print(kospi.text)


# music = requests.get("https://music.naver.com/").text
# soup = BeautifulSoup(music, 'html.parser')
# star = soup.select_one("#domastic > a")
# print(star.text)

# music = requests.get("https://music.naver.com/").text
# soup = BeautifulSoup(music, 'html.parser')
# player = soup.select_one("#snb > div.musicplayer_btn > a")
# print(player.text)

# sports = requests.get("https://sports.news.naver.com/index.nhn").text
# soup = BeautifulSoup(sports, 'html.parser')
# news = soup.select_one("#mostCommentedNewsList")
# print(news.text)

# now = requests.get("https://www.naver.com/").text
# soup = BeautifulSoup(now, 'html.parser')
# time = soup.select_one("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul")
# print(time.text)

# for문을 이용한  webscraping
naver = "https://www.naver.com/"
req = requests.get(naver).text
soup = BeautifulSoup(req, 'html.parser')

for tag in soup.select('.PM_CL_realtimeKeyword_rolling .ah_item'):
    rank = tag.select_one('.ah_r').text
    issue = tag.select_one('.ah_k').text
    print(f'{rank}위는 {issue}입니다')
