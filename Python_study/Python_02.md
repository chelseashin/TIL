##  Python_02

date : 2018-12-18

author : chaewonshin

title : open files and work/Web Scraping

----

**INDEX**

1. String Interpolation

2. 파일명 바꾸기

3. 웹스크래핑

4. GitHub-static-website

   ​	

### 1. String Interpolation(문자열 삽입)

----

```python
# python 과거
'일은 영어로 %s, 이는 영어로 %s' % ('one', 'two')

# pyformat
'{}, {}'.format('one', 'two')
name = '신채원'
e_name = 'chaewonshin'
print(name, e_name)
print('안녕하세요. {}입니다. My name is {}.'. format(name, e_name))
print('안녕하세요. {0}입니다. My name is {1}.'. format(name, e_name))
print('안녕하세요. {1}입니다. My name is {1}.'. format(name, e_name))
```

```python
# f-string python 3.6
print(f'안녕하세요. {name}입니다. My name is {e_name}.')
```

```python
# 어렵다면 이렇게!
name = "신채원"
print("안녕하세요." + name + "입니다." )
```



> lotto quiz

```python
import random
num = list(range(1, 46))
print(num)
lotto = sorted(random.sample(num, k = 6))
lotto
print(lotto)

lotto = random.sample(num, k = 6)
lotto.sort()
print(lotto)
```

> lotto quiz 2

```python
print(num)
lotto2 = sorted(random.sample(num, k = 6))
lotto2
print(f'로또 이번주 당첨번호는 {lotto2}입니다.')
```



----

##### dummy_test

----

```python
# make_dummy_files.py

import os
import random
family = ['김','이','박','최','황','오','강','한','제갈','하','정','송','현','손','조']
given = ['길동','준','민준','소미','수진','지은','동해','민태','준호','세정','지훈','성우','성원']

# 이름 생성하기
for i in range(500):
    cmd = f"touch {str(i)}_{random.choice(family)}{random.choice(given)}.txt"
    print(cmd)
    os.system(cmd)
```



----

### 2. 파일명 바꾸기

> [zzu.li/dummy](http://zzu.li/dummy) 에서 가져온 코드 그대로 bash 에서 실행.
>
> 이제 500 개의 지원서를 조작해보자.

- import os

1. `os.chdir(r'폴더주소')` : 작업하고 있는 위치 변경
2. `os.listdir('폴더주소')` : 저장된 디렉토리 전체 파일 목록 얻기
3. `os.rename('현재파일명','바꿀 파일명')`

----

```python
# 파일 이름 변경하기
# dummy 폴더 안에 있는 사람들의 이름 앞에 SAMSUNG 붙이기

#1 os 를 import 한다.
import os

#2 해당 폴더로 들어간다.
os.chdir(r"C:\Users\student\Desktop\TIL\dummy")

#3 폴더 안에 모든 파일을 돌면서 이름을 바꾼다.
for filename in os.listdir("."):
    os.rename(filename,"SAMSUNG " + filename)    
```

```python
# SAMSUNG이 아니라 SSAFY로 바꾸기!

#1 os 를 import 한다.
import os 

#2 해당 폴더로 들어간다.
os.chdir(r"C:\Users\student\Desktop\TIL\dummy")

#3 폴더 안에 모든 파일을 돌면서 이름을 바꾼다.
for filename in os.listdir("."):
    os.rename(filename, filename.replace("SSAFY SSAFY", "SSAFY"))
```



----

##### make_txt

----

```python
# file을 열고 작업한 후 닫기
# make 1
f = open("new.txt", "w", encoding='utf-8')
f.write("What a wonderful world!")
f.close()
```

```python
# 같은 명령  with문으로 작성
# make 2
with open("new.txt", "w") as f:
    f.write("Hello !!")
```

*make 1과 make 2 는 같은 명령*

```python
#  f-string 이용하여 파일생성과 작업 후 닫기
f = open("new.text", "r")
data = f.read()
print(data)
f.close()
```

----

* practice

  >  몇 번째 줄인지 표시하기

  ```python
  # 방법 1
  f = open("new.txt", "w", encoding = 'utf-8')
  num = list(range(1, 16))
  for i in num:
      data = f'{i}번째 줄입니다. \n'    
      f.write(data)
  f.close()
  ```

  ```python
  # 방법 2
  f = open("new.txt", "w", encoding = 'utf-8')
  for i in range(5):
      data = f'{i}번째 줄입니다. \n'    
      f.write(data)
  f.close()
  ```

  ```python
  # 방법 3(with문)
  with open("new.txt", "w", encoding = 'utf-8') as f:
      for i in range(10):
          data = f'{i}번째 줄입니다. \n' 
          f.write(data)
  ```

  > menu 고르기

  ```python
  menu = ["카레\n", "짜장\n", "탕수육\n"]
  m =  open("menu.txt", "w", encoding = 'utf-8')
  m.writelines(menu)
  m.close()
  ```

  > menu 고르기2(with문)

  ```python
  menu = ["카레\n", "짜장\n", "탕수육\n"]
  with open("menu.txt", "w", encoding = 'utf-8') as f:
  	f.writelines(menu)
  ```



  >   line.txt

  ```python
  f = open("line.txt","w", encoding = 'utf-8')
  numbers = [1, 2, 3, 4, 5]
  for i in numbers:
      words = f'{i}번째입니다.\t'
      f.write(words)
  f.close()
  ```

  > ssafy.txt(with문)

  ```python
  with open("ssafy.txt", "w", encoding = 'utf-8') as f:
      for i in range(5):
          data = f'{i}번째 단어\t'
          f.write(data)
  ```



### 3. 웹 스크래핑

> 하나하나씩 내용물 찍어보면서 진행!

- requests

```python
import requests
req = requests.get("https://www.google.com")
print(req)
print(req.text)
print(req.status_code)
```

#### 3-1. 정보 스크랩 1단계

1. 원하는 정보가 있는 주소로 요청을 보내, 응답을 저장한다.

```python
import requests
req = requests.get("https://www.google.com").text
```

1. 정보를 출력하여 확인한다.

```python
print(req)
```

#### 3-2. 코스피 지수

- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#)

```python
import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.google.com")

soup = BeautifulSoup(req, 'html.parser')
soup.select(경로)
soup.select_one(경로)
```

#### 3-3. 정보 스크랩 2단계

1. 정보를 조작하기 편하게 바꾸고,

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(req, 'html.parser')
```

1. 바꾼 정보 중 원하는 것만 뽑아서,

```python
kospi = soup.select_one(‘selector 경로’)
```

1. 출력한다

```pythno
print(kospi.text)
```

- kospi

```python
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/"
req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')
kospi = soup.select_one('#KOSPI_now')

print(kospi.text)
```

**실습-1 네이버 실시간 검색어 스크래핑**

```python
import requests
from bs4 import BeautifulSoup

url = 'https://www.naver.com/'
req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')

for tag in soup.select('.PM_CL_realtimeKeyword_rolling .ah_item .ah_k'):
    print(tag.text)
```