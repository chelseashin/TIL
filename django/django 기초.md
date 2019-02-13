2019.02.13

< Django start  >

#### Django 가상환경 만들기

```python
# install pyenv
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
source ~/.bashrc
pyenv install 3.6.7
pyenv global 3.6.7
pyenv rehash


# install pyenv-virtualenv
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
source ~/.bashrc
```



#### git user 설정

```python
# git
사용자 정보 설정
메일주소는 반드시 GitHub 계정과 동일해야하고 유저네임도 맞춰주는 것이 좋다.

--global 옵션으로 설정하는 것은 딱 한 번만 하면 된다. 해당 시스템에서 해당 사용자가 사용할 때는 이 정보를 사용한다. (만약 프로젝트마다 다른 이름과 이메일 주소를 사용하고 싶으면 --global 옵션을 빼고 명령을 실행한다.)

$ git config --global user.name 'example'
$ git config --global user.email "example@gmail.com"

# 정보 설정 확인
$ git config --global --list
```



#### Django 시작

```python
# 버전 확인
chelseashin:~/workspace $ python -V
Python 3.6.7

chelseashin:~/workspace $ pyenv virtualenv 3.6.7 django-venv

# 가상환경 설정할 폴더로 이동
chelseashin:~/workspace $ pyenv virtualenvs
chelseashin:~/workspace $ mkdir PROJECT01
chelseashin:~/workspace $ cd PROJECT01/
    
# 가상환경 활성화. 켜기!
chelseashin:~/workspace/PROJECT01 $ pyenv local django-venv
# 장고 설치
(django-venv) chelseashin:~/workspace/PROJECT01 $ pip install django
# 이제 장고 시작~

# 중간에 폴더 안 생기도록 방지하기 위해 마지막에 '.' 붙여주기
(django-venv) chelseashin:~/workspace/PROJECT01 $ django-admin startproject django_intro .
(django-venv) chelseashin:~/workspace/PROJECT01 $ ls
django_intro/  manage.py*
(django-venv) chelseashin:~/workspace/PROJECT01 $ python manage.py runserver $IP:$PORT
# 서버 열기 - 

```



* setting.py 수정

```python
ALLOWED_HOSTS = ['django-intro-chelseashin.c9users.io']

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
```



* gitignore 만들기

```python
(django-venv) chelseashin:~/workspace/PROJECT01 $ touch .gitignore
(django-venv) chelseashin:~/workspace/PROJECT01 $ ls -al
```



* tree 구조 확인

```python
(django-venv) chelseashin:~/workspace/PROJECT01 $ tree
.
├── db.sqlite3    # 장고 기본파일
├── django_intro
│   ├── __init__.py # 
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   ├── settings.cpython-36.pyc
│   │   ├── urls.cpython-36.pyc
│   │   └── wsgi.cpython-36.pyc
│   ├── settings.py    # 모든 환경구조 설정하는 공간
│   ├── urls.py    # 장고를 url로 설정. 목차 개념. 사이트의 연결, 어플리케이션의 일부를 할당 등의 역할
│   └── wsgi.py
└── manage.py

2 directories, 10 files
```



* urls.py 확인

```python
# 건들 일 없음!
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

# 서버 주소에서 /admin 을 붙여 확인
http://django-intro-chelseashin.c9users.io:8080/admin/
```



### terminal에 작성

```python
(django-venv) chelseashin:~/workspace/PROJECT01 $ ls
db.sqlite3  django_intro/  manage.py*
# app 시작하는 폴더를 home으로 하자는 명령어
(django-venv) chelseashin:~/workspace/PROJECT01 $ python manage.py startapp home
# app 자체가 MTV 구조를 가지고 있는 경우

# home 안의 구조 보기
(django-venv) chelseashin:~/workspace/PROJECT01 $ cd home
(django-venv) chelseashin:~/workspace/PROJECT01/home $ tree .
.
├── __init__.py
├── admin.py   # 관리자용 페이지 커스터마이징하는 곳
├── apps.py    #  앱의 정보가 있는 곳. 우리는 수정할 일이 없다!
├── migrations
│   └── __init__.py
├── models.py  # 앱에서 사용하는 Model을 정의하는 곳
├── tests.py   # 테스트 코드를 작성하는 곳
└── views.py   # 뷰들이 정의되는 곳. 사용자에게 어떤 데이터를 보여줄지 구현되는 곳
# 위 3개가 MTV
1 directory, 7 files
```



* settings.py 수정

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # home 앱 등록하고 저장!!!!!!! 꼭 해야하는 절차. 마지막 쉼표 꼭 써
    'home.apps.HomeConfig',
]
```



* apps.py에서 확인

```python
from django.apps import AppConfig


class HomeConfig(AppConfig):
    name = 'home'
