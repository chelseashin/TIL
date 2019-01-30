2019-01-30

< Flask >

* 프로그래밍 폰트
* web 프로젝트 정리
* gitlab
* flask c9 setting
* flask datetime
* flask variable
* render template
* flask 조건 반복



```python
from flask import Flask, render_template
import os
import datetime
app = Flask(__name__)

@app.route('/')
def index():
    return 'hello there!'

# 5월 20일부터 d-day 카운트 출력
@app.route('/dday')

def dday():
    vacation = datetime.datetime(2019, 5, 20)
    today = datetime.datetime.now()
    dday = (vacation - today).days
    # today = datetime.datetime(2019, 1, 30)
    return f'{dday}일 남았습니다.'


# variable routing
@app.route('/hi/<string:name>')
def hi(name):
    return f'안녕, {name}'

# 안녕
@app.route('/hi/<string:name>')    
def greeting(name):
    return render_template('greeting.html', html_name=name)

# 세제곱 구하기
@app.route('/cube/<int:number>')
def cube(number):
    return f'{number}의 세제곱은 {number ** 3} 입니다.'
    
@app.route('/hi/<string:name>')    
def greeting(name):
    return render_template('greeting.html', html_name=name)
    
@app.route('/movie')
def movie():
    movies = ['극한직업', '정글북', '캡틴마블', '보헤미안랩소디', '완벽한타인']
    return render_template('movie.html', movie=movies)

# 항상 마지막에 위치
if __name__ == "__main__":
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)  # c9 열어놓은 ip찾아옴
    
```



```python
<!-- greeting.html -->
<!-- 내 이름이 들어오면, 다른 사람 이름이 들어오면 -->

<!DOCTYPE HTML>
<html>
  <head>
    <title>Flask app</title>
  </head>
  <body>
    {% if html_name == "채원" %}
      <h1>안녕, {{ html_name }}아 왔니?</h1>
    {% else %}
      <h1>{{ html_name }}, 너는 누구야?</h1>
    {% endif %}
  </body>
</html>
```



```python
# movie.html

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
</head>

<body>
    <div class="container">
        <div class="row">
            {% for movie in movies %}
            <div class="card" style="width: 18rem;">
                <img src="..." class="card-img-top" alt="...">
                <div class="card-body">
                    <h5 class="card-title">{{ movie }}</h5>
                    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                    <a href="#" class="btn btn-primary">Go somewhere</a>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>


    <!-- ul 리스트에 있던 영화를 출력해주세요 for문으로 -->
    <h1>영화목록</h1>
    <ul>
        {% for movie in movies %} {{ movie }} {% endfor %}
    </ul>

    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
</body>

</html>
```

