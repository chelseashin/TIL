## Python_03

date : 2018-12-19

author : chaewonshin

title : 제어문/html,css

----

> - 아래 코드의 출력 결과를 예상하라
>
>   ```python
>   if True:
>       if False:
>           print("1")
>           print("2")
>       else:
>           print("3")
>   else:
>       print("4")
>   print("5")
>   
>   
>   # 정답
>   3
>   5
>   # if - else 구문을 만나면 조건에 충족(True)하는 하나의 구역만 실행한다는 사실 유의!
>   ```



#### 제어문

----

```python
'''
Q1
# 자연수 n이 주어졌을 때, 1부터  N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오
'''
# input() : 사용자의 입력 값을 받는다.

# A 1
n = int(input('숫자를 입력하세요: '))
for i in range(n):
    print(i+1)
    
    
# A 2
n = int(input('숫자를 입력하세요: '))
for i in range(1,n+1):
    print(i)
```

----

```python
'''
Q2
투자 경고 종목 리스트가 있을 때, 사용자로부터 종목명을 입력받은 후 해당 종목이 
투자 경고 종목이라면 '투자 경고 종목입니다'를 아니면
"투자경고 종목이 아닙니다"를 출력하는 프로그램을 작성하라
'''

warn_investment_list = ["microsoft", "google", "naver", "kakao", "samsung", "lg"]
print(f"경고 종목 리스트: {warn_investment_list}")
item = input('투자종목이 무엇입니까?: ')

# A 1
if item in warn_investment_list:
    print("투자 경고 종목입니다")
else:
    print("투자 경고 종목이 아닙니다")

# A 2
if item.lower() in warn_investment_list:
    print("WARNING!")
else:
    print("SAFE")

# .lower() : 입력값에 대문자가 들어와도 소문자로 바꿔주는 것.
# if - not in 일 때는 논리구조가 반대로 된다.
# if x in y : x 가 in 에 포함되어 있는지 판단. (있다면 True) <-> if x not in y

```

----

```python
'''
Q2
# 다음 리스트에서 0, 4, 5번째 항목을 제외한 새로운 리스트를 생성하시오
'''

# 튜플(tuple)
# 리스트는 [ 과 ]으로 둘러싸지만 튜플은 ( 과 ) 으로 둘러싼다.
# 리스트는 그 값의 생성, 삭제, 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다.

colors = ['Apple', 'Banana', 'Coconut', 'Deli', 'Ele', 'Grape']

# A1
deleteindex = [0, 4, 5]
fruit = []

for i in range(0, len(colors)):
    if i not in deleteindex:
        fruit.append(colors[i])
print(fruit)


# A2
fruit = []

for color in colors:
    if colors.index(color) not in (0, 4, 5):
        fruit.append(color)
print(fruit)


# A3
fruit = []

for a in colors:
    if a not in colors[0] and a not in colors[4] and a not in colors[5]:
        fruit.append(a)
print(fruit)
```



#### ssafy_dictionary

----

```python
# ssafy_dictionary
ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"]
        }
    },
    "duration": {
        "semester1": "6월까지"
    },
    "classes": {
        "seoul":  {
            "lecturer": "john",
            "manager": "pro",
        },
        "daejeon":  {
            "lecturer": "tak",
            "manager": "yoon",
        }
    }
}


# print(ssafy)

# ssafy의 semester1의 기간을 출력하세요.
# dict = ["key" : value]
print(ssafy["duration"]["semester1"])

# ssafy의 dictionary 안에 들어있는 '대전'을 출력하세요
print(ssafy["location"][1])

# daejeon의 매니저의 이름을 출력하세요
print(ssafy["classes"]["daejeon"]["manager"])
```



### html 

* page 만들기

----

index.html

----

```python
<!DOCTYPE html>
<html lang = "en">
    <head> 
        <!-- 3. using css file -->
        <link rel="stylesheet" href="style.css">
        <meta charset = "utf-8">
        <title>채원이의 블로그</title>
        <link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet">
        <!-- 1. embedding style -->
        <style>
            /* h1 { color : blueviolet;} */
        </style>
    </head>
    <body>
        <!-- 2. inline styling -->
        <h1 class ="ssafy" style = "color:blueviolet;">Hello Chelsea</h1>
        <div class="container">
            <p id="datascience">데이터사이언스</p>
            <p id="coding">코딩 열심히 해야겠습니다.</p>
            <span>
                <p>paragraph3</p>
            </span>
        </div>
        <hr>
        <p>안녕하세요!</p>
        <p>채원입니다</p><br>
        <hr>
        <p class="text-center">Center</p>
        <p class="text-large text-red">Large Red</p>
        <p class="text-center">Center Large Blue</p>
        <!-- 이미지 태그 -->
        <img src="https://avatars1.githubusercontent.com/u/45935233?s=460&v=4" alt="chelsea">
        <p id="uniq" class="ssafy daejeon development"></p>

    </body>
</html>
```



* style.css

----

```python
.text-center {
    text-align: center;
}

.text-large {
    font-size: 200%
}

h1, p {
    color:violet;
}

body {
    background:rgb(236, 222, 236);
}

#datascience {
    color:olive;
}


.container {
    background:rgb(236, 177, 171);
}

.text-red{
    color:red;
}
.text-center{
    color:royalblue;
}


div p {
    color:green;
}


div > p {
    color:hotpink;
}

p ~ span{
    color:orange
}
```

