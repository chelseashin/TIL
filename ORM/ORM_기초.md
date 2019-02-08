2019.02.07

< ORM >

* ORM(Object-relational mapping)을 단순하게 표현하면 객체와 관계와의 설정이라 할 수 있다. ORM에서 말하는 [객체](http://www.incodom.kr/%EA%B0%9D%EC%B2%B4)([Object](http://www.incodom.kr/Object))의 의미는 우리가 흔히 알고 있는 OOP(Object_Oriented Programming)의 그 객체를 의미한다는 것을 쉽게 유추할 수 있을 것이다. 그렇다면 과연 관계라는 것이 의미하는 것은 무엇일까? 지극히 기초적인 이야기지만 개발자가 흔히 사용하고 있는 관계형 데이터베이스를 의미한다.

* 객체형 데이터(JAVA Object)와 관계형 데이터(RDB의 테이블 ) 사이에서 개념적으로 일치하지 않는 부분을 해결하기 위하여 이 둘 사이를 Mapping하는 것을 의미한다. 객체형 데이터와 관계형 데이터의 각 속성들을 매핑할 경우, 관계형 데이터처럼 사용가능하다.

  쉽게 말해, SQL문 작성 없이 간단한 매핑설정으로 데이터 베이스의 테이블 데이터를 JAVA객체로 전달받을 수 있는 것이다. 


* 장점
  1. 객체 지향적인 코드로 인해 직관적이고 비즈니스 로직에 더 집중할 수 있도록 한다.
  2.  재사용 가능, 유지보수성이 향상
  3. DB에 대한 종속성이 줄어든다.

* 단점
  1. 오로지 ORM으로만은 거대한 서비스를 구현하기가 어렵다.
  2. 어느 정도의 속도 저하가 발생할 수 있다.



* ORM 터미널에서 설치

  ```sql
  pip install flask_sqlalchemy
  pip install flask_migrate
  ```

* app.py

  ```sql
  from flask import Flask 
  from flask_sqlalchemy import SQLAlchemy
  from flask_migrate import Migrate
  
  app = Flask(__name__)
  
  # flask app에 sqlalchemy 관련 설정
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
  app.config['SQLAlchemy_TRACK_MODIFICATIONS'] = False
  
  # app.config['SQLAlchemy_TRACK_MODIFICATIONS'] = True가 기본값 
  # sqlalchemy 데이터베이스 객체 수정 및 신호 방출 등을 추적함
  # 과도한 메모리를 사용하기 때문에 False.
  
  # sqlalchemy 초기화
  db = SQLAlchemy(app)
  
  # migrate : 실제 db에서 실행함
  # flask와 db를 인자로 받음
  migrate = Migrate(app, db)
  
  # 약속이니까 대소문자 구분 잘 하여 쓰기!
  class User(db.Model):
      __tablename__ = 'users'
      id = db.Column(db.Integer, primary_key=True)
      username = db.Column(db.String(80), unique=True, nullable=False) 
      # nullable=False 값이 비어있을 수 없다고 지정. 
      email = db.Column(db.String(120), unique=True, nullable=False)
      
      def __repr__(self):
          return f"<User '{self.username}'>"
  ```



* 터미널에서 ORM 초기 설정

  ```sql
  (flask-venv) chelseashin:~/workspace/orm $ flask db init
  (flask-venv) chelseashin:~/workspace/orm $ flask db migrate -- migration 폴더 생성됨
  (flask-venv) chelseashin:~/workspace/orm $ flask db upgrade
  ```

* orm.sql 

```sql
-- CREATE
INSERT INTO users (username, email)
VALUES ('chelsea', 'chaewonshin95@gmail.com');

user = User(username = 'chelsea',
            email = 'chaewonshin95@gmail.com')
            
-- READ
SELECT * FROM users;
users = Users.query.all()

SELECT * FROM users WHERE username="chelsea";
users = User.query.filter_by(username="chelsea").all()

SELECT * FROM users WHERE username="chelsea" LIMIT 1;
miss = User.query.filter_by(username='ssafy').first()

-- Get one by id
-- PK만 get으로 가져올 수 있음
SELECT * FROM users WHERE id=1;
user = User.query.get(1)

-- LIKE
users = User.query.filter(User.email.like('%exam%')).all()
users = User.query.limit(1).offset(2).all()  -- 세번째부터 하나 가져옴

-- UPDATE
user = User.query.get(1)
user.username = 'ssafy'
db.session.commit()
user.username

-- DELETE
user = User.query.get(1)
db.session.delete(user)
db.session.commit()
```



* ORM 터미널 설정

```sql
(flask-venv) chelseashin:~/workspace/orm $ python 
Python 3.6.7 (default, Jan 30 2019, 06:16:36) 
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from app import *
/home/ubuntu/.pyenv/versions/flask-venv/lib/python3.6/site-packages/flask_sqlalchemy/__init__.py:794: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
  'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
  
>>> user = User(username="chelsea", email="chaewonshin95@gmail.com")
>>> db.session.add(user)
>>> db.session.commit()
>>> user.username
'chelsea'
>>> user.email
'chaewonshin95@gmail.com'

>>> users = User.query.all()
>>> users
[<User 'chelsea'>]
>>> type(user)
<class 'app.User'>
>>> users = User.query.filter_by(username="chelsea").all()
>>> users = User.query.filter_by(username="chelsea").first()

-- 값이 없으면 None을 반환
>>> miss = User.query.filter_by(username='ssafy').first()
>>> type(miss)
<class 'NoneType'>

-- username 'ssafy'로 바꾸기
>>> user
<User 'chelsea'>
>>> user.username
'chelsea'
>>> user.username = 'ssafy'
>>> db.session.commit()
>>> user.username
'ssafy'

```



* app.py 객체화를 위한 분리작업 - 모두 분리시켜줘야 함!
* app.py

```sql
import os
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, User

app = Flask(__name__)

# flask app에 sqlalchemy 관련 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
app.config['SQLAlchemy_TRACK_MODIFICATIONS'] = False

# app.config['SQLAlchemy_TRACK_MODIFICATIONS'] = True가 기본값 
# sqlalchemy 데이터베이스 객체 수정 및 신호 방출 등을 추적함
# 과도한 메모리를 사용하기 때문에 False.

# sqlalchemy 초기화
# db = SQLAlchemy(app)
db.init_app(app)

# app과 db를 인자로 받음
migrate = Migrate(app, db)

@app.route('/')
# 뷰 함수
def index():
    # return url_for('index') =>>>'/'
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/users/create')
def create():
    username = request.args.get('username')
    email = request.args.get('email')
    user = User(username=username, email=email)
    # db에 넣어줘야 함
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/users/delete/<int:id>')
def delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/users/edit/<int:id>')
def edit(id):
    user = User.query.get(id)
    return render_template('edit.html', user=user)
    
@app.route('/users/update/<int:id>')
def update(id):
    user = User.query.get(id)
    username = request.args.get('username')
    email = request.args.get('email')
    
    user.username = username
    user.email = email
    db.session.commit()
    
    return redirect(url_for('index'))
    
    
# 항상 맨 아래에 위치
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)
```



* models.py

```sql
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# table 만들기
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False) 
    # nullable=False : 값이 비어있을 수 없다. 
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self):
        return f"<User '{self.username}'>"
```



* index.html - 띄워서 연결 되었는지 확인

```html
{% extends "base.html" %}
{% block title %} Index {% endblock %}
{% block head %}
<!--부모의 것을 계속해서 자식을 추가하여 가져온다는 뜻-->
    {{ super () }}
    <link rel="stylesheet" href="style.css" type="text/css" />
{% endblock %}

{% block body %}
    <form action="/users/create">
        <input type="text" name="username"/>
        <input type="email" name="email"/>
        <input type="submit" value="Submit"/>
    </form>
    
    <ul>
        {% for user in users %}
            <li>{{ user.username }} : {{ user.email }} 
                <a href="/users/delete/{{ user.id }}">[DELETE]</a>
                <a href="/users/edit/{{ user.id }}">[EDIT]</a>
            </li>
        {% endfor %}
    </ul>
{% endblock %}
```



* base.html

```sql
<!DOCTYPE html>
<html lang="en">

<head>
    <!--block 태그는 파생된 템플릿이 변경할 수 있는 항목을 정의합니다. -->
    {% block head %}
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">

    <title> {% block title%} {% endblock %} - My Webpage</title>
    {% endblock %}
</head>

<body>
    <div class="container">
        <h1>이것은 BASE의 h1 입니다.</h1>
        {% block body %} {% endblock %}
    </div>

    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
</body>

</html>
```





* Update - 수정페이지가 필요!

```html
{% extends "base.html" %}

{% block body %}
    <h1> 여기는 수정페이지 입니다.</h1>
    <form action = "/users/update/{{ user.id }}">
        <input type="text" value="{{user.username}}" name="username"/>
        <input type="email" value="{{user.email}}" name="email"/>
        <input type="submit" value="Submit"/>
    </form>
    
{% endblock %}
```
