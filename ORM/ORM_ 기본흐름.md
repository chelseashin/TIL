

2019.02.08

< ORM_기본흐름 정리 >

* 가상환경 setting
* 완전히 흐름을 숙지해야 함!
* 방향의 중요성
* 변수의 중요성(오타주의)

* app.py

```python
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, User
# model.py에서 db와 User class불러오기

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db에 app 연동
db.init_app(app)

# migrate 초기화
migrate = Migrate(app, db)

# 뷰 함수
@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

# @app.route('/users/create')  # unique한 페이지
@app.route('/users/create/') # 후방 슬래쉬 없이 엑세스 하면 슬래쉬가 있는 url로 잡아줌(거의 이 경우를 사용)
def create():
    nickname = request.args.get('nickname')
    address = request.args.get('address')
    # 앞의 nickname은 column name!
    user = User(nickname=nickname, address=address)
    db.session.add(user)
    db.session.commit()
    # url_for은 뷰 함수의 이름을 씀. 그래서 index를 씀
    return redirect(url_for('index'))

@app.route('/users/delete/<int:id>/')
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
    nickname = request.args.get('nickname')
    address = request.args.get('address')
    
    user.nickname = nickname
    user.address = address
    
    db.session.commit()
    
    return redirect(url_for('index'))
    
# 아래에 위치 - 서버 꺼지지 않도록!
if __name__ == "__main__":
    app.run(host = os.getenv('IP'), port=os.getenv('PORT'), debug = True)
```



* models.py

```python
from flask_sqlalchemy import SQLAlchemy

# sqlalchemy 초기화
db = SQLAlchemy()

# sqlalchemy datatype 6가지
# Integer / String(size) / Text / DateTime / Float / Boolean

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(20), nullable=False)
```



* index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1> INDEX</h1>
    <!-- 길 만들어 주기 -->
    <form action="/users/create/">
        <input type="text" name="nickname" required/>
        <input type="text" name="address" required/>
        <input type="submit" value="submit"/>
    </form>
        
    <h2>주소록</h2>
    <ul>
        {% for user in users %}
        <li>
            닉네임 : {{ user.nickname }} / 주소 : {{ user.address }}
            <a href="/users/delete/{{ user.id }}">[Delete]</a>
            <a href="/users/edit//{{ user.id }}">[Edit]</a>
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```



* edit.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>EDIT</h1>
     <form action="/users/update/{{user.id}}">
        <input type="text" name="nickname" value="{{ user.nickname }}" required/>
        <input type="text" name="address" value="{{ user.address }}" required/>
        <input type="submit" value="submit"/>
    </form>
</body>
</html>
```