```



* urls.py에서 추가

```python
from django.contrib import admin
from django.urls import path
# home의 views와 연결
from home import views

urlpatterns = [
    # 항상 여기에 작성! 약속!
    # home에 있는 views의 index 함수를 사용
    path('home/index/', views.index, name = 'index'),
    path('admin/', admin.site.urls),
]

# 저장 후 서버 켜서 확인
http://django-intro-chelseashin.c9users.io:8080/home/index/
        
`Welcome to Django!`뜬 거 확인~~
```



* views.py

```python
from django.shortcuts import render, HttpResponse
# from pprint import pprint

def index(request):
    # print(request)
    # print(type(request))
    # pprint(request.META)
    return HttpResponse('Welcome to Django!')

```



url.py의 역할 : @app.route() 

views.py의 역할 : def index()  - 모든 함수 정의 여기에서 함!



* 저녁 메뉴 정하는 url 리턴

```python
### view.py

from django.shortcuts import render, HttpResponse
import random

def dinner(request):
    menu = '치킨', '삼겹살', '비빔밥', '파스타', '피자'
    return HttpResponse(random.choice(menu))


### urls.py
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('home/dinner/', views.dinner, name= 'dinner'),
    path('home/index/', views.index, name = 'index'),
    path('admin/', admin.site.urls),
]
```



## 작성 순서!

1. 처리할 views(controller)
2.  요청 urls
3. 결과 보여줄 templates(html..)



## git push

```python
git remote add origin https://github.com/chelseashin/django_intro.git
git push -u origin master
```



* hello / cube

```python
# views.py

def hello(request, name):
    return render(request, 'hello.html', {'name': name})
    
def cube(request, number):
    # 연산작업은 주로 views에서 함
    result = number ** 3
    return render(request, 'cube.html', {'number': number, 'result': result})
# html로 넘겨줄 값
    
# urls.py - 경로 설정
 	path('home/cube/<int:number>/', views.cube, name= 'cube'),
    path('home/hello/<name>/', views.hello, name= 'hello'),
```



```html
# hello.html
<h1> {{name}}아, 안녕?</h1>

# cube.html
<h1>{{number}}의 세제곱은 {{result}}입니다!</h1>
```



* ping/pong

```python
# views.py

def ping(request):
    return render(request, 'ping.html')
    
def pong(request):
    print(request.GET)
    data = request.GET.get('data')
    return render(request, 'pong.html',{'data' : data})

# urls.py
# 주소 추가
	path('home/pong/', views.pong, name='pong'),
    path('home/ping/', views.ping, name='ping'),

```



```html
# ping.html

<body>
    <form action='/home/pong/'>
        <input type="text" name ="data">
        <input type="submit" value ="Submit">
    </form>
</body>


# pong.html
<h1>퐁~~~~~ {{ data }}</h1>
```



* user_new / user_create - nickname, password 추가

```python
# views.py
def user_new(request):
    return render(request, 'user_new.html')
    
def user_create(request):
    nickname = request.POST.get('nickname')
    pwd = request.POST.get('pwd')
    return render(request, 'user_create.html', {'nickname' : nickname, 'pwd' : pwd})

# urls.py - 주소 추가
urlpatterns = [
    path('home/user_create/', views.user_create, name='user_create'),
    path('home/user_new/', views.user_new, name='user_new'),
]
```



```html
# user_new.html
<form action='/home/user_create/' method='POST'>
        <!--사이트 위조 방지-->
        {% csrf_token %} 
        <input type="text" name ="nickname">
        <input type="password" name ="pwd">
        <input type="submit" value ="Submit">
</form>

# user_create.html
<h1>nickname : {{ nickname }}</h1>
<h1>password : {{ pwd }}</h1>
```



* html의 base가 되는 base.html 생성

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>{% block title %}{% endblock %}</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
</head>

<body>
    <h1>장고 연습</h1>
    
    <hr>
    
    <div class="container">
        {% block body %}{% endblock %}
    </div>
    
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
</body>

</html>

```



* base.html을 만들었기 때문에 이를 바탕으로
*  user_new.html와 user_create.html를 수정해보자.

```html
# user_new.html

{% extends 'base.html' %}
{% block title %}user_new{% endblock %}
{% block body %}
    <form action='/home/user_create/' method='POST'>
        <!--사이트 위조 방지-->
        {% csrf_token %} 
        <input type="text" name ="nickname">
        <input type="password" name ="pwd">
        <input type="submit" value ="Submit">
    </form>
{% endblock %}

# user_create.html
{% extends 'base.html' %}
{% block title %}user_create{% endblock %}
{% block body %}
    <h1>nickname : {{ nickname }}</h1>
    <h1>password : {{ pwd }}</h1>
{% endblock %}
```