# # movie_project_신채원
# # 파일 읽기
# # movie.csv 파일 열기
 
# f = open('movie.csv', 'r', encoding='utf-8')
# movie = csv.reader(f)
# for line in movie:
#     print(line)
# # f.close()


# # movie_naver.csv 파일 열기

# f = open('movie_naver.csv', 'r', encoding='utf-8')
# movie_naver = csv.reader(f)
# for movies in movie_naver:
#     print(movies)


# # boxoffice.csv 파일 열기

# f = open('boxoffice.csv', 'r', encoding='utf-8')
# boxoffice = csv.reader(f)
# for box in boxoffice:
#     print(box)
# ---------------------------------------------------------------------
# import csv
# with open('boxoffice.csv', newline='', encoding='utf-8') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row['movie_code'], row['title'], row['audience'], row['recorded_at'])


# 주간 data 가져오기
# import requests
# import csv
# import json
# from pprint import pprint


# url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={my_key1}&targetDt=20190113"
# res = requests.get(url)
# movie = res.json()

# # pprint(movie)
# top_movie = movie['boxOfficeResult']['weeklyBoxOfficeList']
# # print(movie['boxOfficeResult']['weeklyBoxOfficeList'][1]['movieNm'])
# # pprint(top_movie)
# # print(len(top_movie))

# movie_code = []
# movie_title = []
# performance = []
# record_day = []

# for i in range(len(top_movie)):
#     movie_code.append(movie['boxOfficeResult']['weeklyBoxOfficeList'][i]['movieCd'])
#     movie_title.append(movie['boxOfficeResult']['weeklyBoxOfficeList'][i]['movieNm'])
#     performance.append(movie['boxOfficeResult']['weeklyBoxOfficeList'][i]['audiAcc'])
#     record_day.append(movie['boxOfficeResult']['showRange'])

# # print(movie_code)
# # print(movie_title)
# # print(performance)
# # print(record_day)

# with open('boxoffice.csv', 'w', newline='', encoding='utf-8') as f:
#    fieldnames = ('movie_code', 'movie_title', 'performance', 'record_day')
#    writer = csv.DictWriter(f, fieldnames=fieldnames)

#    writer.writeheader()
#    for i in range(len(top_movie)):
#        writer.writerow({'movie_code': movie_code[i], 'movie_title': movie_title[i], 'performance':performance[i], 'record_day':record_day[i]})

# with open('boxoffice.csv', newline='', encoding='utf-8') as csvfile:
#    reader = csv.DictReader(csvfile)
#    for row in reader:
#        print(fieldnames)
#        print(row['movie_code'], row['movie_title'], row['performance'], row['record_day'])


# 10주치 데이터 가져오기
import requests
import os
import csv
import json
from pprint import pprint

movie_code = []
movie_title = []
performance = []
record_day = []
target_day = [20181111, 20181118, 20181125, 20181202, 20181209, 20181216, 20181223, 20181230, 20190106, 20190113]

for i in range(len(target_day)):

    url = f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={my_key1}&targetDt={target_day[i]}"
    res = requests.get(url)
    movie = res.json()
    top_movie = movie['boxOfficeResult']['weeklyBoxOfficeList']

    for v in range(10):
        if top_movie[v]['movieCd'] not in movie_code:
            movie_code.append(top_movie[v]['movieCd'])
            movie_title.append(top_movie[v]['movieNm'])
            performance.append(top_movie[v]['audiAcc'])
            record_day.append(target_day[i])

# print(movie_code)
# print(movie_title)
# print(performance)
# print(record_day)
    

with open('boxoffice.csv', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ('movie_code', 'movie_title', 'performance', 'record_day')
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    
    for i in range(len(movie_code)):
        writer.writerow({'movie_code': movie_code[i], 'movie_title': movie_title[i], 'performance':performance[i], 'record_day':record_day[i]})