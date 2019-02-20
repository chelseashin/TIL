19.02.20

< Django 

* 프로젝트 시작 명령어

```python
(django-venv) chelseashin:~/workspace $ cd PROJECT02
(django-venv) chelseashin:~/workspace/PROJECT02 $ c9 open .
(django-venv) chelseashin:~/workspace/PROJECT02 $ c9 open .gitignore
(django-venv) chelseashin:~/workspace/PROJECT02 $ ls -al
total 20
drwxr-xr-x 3 ubuntu ubuntu 4096 Feb 20 00:26 ./
drwxrwxr-x 6 ubuntu ubuntu 4096 Feb 20 00:21 ../
    # gitignore 생성
-rw-r--r-- 1 ubuntu ubuntu 1786 Feb 20 00:26 .gitignore
    # gitignore 홈페이지에서 'django'검색하여 전문 복사후 .gitignore 에 붙여넣기
drwxr-xr-x 3 ubuntu ubuntu 4096 Feb 20 00:23 crud/
-rw-r--r-- 1 ubuntu ubuntu    0 Feb 20 00:22 db.sqlite3
-rwxr-xr-x 1 ubuntu ubuntu  536 Feb 20 00:21 manage.py*
(django-venv) chelseashin:~/workspace/PROJECT02 $ cd ..
    # 잘못된 곳에 가상환경 설치했을 때 
(django-venv) chelseashin:~/workspace $ ls -al
total 32
drwxrwxr-x  6 ubuntu ubuntu 4096 Feb 20 00:21 ./
drwxr-xr-x 20 ubuntu ubuntu 4096 Feb 14 01:36 ../
drwxr-xr-x  3 ubuntu ubuntu 4096 Feb 13 00:29 .c9/
-rw-r--r--  1 ubuntu ubuntu   12 Feb 20 00:19 .python-version
drwxr-xr-x  6 ubuntu ubuntu 4096 Feb 14 01:45 PROJECT01/
drwxr-xr-x  3 ubuntu ubuntu 4096 Feb 20 00:26 PROJECT02/
drwxr-xr-x  4 ubuntu ubuntu 4096 Feb 13 06:43 homeworkshop/
-rwxr-xr-x  1 ubuntu ubuntu  536 Feb 20 00:19 manage.py*
    # 가상환경 제거
(django-venv) chelseashin:~/workspace $ rm -rf .python-version 
chelseashin:~/workspace $ cd PROJECT02/
    # 폴더 이동 후 가상환경 만들기
chelseashin:~/workspace/PROJECT02 $ pyenv local django-venv 
    # 앱 생성
(django-venv) chelseashin:~/workspace/PROJECT02 $ python manage.py startapp boards
```



* settings.py에 새로 만든 앱 INSTALLED_APPS 상단에 등록

```python
INSTALLED_APPS = [
    'boards.apps.BoardsConfig', 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```



* boards 앱의 Models.py(대소문자 주의)

```python
from django.db import models

# Create your models here.
class Board(models.Model):    
    # 각 모델은 django.db.models.Model 클래스의 서브 클래스에 표현
    title = models.CharField(max_length=10)  
    # 데이터타입 속성 : max_length는 Character field의 필수 인자. 
    content = models.TextField()    
    created_at = models.DateTimeField(auto_now_add=True) 
    # 대소문자 주의, settings.py로 이동하여 하단에 USE_TZ = False로 수정
    # auto_now_add=True : 장고 모델이 최초 저장시에만 현재 날짜를 적용
    updated_at = models.DateTimeField(auto_now=True)
    # auto_now=True : 장고 모델이 save될 때마다 현재 날짜를 적용. 수정될 때마다 작성시간이 바뀜
```



* Terminal 명령어 

```python
# 'boards'에 migrations 생성 - 앱에서 설계도 역할
(django-venv) chelseashin:~/workspace/PROJECT02 $ python manage.py makemigrations boards
Migrations for 'boards':
  boards/migrations/0001_initial.py
    - Create model Board
    
# DB에 아직 들어가지 않은 설계도 : 0001_initial.py

# boards앱의 0001_initial.py 확인 - db형식으로 되어있음
(django-venv) chelseashin:~/workspace/PROJECT02 $ python manage.py sqlmigrate boards 0001
BEGIN;
--
-- Create model Board
--
CREATE TABLE "boards_board" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(10) NOT NULL, "content" text NOT NULL, "created_at" datetime NOT NULL);
COMMIT;

# 새로운 migrations 생성
(django-venv) chelseashin:~/workspace/PROJECT02 $ python manage.py makemigrations boards
Migrations for 'boards':
  boards/migrations/0002_board_updated_at.py
    - Add field updated_at to board
    
# migration 파일들을 DB에 넣기! 이렇게 해야 모델 만들어짐
(django-venv) chelseashin:~/workspace/PROJECT02 $ python manage.py migrate
    
# 2번 파일 들어가기
(django-venv) chelseashin:~/workspace/PROJECT02 $ python manage.py sqlmigrate boards 0002
BEGIN;
--
-- Add field updated_at to board
--
ALTER TABLE "boards_board" RENAME TO "boards_board__old";
CREATE TABLE "boards_board" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "updated_at" datetime NOT NULL, "title" varchar(10) NOT NULL, "content" text NOT NULL, "created_at" datetime NOT NULL);
INSERT INTO "boards_board" ("id", "title", "content", "created_at", "updated_at") SELECT "id", "title", "content", "created_at", '2019-02-20 10:12:22.696799' FROM "boards_board__old";
DROP TABLE "boards_board__old";
COMMIT;
```



