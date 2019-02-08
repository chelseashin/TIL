2019.02.08

< ORM을 이용한 Movie project >

1. 워크스페이스 생성
2. 파이썬 설치
3. 폴더 생성
4. 폴더에 가상환경 설정
5. 프로젝트 시작

04_crud/
​	README.md
​	app.py
​	models.py
​	db_flask.sqlite3
​	migrations/
​	templates/
​		index.html
​		edit.html
​		new.html
​		show.html
​		base.htm

* app.py - 가장 기본 실행 페이지

```python
import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Movie
# model.py에서 db와 Movie class불러오기

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db에 app 연동
db.init_app(app)

# migrate 초기화
migrate = Migrate(app, db)

# 1. index - 영화 목록
@app.route('/movies/')
def index():
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)
    
# 2. new - 새 영화를 등록할 페이지로 이동
@app.route('/movies/new/')
def new():
    return render_template('new.html')
    
# 3. create - 새 영화 등록 페이지 생성
@app.route('/movies/create/')
def create():
    movie = Movie(title = request.args.get('title'),
                title_en = request.args.get('title_en'),
                audience = request.args.get('audience'),
                open_date = request.args.get('open_date'),
                genre = request.args.get('genre'),
                watch_grade = request.args.get('watch_grade'),
                score = request.args.get('score'),
                poster_url = request.args.get('poster_url'),
                description = request.args.get('description'))
    
    db.session.add(movie)
    db.session.commit()
    
    return redirect(url_for('show', id=movie.id))
    
# 4. show - 등록 영화 조회
@app.route('/movies/<int:id>/')
def show(id):
    movie = Movie.query.get(id)
    return render_template('show.html', movie=movie)
    
# 5. edit - 영화 정보 수정
@app.route('/movies/<int:id>/edit/')
def edit(id):
    movie = Movie.query.get(id)
    return render_template('edit.html', movie=movie)

# 6. update - 영화 정보 수정
@app.route('/movies/<int:id>/update/')
def update(id):
    movie = Movie.query.get(id)
    movie.title = request.args.get('title')
    movie.title_en = request.args.get('title_en')
    movie.audience = request.args.get('audience')
    movie.open_date = request.args.get('open_date')
    movie.genre = request.args.get('genre')
    movie.watch_grade = request.args.get('watch_grade')
    movie.score = request.args.get('score')
    movie.poster_url = request.args.get('poster_url')
    movie.description = request.args.get('description')
    
    db.session.commit()
    return redirect(f"/movies/{movie.id}/")
    # return redirect(url_for('index'))
    
# 7. delete - 영화 정보 삭제
@app.route('/movies/<int:id>/delete/')
def delete(id):
    movie = Movie.query.get(id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('index'))
    
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)
```



* models.py

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 클래스 생성
class Movie(db.Model):
    __tablename__='movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    title_en = db.Column(db.String, nullable=False)
    audience = db.Column(db.Integer, nullable=False)
    open_date = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    watch_grade = db.Column(db.String, nullable=False)
    score = db.Column(db.Float, nullable=False)
    poster_url = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
```



* base.html

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <!--block 태그는 파생된 템플릿이 변경할 수 있는 항목을 정의합니다. -->
    {% block head %}
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
    <link rel="icon" type="image/png" sizes="96x96" href="/templates/favicon-96x96.png">

    <title> {% block title%} {% endblock %} - My Movie</title>
    {% endblock %}
</head>

<body>
    <div class="container ">
        {% block body %} {% endblock %}
    </div>

    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
</body>

</html>
```



* index.html

```html
{% extends "base.html" %}
<!--{% block title %} INDEX {% endblock %}-->

{% block body %}
    <h1 class="text-center">INDEX</h1>
    <a class="text-center", href="/movies/new/">[새 영화 등록]</a>
    <ul>
        {% for movie in movies %}
        <li>
            <a href="/movies/{{ movie.id }}/"> {{ movie.title }}</a> : {{ movie.score }}
        </li>
        {% endfor %}
    </ul>
{% endblock %}
```



* new.html

```html
{% extends "base.html" %}
<!--{% block title %} 영화 정보 등록 {% endblock %}-->
{% block head %}
    {{ super () }}
    <h1 class="text-center">영화 정보 등록</h1>
    <link rel="stylesheet" href="style.css" type="text/css" />
{% endblock %}

{% block body %}
    <form action="/movies/create/">
        영화명 : <input type="text" name="title"/><br>
        영화명(영문) : <input type="text" name="title_en"/><br>
        누적 관객수 : <input type="number" name="audience"/><br>
        개봉일 : <input type="date" name="open_date"/><br>
        장르 : <input type="text" name="genre"/><br>
        관람등급 : <input type="text" name="watch_grade"/><br>
        평점 : <input type="number" name="score"/><br>
        포스터 이미지 URL : <input type="text" name="poster_url"/><br>
        영화소개 : <textarea rows="4" cols="50" name ="description" ></textarea><br>
        <input type="submit" value="Submit"/>
    </form>
{% endblock %}
```



* show.html

```html
{% extends "base.html" %}
{% block head %} 
    {{ super () }}
<h1 class="text-center">등록 영화 조회</h1>
<link rel="stylesheet" href="style.css" type="text/css" />
{% endblock %}

{% block body %}
<ul>
    <li>
        영화명 : {{ movie.title }}<br>
        영화명(영문) : {{ movie.title_en }}<br>
        누적 관객수 : {{ movie.audience }}<br>
        개봉일 : {{ movie.open_date }}<br>
        장르 :{{ movie.genre }}<br>
        관람등급 : {{ movie.watch_grade }}<br>
        평점 : {{ movie.score }}<br>
        포스터 이미지 URL : {{ movie.poster_url }}<br>
        영화소개 : {{ movie.description }}<br>
        <a href="/movies/">[목록]</a>
        <a href="/movies/{{ movie.id }}/edit/">[수정]</a>
        <a href="/movies/{{ movie.id }}/delete/">[삭제]</a>
    </li>
</ul>
{% endblock %}
```



* edit.html

```html
{% extends "base.html" %}
<!--{% block title %} 영화 정보 수정 {% endblock %}-->
{% block head %}
    {{ super () }}
{% endblock %}
{% block body %}
    <h1 class="text-center">영화 정보 수정</h1>
    
    <form action="/movies/{{movie.id}}/update/">
        영화명 : <input type="text" name="title" value="{{ movie.title }}" required/><br>
        영화명(영문) : <input type="text" name="title_en" value="{{ movie.title_en }}" required/><br>
        누적 관객수 : <input type="number" name="audience" value="{{ movie.audience }}" required/><br>
        개봉일 : <input type="date" name="open_date" value="{{ movie.open_date }}" required/><br>
        장르 : <input type="text" name="genre" value="{{ movie.genre }}" required/><br>
        관람등급 : <input type="text" name="watch_grade" value="{{ movie.watch_grade }}" required/><br>
        평점 : <input type="number" name="score" value="{{ movie.score }}" required/><br>
        포스터 이미지 URL : <input type="text" name="poster_url" value="{{ movie.poster_url }}" required/><br>
        영화소개 : <textarea rows="4" cols="50" name ="description" required/>{{ movie.description }}</textarea><br>
        <input type="submit" value="Submit"/>
    </form>
{% endblock %}    

```

