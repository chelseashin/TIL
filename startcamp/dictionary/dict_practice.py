"""
파이썬  dictionary 활용 기초!
"""

dict = {
    "대전" : 23,
    "서울" : 30,
    "구미" : 20
}
# type을 알고 싶을 때
# print(type(dict.values()))


# 1. 평균을 구하시오.

# score = {
#     "국어" : 87,
#     "영어" : 92,
#     "수학" : 40
# }

# print(score.values())

#  A 1
# value = 0
# for i in score.values():
#     value = value + i
# print(value/len(score.values()))

# A 2
# value = 0
# for i in score.values():
#     value = value + i
#     mean = value/len(score.values())
# print(mean)

# A 3
# total_score = 0
# for score in score.values():
#     total_score = total_score + score
#     total_score += score (위와 같음!)
# average_score = total_score /len(score.values())
# print(average_score)



# 2. 반 평균을 구하시오
scores = {
    "철수" : {
        "수학" : 80,
        "국어" : 90,
        "음악" : 100
    },
    "영희" :  {
        "수학" : 70,
        "국어" : 60,
        "음악" : 50
    }
}

# print(scores)
# print(scores.values())
# print(type(scores.values()))
# total = scores.values()
# print(total)

# 다시 풀어보자
# total_score = 0
# count = 0
# for per_score in scores.values():
# #    print(per_score)
#     for ind_score in per_score.values():
#         total_score += ind_score
# #       total_score = total_score + ind_score(위와 같은 식! 누적된다는 의미)
#         count += 1
# mean_score = total_score / count
# print(mean_score)

# 3. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
cities = {
    "서울" : [-6, -10, 5],
    "대전" : [-3, -5, 2],
    "광주" : [0, -2, 10],
    "부산" : [2, -2, 9]
 }

#  cities_min = min(cities.values())
#  cities_max = max(cities.values())
#  print(cities_min)
#  print(cities_max)

# name, temp
# max()
# min()
# print(cities)
print(cities.items())

# A 1
hot = 0
cold = 0
hot_city = ""
cold_city = ""
count = 0

for name, temp in cities.items():
    # name = "서울"
    # temp = [-6, -10, 5]
    if count == 0:
        hot = max(temp)
        cold = min(temp)
        hot_city = name
        cold_city = name
    else:
        # 최저 온도가  cold 보다 더 추우면, cold에 넣고
        if min(temp) < cold:
            cold = min(temp)
            cold_city = name
        # 최고 온도가 hot 보다 더 더우면, hot에 넣고
        if max(temp) > hot:
            hot = max(temp)
            hot_city = name
    count += 1

print(f"{hot_city}, {cold_city}")