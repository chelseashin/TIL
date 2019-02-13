2019.02.13

< Django 기초  >

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
Looking in links: /tmp/tmpot1_tx_4
Requirement already satisfied: setuptools in /home/ubuntu/.pyenv/versions/3.6.7/envs/django-venv/lib/python3.6/site-packages (39.0.1)
Requirement already satisfied: pip in /home/ubuntu/.pyenv/versions/3.6.7/envs/django-venv/lib/python3.6/site-packages (10.0.1)
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
├── admin.py   # 관리자형 파일을 customize
├── apps.py    # app 정보
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
└── views.py
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
    result = number ** 3
    return render(request, 'cube.html', {'number': number, 'result': result})
    
    
# urls.py
# 주소 추가
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
    <form action='/home/pong'>
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



