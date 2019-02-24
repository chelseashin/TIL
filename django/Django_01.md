## Django_01

> **Django: the Web framework for perfectionists with deadlines.**

**Content**

[0. 준비 사항](https://github.com/djpy2/Django/blob/master/Django_01.md#0-%EC%A4%80%EB%B9%84-%EC%82%AC%ED%95%AD)

[1. Django start](https://github.com/djpy2/Django/blob/master/Django_01.md#1-django-start)

[2. MTV](https://github.com/djpy2/Django/blob/master/Django_01.md#2-mtv)

[3. views-urls](https://github.com/djpy2/Django/blob/master/Django_01.md#3-views-urls)

[4. Template](https://github.com/djpy2/Django/blob/master/Django_01.md#4-template)

[5. Form](https://github.com/djpy2/Django/blob/master/Django_01.md#5-form)

[6. Template Inheritance](https://github.com/djpy2/Django/blob/master/Django_01.md#6-template-inheritance)



### 0. 준비 사항

1. pyenv / python / pyenv-virtualenv 설치 및 설정

   - python 3.6.7
   - git
   - django 2.1.x

2. 가상환경 생성

```python
# 가상환경 이름 : django-venv
$ pyenv virtual 3.6.7 django-venv
```



1. 프로젝트 폴더 생성 및 이동

```python
$ mkdir PROJECT01
$ cd PROJECT01
```



1. local 가상환경 및 활성화

```python
$ pyenv local django-venv

# 가상환경 활성화
(django-venv) $
```



------

### 1. Django start

#### 1.1 django project

1. 프로젝트 생성

> 가상환경이 활성화 된 현제 폴더 안에 프로젝트를 생성, 명령어 마지막 `.` 주의
>
> project를 생성할 때, python이나 Django에서 이미 사용중인 이름은 피해야 함.
>
> `-`도 사용할 수 없다. 
>
> (ex. django, test, class, django-test, ...)

* 프로젝트 이름 : django_intro

```python
$ django-admin startproject django_intro .
```



2. 서버 실행

```python
$ python manage.py runserver $IP:$PORT
```

>c9에서는 Invalid HTTP_HOST header error가 발생
>
>* `settings.py`에서 `ALLOWED_HOSTS `와일드 카드 설정.
>
>```python
>ALLOWED_HOSTS = ['*']
># 또는
>ALLOWED_HOSTS = ['example-username.c9users.io']
># https://, :8080 를 제외한 url
>```
>
>* 서버실행 후 로켓 확인



3. gitignore 설정

```python
$ touch .gitignore
```

* <https://www.gitignore.io/> 에서 django 를 선택해서 받은 코드를 `.gitingnore` 파일에 입력.



4. TIME_ZONE, LANGUAGE_CODE 설정

* `settings.py`

  ```python
  LANGUAGE_CODE = 'ko-kr'
  TIME_ZONE = 'Asia/Seoul'
  ```


5. 서버 재실행 및 한글화 확인

> **상황에 따른 설정**
>
> 공식문서에 따르면, 단일 프로젝트에서는 `django-admin` 보다는 `manage.py`를 사용하는 것이 편할 것이라고 이야기한다. 기본적으로 후자는 프로젝트 경로를 시스템 path에 추가하며, settings.py 설정된 내용을 `DJANGO_SETTINGS_MODULE` 환경변수에 넣어서 활용한다.
>
> 다만, 나중에 프로젝트 및 app 단위별로 setting이 나뉘게 된다면 이 경우에는 `django-admin` 명령어에 CLI 옵션 `--settings` 를 통해 지정하여 실행할 수 있는 장점이 있다.



6. 프로젝트 구조

   ```python
   PROJECT01/
       manage.py
       django_intro/
           __init__.py
           settings.py
           urls.py
           wsgi.py
   	db.sqlite3
   ```

* `PROJECT01/`: 디렉토리 바깥의 디렉토리는 단순히 프로젝트를 담는 공간.

  ​			이 이름은 django와 아무 상관 없으므로 원하는 이름으로 변경

* `manage.py` : Django프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인의 유틸리티

* `django_intro/` : 디렉토리 내부엥는 project를 위한 실제 Python패키지들이 저장됨. 이 디렉토리 내의 이름을 활용하여 (`django_intro.urls` 와 같은 식으로) project 어디서나 Python 패키지들을 import 할 수 있다.

* `__init__.py` : Python으로 하여금 이 디렉토리를 패키지 처럼 다루라고 알려주는 용도의 단순한 빈 파일

* `settings.py` : 현재 Django project의 모든 환경/구성을 저장. 

* `urls.py` : 현재 Django project의 URL선언을 저장. Django로 작성된 사이트의 "목차". 사이트의 url과 views의 연결을 지정. 모든 url 매핑 코드가 포함될 수 있지만, 특정한 어플리케이션에 일부를 할당해 주는 것이 일반적

* `wsgi.py` : 현재 project를 서비스 하기 위한 WSGI 호환 웹 서버의 진입점.
  * WSGI(Web server gateway interface) : python 웹 프레임워크에서 사용하는 웹서버 규칙



#### 1.2  django application 

1. Application 만들기 

   * 앱 이름 : home

   ```python
   $ python manage.py startapp home
   ```


2. Application 구조

```python
home/
	__init__.py
	admin.py
	apps.py
	models.py
	tests.py
	views.py
	migrations/
		__init__.py
```

* `admin.py` : 관리자용 페이지 커스터마이징 장소.
* `apps.py`: 앱의 정보가 잇는 곳.
* `models.py` : 앱에서 사용하는 model을 정의하는 곳
* `tests.py` : 테스트 코드를 작성하는 곳
* `views.py` : view들이 정의되는 곳. 사용자에게 어떤 데이터를 보여줄지 구현하는 곳.



3. Application 등록

   > * 생성한 app을 사용하려면 프로젝트에 app을 만들었다고 알려주어야 사용 가능하다.
   > * `home > apps.py > class HomeConfig()` 구조이기 때문에 `home.apps.HomeConfig`로 작성한다. 

   * `settings.py`에 작성

   ```python
   INSTALLED_APPS = [
       'home.apps.HomeConfig',
   ]
   # 항상 마지막에 `,`를 작성해줘야 함.
   ```



----

------

### 2. MTV

- 장고를 제외하면 일반적으로 MVC 패턴으로 사용된다.

  * Model : 어플리케이션의 핵심 로직의 동작을 수행한다. (Database)
  * Template(View) : 어떻게 데이터가 보여질지를 수행한다.(Interface)

  * View(Controller) : 어떤 데이터를 보여줄지를 구현한다.(Logic)

- .py 3대장

  * `models.py` : 데이터베이스 관리
  * `views.py` : 페이지 관리(페이지 하나 당, 하나의 함수)

  * `urls.py` : 주소(url) 관리

  > flask에서 app.py한 곳에서 했던 것을, django는 모두 나눠서 한다.

----

### 3. views-urls

> 우리는 앞으로
>
> 1. views.py
> 2. urls.py
> 3. templates
>
> 순으로 코드를 작성할 것이다.

![img_01](https://github.com/djpy2/Django/raw/master/images/img_01.png)



1. views 설정(`home/views.py`)

   ```python
   from django.shortcuts import render, HttpResponse
   
   # Create your views here.
   def index(request):
       return HttpsResponse("hello, django!")
   ```

   > 여기서 우리가 접속해서 볼 페이지를 작성한다.

2. urls 설정(`django_intro/urls.py`)

   ```python
   from django.contrib import admin
   from django.urls import path
   from home import views
   
   urlpatterns = [
       path('home/index/', views.index, name='index'),
       path('admin/', admin.site.urls),
   ]
   ```

   * 장고 서버로 요청(request)가 들어오면, 이 요청이 어디로 가야하는지 인식하고 관련된 함수(view)로 넘겨준다. 

   ```python
   def index(request):
       return HttpResponse('welcome to django!')
   ```

>path() 함수
>
>* `path()`함수에는 2개의 필수 인수인 `route` 와 `view`, 2개의 선택 가능한 인수로 `kwargs` 와 `name` 까지 모두 4개의 인수가 전달된다. (`kwargs` 는 다루지 않는다.)
>* path(route, view, name)
>
>HttpResponse
>
>* HttpResponse(content="")
>* Content 로 넘겨줄 수 있는 것은 iteraror 혹은 string 만 가능하다.
>  - iterator 는 join 해서 string 으로 만들어서 넘겨주고, int 는 string 으로 형변환해서 넘겨준다.
>
>**나중에 url을 나누게 된다면, 직접 app에 urls.py를 만들고 아래처럼 구조를 만든다!**
>
>```python
># app urls.py
>
>from django.urls import path
>from . import views
>
># 끝에 쉼표 꼭 써주기
>urlpattens = [
>    path('index/', views.index, name="index"),
>]
>```
>
>```python
># 프로젝트 urls.py
>from django.contrib import admin
>from django.urls import include, path
>
># 입구 바꿔주기. home의 urls를 바라보도록!
>urlpatterns = [
>    path('home/', include('home.urls')),
>    path('admin/', admin.site.urls),
>]
>```



3. 첫 메세지 출력 확인하기

```python
$ python manage.py runserver $IP:$PORT
```



----



### 4. Template

> Django 에서 사용되는 Template 은 DTL(Django Template Language)이다.
>
> jinja2 와 문법이 유사하다.

#### 4.1 Template Variable

1. views 설정

   ```python
   import random
   
   def dinner(request):
       menus = ['pizza', 'bob', 'chicken', 'sushi']
       pick = random.choice(menus)
      	return render(request, 'dinner.html', {'menus':menus, 'pick':pick})
   ```

   > render()
   >
   > *  render(request, template_name, {context})
   >   * 필수 인수 : request, template_name
   >   * 선택 인수 : context (**DTL 에서 사용될 변수를 딕셔너리**로 넘긴다.)



2. urls 설정

   ```python
   urlpatterns = [
       path('home/dinner/', views.dinner, name="dinner"),
   ]
   ```


3. templates 설정

   * dinner.html 작성

   ```python
   {% for menu in menus%}
   	<p>{{ menu }}</p>
   {% endfor %}
   <hr>
   {% if pick == 'chicken' %}
   	<p> 아웃닭 !!!! </p>
   {% else %}
   	<p>{{pick}}</p>
   {% endif %}
   ```


#### 4.2 Variable Routing

![img_02](https://github.com/djpy2/Django/raw/master/images/img_02.png)



1. views.py

   ```python
   def hello(request):
       return render(request, 'hello.html', {'name':name})
   ```

2. urls.py

   ```python
   path('home/hello/<name>', views.hello, name="name"),
   ```

3. templates > hello.html

   ```html
   <h1>
       {{name}}, 아 안녕!
   </h1>
   ```


**넘어 오는 숫자를 3제곱 리턴하는 실습**

1. views.py

   ```python
   def cube(request, num):
       nums = num ** 3
       return render(request, 'cube.html', {'num':num, 'nums':nums})
   ```

2. urls.py

   ```python
   path('home/<int:num>/', views.cube, name='cube'),
   ```

3. templates > cube.html

   ```html
   <h1>
       {{num}}의 세제곱은 {{nums}} 입니다!
   </h1>
   ```


----

### 5. Form

#### 5.1 GET

1. ping

   * views 설정

   ```python
   def ping(request):
       return render(request, 'ping.html')
   ```

   * urls 설정

   ```python
   path('ping/', views.ping, name='ping'),
   ```

   * templates 설정

   ```html
   <form action='home/pong/'>
       <input type='text' name='data'/>
       <input type='submit' value='Submit'/>
   </form>
   ```




2. pong

   * views 설정

   ```python
   def pong(request):
       data = request.GET.get('data')
       return render(request, 'pong.html', {'data':data})
   ```

   * urls 설정

   ```python
   path('home/pong/', views.pong, name='pong'),
   ```

   * templates 설정

   ```html
   <h1>
       퐁 ~~~~ {{data}}
   </h1>
   ```


#### 5.2 POST

1. user_new

   1. views 설정

      ```python
      def user_new(request):
          return render(request, 'user_new.html')
      ```

   2. urls 설정

      ```python
      path('home/user_new/', views.user_new, name='new'),
      ```

   3. template 설정

      > - `{% csrf_token %}` : 사이트간 위조 방지
      > - post 는 url 끝에 슬래쉬(`/`) 필수

      ```python
      <form action='/home/user_create/' method='POST'> 
          {% csrf_token %}
          <input type="text" name="username"/>
          <input type="password" name="pwd"/>
          <input type="submit" value="Submit"/>
      </form>
      ```



2. user_create
   1. view 설정

   ```python
   def user_create(request):
       # print(request.POST)
       username = request.POST.get('username')
       pwd = request.POST.get('pwd')
       return render(request, 'user_create.html', {'username': username, 'pwd': pwd})
   ```

   2. urls 설정

   ```python
   path('home/user_create/', views.user_create, name='create'),
   ```

   3. templates 설정

   ```python
   <h1>username : {{ username }}</h1>
   <h2>password : {{ pwd }}</h2>
   ```



* GET 방식과 POST 방식

  * GET 방식 : 서버로 데이터를 전송할 때, url에 데이터를 포함하는 방식

  * POST 방식 : 서버로 데이터를 전송할 때, url에 데이터를 포함하지 않는다.

    ​		      ID와 비밀번호처럼 기본적인 보안이 필요한 곳에서 주로 쓰임.





​	**CSRF** 사이트 간 요청 위조(Cross-site Request Forgery) [doc](https://sj602.github.io/2018/07/14/what-is-CSRF/)

> 2008 옥션 해킹(해커가 옥션 운영자에게 CSRF 코드가 포함된 이메일을 보내서 관리자 권한을 얻어냈다))

- 웹 애플리케이션 취약점 중 하나로 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹페이지를 보안에 취약하게 한다거나 수정, 삭제 등의 작업을 하게 만드는 공격방법을 의미한다.
- 실제로 input type hidden 으로 특정한 hash 값이 담겨있는 것을 볼 수 있다.
- `setting py` 에 middleware 설정에 보면 csrf 관련된 내용이 설정된 것을 볼 수 있다.

**해당 csrf attack 보안과 관련된 설정은 settings.py에서 MIDDLEWARE 에 되어있다.**

> Middleware is a framework of hooks into Django’s request/response processing. It’s a light, low-level “plugin” system for globally altering Django’s input or output.

- 실제 토큰이 없을 때 오류가 raise 되는 시점을 보면 middleware 어쩌고저쩌고로 되어있다.

```
MIDDLEWARE = [
 'django.middleware.security.SecurityMiddleware',
 'django.contrib.sessions.middleware.SessionMiddleware',
 'django.middleware.common.CommonMiddleware',
 'django.middleware.csrf.CsrfViewMiddleware',
 'django.contrib.auth.middleware.AuthenticationMiddleware',
 'django.contrib.messages.middleware.MessageMiddleware',
 'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

- 4번째 줄에 있는 csrf 를 주석처리하면 토큰이 없어도 되지만 그런 보안에 취약한 것은 하지말자.
- Flask 보다 Django를 사용하는 이유도 기본적인 설정들을 통해 안정성 있고 편리한 개발을 할 수 있기 때문인 것. (플라스크가 Micro framework인 이유)
- 실제로 [상단의 요청 과정 그림](#4.2 Variable Routing) 에서 `urls.py` 이전에 Middleware의 설정 사항들을 순차적으로 거친다. 응답은 아래에서 위로부터 미들웨어를 적용시킨다.



### 6. Template Inheritance

- `home/templates/base.html` 만들기 (+bootstrap)

  > html 파일 모두 상속받게 수정하기

```html
<!DOCTYPE html>
<html lang="ko">
<head>
	<meta charset="UTF-8">
    <title>{% block title %}{% endblock %}</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.0/css/bootstrap.min.css" integrity="sha384-PDle/QlgIONtM1aqA2Qemk5gPOE7wFq8+Em+G/hmo5Iq0CCmYZLv3fVRDJ4MMwEA" crossorigin="anonymous">
</head>
</head>
<body>
    <h1>장고 연습</h1>
	<hr>
    <div class="container">
    	{% block body %}{% endblock %}     
    </div>
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.0/js/bootstrap.min.js" integrity="sha384-7aThvCh9TypR7fIc2HV4O/nFMVCBwyIUKL8XCtKE+8xgCgl/PQGuFsvShjr74PBp" crossorigin="anonymous"></script>

</body>
</html>
```