* database 확인하기

```python
(django-venv) chelseashin:~/workspace/PROJECT02 $ sqlite3 db.sqlite3
SQLite version 3.8.2 2013-12-06 14:53:30
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> .tables
auth_group                  boards_board              
auth_group_permissions      django_admin_log          
auth_permission             django_content_type       
auth_user                   django_migrations         
auth_user_groups            django_session            
auth_user_user_permissions

# 테이블의 스키마 확인
sqlite> .schema boards_board
CREATE TABLE "boards_board" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(10) NOT NULL, "content" text NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL);

# sql에서 나가기
sqlite> .exit
```



* shell로 django orm 문법 써보기

```python
(django-venv) chelseashin:~/workspace/PROJECT02 $ python manage.py shell
Python 3.6.7 (default, Feb 13 2019, 00:39:46) 
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from boards.models import Board         
# sql에서 * 역할
>>> Board.objects.all()
<QuerySet []>
>>> board = Board()
>>> board.title = 'first'
>>> board.content = 'django!'
# 저장
>>> board.save()
>>> Board.objects.all()
<QuerySet [<Board: Board object (1)>]>
# db 나가기
>>> exit()
```



* models.py에 메소드 만들기

```python
def __str__(self):
        return f"{self.id}: {self.title}"
    
# self.id : 1 2 3 ...
# self.title : 제목 순서대로 나타냄
```



*  shell 에서 확인

``` python
(django-venv) chelseashin:~/workspace/PROJECT02 $ python manage.py shell
Python 3.6.7 (default, Feb 13 2019, 00:39:46) 
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from boards.models import Board
>>> Board.objects.all()
# first로 바뀐 거 확인
<QuerySet [<Board: 1: first>]>
>>> exit()
```



* terminal 에서 django-extension 설치

```python
(django-venv) chelseashin:~/workspace/PROJECT02 $ pip install django-extensions
```



* settings.py에 앱 등록

```python
INSTALLED_APPS = [
    'boards.apps.BoardsConfig', 
    'django_extensions',
    
    # 이렇게 해야 확장 프로그램 확인
```



* terminal

```python
(django-venv) chelseashin:~/workspace/PROJECT02 $ python manage.py shell_plus
    # 두 번째 글 작성
>>> board = Board(title="seconds", content="django!")
>>> board.save()
	# 저장된 객체 확인
>>> Board.objects.all()
<QuerySet [<Board: 1: first>, <Board: 2: seconds>]>
	# 세 번째 객체 생성
>>> Board.objects.create(title="third", content="django!"
    # 네 번째 객체 생성
>>> board = Board()
>>> board.title = 'forth' 
>>> board.content = 'django!!!!'
>>> board.id
>>> board.created_at
    # 저장
>>> board.save()
    # id 확인
>>> board.id
4
    # 생성시간 확인
>>> board.created_at
datetime.datetime(2019, 2, 20, 10, 35, 16, 51544)

# 객체 생성
>>> board = Board()
>>> board.title =  'lookhowtheyshineforyou'
# 비우기 
>>> board.full_clean()
                         
# 모든 객체 확인
>>> Board.objects.all()
<QuerySet [<Board: 1: first>, <Board: 2: seconds>, <Board: 3: third>, <Board: 4: forth>]>
>>> Board.objects.filter(title='first').all()
<QuerySet [<Board: 1: first>]>
>>> Board.objects.filter(title='first').first()
<Board: 1: first>
>>> Board.objects.filter(title='missing').first()                                       

# pk가 1인 것 조회
>>> board = Board.objects.get(pk=1)
>>> board
<Board: 1: first>
>>> board = Board.objects.filter(id=1)
>>> board
<QuerySet [<Board: 1: first>]>
# 'fi'가 포함된 모든 객체 보기
>>> boards = Board.objects.filter(title__contains='fi').all()
>>> boards
<QuerySet [<Board: 1: first>]>
# 'fi'로 시작하는 ~
>>> boards = Board.objects.filter(title__startswith='fi')
>>> boards
<QuerySet [<Board: 1: first>]>
# '!'로 끝나는 ~
>>> boards = Board.objects.filter(content__endswith='!')
>>> boards
<QuerySet [<Board: 1: first>, <Board: 2: seconds>, <Board: 3: third>, <Board: 4: forth>]>

>>> board = Board.objects.get(pk=1)
get : 값이 중복되거나 없을 때 테이터를 가져오기 수월한 메소드. 키 하나만 가져오기에 좋음
    # id는 항상 filter 말고 .get으로 가져와야 함. 리스트 형식으로!
    
    
# 정렬 
>>> boards = Board.objects.order_by('-title').all()
>>> boards
<QuerySet [<Board: 3: third>, <Board: 2: seconds>, <Board: 4: forth>, <Board: 1: first>]>

# 1번 글 바꾸기
>>> board = Board.objects.get(pk=1)
>>> board.title='hello'
>>> board.save()
>>> board.title
'hello'
>>> board.delete()
(1, {'boards.Board': 1})
# 나가기
>>> exit()
```





