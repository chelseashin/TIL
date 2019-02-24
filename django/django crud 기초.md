19.02.21



< Django CRUD 연습 >

 

### 전생을 알려주는 APP 만들기

----

views.py > urls.py > templates에 html 순으로 만들기



* terminal 명령어

```python
# 폴더로 이동 후 APP 생성
(django-venv) chelseashin:~/workspace/PROJECT02 $ python manage.py startapp jobs
python manage.py makemigrations jobs
python manage.py migrate jobs
```



* settings.py에서 앱 등록

```python
INSTALLED_APPS = [
    # 앱 등록
    'jobs.apps.JobsConfig',
```



* views.py

```python
from django.shortcuts import render
from faker import Faker
import requests
from .models import Job

# Create your views here.
def index(request):
    return render(request, 'jobs/index.html')
    
def pastlife(request):
    # index의 name을 받아옴
    name = request.GET.get('name')
    # db에 있는지 확인
    person = Job.objects.filter(name=name).first()   #왼쪽 : 컬럼, 오른쪽 : 받아온 것/ 첫번째 값을 받아옴 # 없으면 None을 반환
    # person = Job.objects.get(name=name)    # 없으면 에러가 뜸
    
    # 있으면 원래 직업을 가져오고
    if person:  # 값이 True가 나옴
        pastjob = person.pastjob
    # 없으면 faker로 새로운 직업을 넣어서 모델에 저장하고 가져옵니다!
    else:
        faker = Faker('ko-kr')
        # class에서 생성한 바로 위의 인스턴스 객체를 사용해야 함!
        pastjob = faker.job()
        person = Job(name=name, pastjob=pastjob)
        person.save()
        
    GIPHY_API = "UgIxshFJsyAnlMOl27I5ONuGaBRbvArQ"
    url = f"http://api.giphy.com/v1/gifs/search?api_key={GIPHY_API}&q={pastjob}&limit=1&lang=ko"
    data = requests.get(url).json()
    image = data.get('data')[0].get('images').get('original').get('url')
        
    return render(request, 'jobs/pastlife.html', {'person': person, 'image': image})
```



* urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('pastlife/', views.pastlife, name='pastlife'),
    path('', views.index, name='index'),
    ]
```



* models.py에서 클래스 생성

```python
from django.db import models

# Create your models here.
class Job(models.Model):
    name = models.CharField(max_length=20)
    pastjob = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
```



* admin.py에 클래스 등록. 후에 admin 페이지에서 확인 가능

```python
from django.contrib import admin
from .models import Job

# Register your models here.
# 클래스 등록
class JobAdmin((admin.ModelAdmin)):
    # 튜플과 리스트 모두 가능
    list_display = ['id', 'name', 'pastjob',]
admin.site.register(Job, JobAdmin)
```



* templates에 jobs폴더 만들고 그 안에 html파일 생성

* index.html

```python
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>INDEX</title>
</head>

<body>
    <h1>전생 APP</h1>
    <h2>전생을 알려드립니다!</h2>
    <form action="/jobs/pastlife/">
        <input type="text" name="name">
        <input type="submit" value="Submit">
    </form>
</body>
</html>

```



* pastlife.html

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>PASTLIFE</title>
</head>
<body>
    <h1>{{ person.name }}님의 전생은 {{ person.pastjob }} 입니다.</h1>
    <img src="{{ image }}" alt="움짤"></img><br>
    <a href="/jobs/">다시 해보기</a>
</body>
</html>
```

