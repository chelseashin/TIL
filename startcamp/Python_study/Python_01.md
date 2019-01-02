## Python_01

date : 2018-12-17

author : chaewonshin

title : print numbers

----

#####  다음 리스트의 요소들을 한줄로 출력하시오(for문 사용)

----

```python
# numbers = [2, 3, 6, 11, 8]
# 답 예시 => 2 3 6 11 8

numbers = [2, 3, 6, 11, 8]
print(numbers)

for i in numbers:
	print(i, end = " ")
```

----



##### 주어진 리스트의 요소들 중에서 자연수가 홀수인지 짝수인지 판별하여 

##### 각각의 리스트로 출력하여라.

----

```python
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 답 예시
# [2, 6, 8] 짝수입니다
# [3, 11] 홀수입니다

odd = []
even = []

for number in numbers:

    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print(even, "짝수입니다")
print(odd, "홀수입니다")

```



* ##### 조건문 활용하기 - 미세먼지 데이터

```python
import requests
from bs4 import BeautifulSoup
url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?sidoName=%EB%8C%80%EC%A0%84&ServiceKey=QaGapZXPV5DTM72fy6lrf3hJnrJxhila1UVkPlUCo0N0g0F0RZ9WEngT8RkNjNo4IF%2BikV%2BthQLze39nK4IQjA%3D%3D&ver=1.3&pageNo=2'
request = requests.get(url).text
soup = BeautifulSoup(request,'xml')
daejeon = soup('item')[0]
location = daejeon.stationName.text
time = daejeon.dataTime.text
dust = int(daejeon.pm10Value.text)


print(f"{time} 기준 \n대전 {location}의 미세먼지 농도는 {dust} 입니다.")


# dust 변수에 들어 있는 값을 기준으로 상태 정보를 출력해보세요.
if(150 < dust):
  print("매우나쁨")
elif(80 < dust <= 150):
  print("나쁨")
elif(30 < dust and dust <= 80):
  print("보통")
else:
  print("좋음")
```



* ##### 반복문 활용하기 - 여러번 인사하기

```python
greeting = "안녕하세요??"

for i in range(5):
    print(greeting)
```

- 웹 API 란?

  - 미세먼지 데이터 살펴보기


* ##### 외장함수 `random` - 로또

```python
import random

numbers = list(range(1,46))
lotto = random.sample(numbers, 6)
print(lotto)
import random

numbers = list(range(1,46))
lotto = random.sample(numbers, 6)
print(sorted(lotto))
import random

numbers = list(range(1,46))
lotto = random.sample(numbers, 6)
print(f"오늘의 행운의 번호는 {sorted(lotto)} 입니다")
```