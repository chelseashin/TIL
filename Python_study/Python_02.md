##  Python_02

date : 2018-12-18

author : chaewonshin

title : open files and work



----

##### string_test

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

##### ch_name

----

```python
# 파일 이름 변경하기
# dummy 폴더 안에 있는 사람들의 이름 앞에 SAMSUNG 붙이기
import os
os.chdir(r"C:\Users\student\Desktop\TIL\dummy")
for filename in os.listdir("."):
    os.rename(filename,"SAMSUNG " + filename)
```

```python
# SAMSUNG이 아니라 SSAFY로 바꾸기!
import os 
os.chdir(r"C:\Users\student\Desktop\TIL\dummy")
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