## PROJECT02

* boards에 templates폴더 만들고 그 안에 boards폴더 또 만들기
* view.py에서 함수 만들기

```python
# 모듈 import 순서
# 1. 파이썬 표준 라이브러리 ex)os, random ...
# 2. core django : 장고 프레임워크에 내장되어 있는 것
# 3. 3rd party library : pip로 설치한 것들. django-extension
# 4. 장고 프로젝트 app

from django.shortcuts import render, redirect
from .models import Board    # 3rd party library - 명시적 상대 표현

# Create your views here.
def index(request):
# READ
    # boards = Board.objects.all()[::-1]   # 원래 결과를 파이썬이 내림차순으로 변경
    boards = Board.objects.order_by('-id')  # db가 애초에 정렬 바꿔서 보내주는 것
    return render(request, 'boards/index.html', {'boards': boards})
    
def new(request):
    return render(request, 'boards/new.html')

# CREATE
def create(request):
    # 서버의 상태나 값을 바꾸기 위해 사용. 
    # 글 작성 시 글쓰기를 하면 글의 내용이 DB의 값이 변경되게 하는 경우 사용.
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    # 저장
    board = Board(title=title, content=content) # 뒤의 title은 바로 위에 request 받은 것.
    board.save()
    # 위의 두 줄과 같음
    # Board.objects.create(title=title, content=content)
    
    # render는 html을 띄워주기만 함. (render의 한계)
    # 처음에 글이 보이지 않았던 이유는 보여지는 페이지 자체를 index이지만 index의 url로는 
    # 돌아가지 못했기 때문이다. 즉 단순히 html문서만 보여준 것이다.
    # create는 model에 record를 생성해! 라는 요청이기 때문에, 단순히 페이지를 달라고 하는 
    # GET 방식 보다는 POST가 의미상 더 적절하다.
    # (그리고 모델과 관련된 데이터이기 때문에, url에 직접 보여지는 것은 좋지 않다.)
    
    # 그래서 render보다는 redirect를 사용함!
    # return render(request, 'boards/index.html')
    return redirect('/boards/') # 직접 url로 보내줌

```



* urls.py에서 입구 변경

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('boards/', include('boards.urls')), # url입구 변경. boards에 urls.py 만들기
    path('admin/', admin.site.urls),
]
```



* templates 안의 boards의 urls.py에 경로에는 그대로 작성하면 됨!

```python
from django.urls import path
# views.py에서 만든 함수를 씀!
from . import views

urlpatterns = [
    path('create/', views.create, name='create'),
    path('new/', views.new, name='new'),
    path('', views.index, name = 'index'),
    ]
```



* index.html

```python
{% extends 'boards/base.html' %}
{% block body %}
    <h1>Board</h1>
    <a href="/boards/new/">글 작성하기</a>
    <hr>
    {% for board in boards %}
        <p>{{ board.id }}</p>
        <p>{{ board.title }}</p>
        {{ board.created_at | timesince }} 전
        <hr>
    {% endfor %}
    
{% endblock %}
```



* new.html

```python
{% extends 'boards/base.html' %}
{% block body %}
    <h1>New</h1>
    <!--POST방식-->
    <form action='/boards/create/' method="POST">
    <!--자기가 쓴 글을 알아차림. 새로고침하더라도 데이터가 남음-->
        {% csrf_token %}
        <label for="title">TITLE</label>
        <input type="text" name="title"/><br>
        <label for="content">CONTENT</label>
        <textarea name="content" id="content"></textarea><br>
        <input type="submit" name="submit"/>
    </form>
    <a href="/boards/">BACK</a>
{% endblock %}
```



* 새로운 html 파일은 boards 안의 templates 안의 boards에 작성
* html의 상단에 {% extends 'boards/base.html' %} 작성 - base.html 형식 상속



* admin.py - admin관리가 있다는  django의 큰 장점

```python
from django.contrib import admin
from .models import Board

# Register your models here.
# 클래스 등록
class BoardAdmin(admin.ModelAdmin):
    # 리스트 보기
    list_display = ('title', 'content', 'created_at', 'updated_at',)
admin.site.register(Board, BoardAdmin)
```

