# boxoffice.csv 파일 열어서 movie_code 리스트로 저장

import requests
import csv
import json
from pprint import pprint

movie_code = []
f = open('boxoffice.csv', 'r', encoding='utf-8')
boxoffice = csv.reader(f)
for i in boxoffice:
    movie_code.append(i[0])
del movie_code[0]
# print(movie_code)
# print(len(movie_code))

# url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={my_key2}&movieCd=20177538"
# res = requests.get(url)
# movie = res.json()
# movie_info = movie['movieInfoResult']['movieInfo']

# print(movie_info['movieNm'])
# print(movie_info['movieNmEn'])
# print(movie_info['movieNmOg'])
# print(movie_info['prdtYear'])
# print(movie_info['showTm'])
# print(movie_info['genres'][0]['genreNm'])
# print(movie_info['directors'][0]['peopleNm'])
# print(movie_info['audits'][0]['watchGradeNm'])
# print(movie_info['actors'][0]['peopleNm'])
# print(movie_info['actors'][1]['peopleNm'])
# print(movie_info['actors'][2]['peopleNm'])


# 영화 상세정보 - 전체 

import requests
import os
import csv
import json
from pprint import pprint

movie_code = []
f = open('boxoffice.csv', 'r', encoding='utf-8')
boxoffice = csv.reader(f)
for i in boxoffice:
    movie_code.append(i[0])
del movie_code[0]
# print(len(movie_code))

movie_name_ko = []
movie_name_en = []
movie_name_og = []
prdt_year = []
show_time = []
genres = []
directors = []
watch_grade_nm = []
actor1 = []
actor2 = [] 
actor3 = []

for i in range(len(movie_code)):
    url = f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={my_key2}&movieCd={movie_code[i]}"
    res = requests.get(url)
    movie = res.json()
    movie_info = movie['movieInfoResult']['movieInfo']

    movie_name_ko.append(movie_info['movieNm'])
    movie_name_en.append(movie_info['movieNmEn'])
    movie_name_og.append(movie_info['movieNmOg'])
    prdt_year.append(movie_info['prdtYear'])
    show_time.append(movie_info['showTm'])
    genres.append(movie_info['genres'][0]['genreNm'])
    directors.append(movie_info['directors'][0]['peopleNm'])
    watch_grade_nm.append(movie_info['audits'][0]['watchGradeNm'])
    # actor1.append(movie_info['actors'][0]['peopleNm'])
    # actor2.append(movie_info['actors'][1]['peopleNm'])
    # actor3.append(movie_info['actors'][2]['peopleNm'])
    if len(movie_info['actors']) >= 3:
        actor1.append(movie_info['actors'][0]['peopleNm'])
        actor2.append(movie_info['actors'][1]['peopleNm'])
        actor3.append(movie_info['actors'][2]['peopleNm'])
    elif len(movie_info['actors']) == 2:
        actor1.append(movie_info['actors'][0]['peopleNm'])
        actor2.append(movie_info['actors'][1]['peopleNm'])
        actor3.append('')
    elif len(movie_info['actors']) == 1:
        actor1.append(movie_info['actors'][0]['peopleNm'])
        actor2.append('')
        actor3.append('')
    else:
        actor1.append('')
        actor2.append('')
        actor3.append('')
    
        
with open('movie.csv', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ('movie_code', 'movie_name_ko','movie_name_en','movie_name_og', 'prdt_year', 'show_time', 'genres', 'directors', 'watch_grade_nm', 'actor1', 'actor2', 'actor3')
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    
    for i in range(len(movie_code)):
        writer.writerow({'movie_code': movie_code[i], 'movie_name_ko': movie_name_ko[i], 'movie_name_en': movie_name_en[i], 'movie_name_og': movie_name_og[i], 'prdt_year': prdt_year[i], 'show_time': show_time[i], 'genres': genres[i], 'directors':directors[i], 'watch_grade_nm':watch_grade_nm[i],'actor1':actor1[i], 'actor2': actor2[i], 'actor3':actor3[i]})