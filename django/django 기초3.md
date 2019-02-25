

19.02.21

< Django 기초 3 >

- UPDATE / DELETE 구현하기!!
- views.py
- 

```python
pip install faker
python : python shell 켜기
# faker : 랜덤으로 해당 내용 리턴
(django-venv) chelseashin:~/workspace/PROJECT02 $ python
Python 3.6.7 (default, Feb 13 2019, 00:39:46) 
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from faker import Faker
# 한국어 모드
>>> faker = Faker('ko_kr')
# 결과 무작위로 나옴
>>> faker.job()
'기타 식품가공관련 기계조작원'
>>> faker.address()
'제주특별자치도 안양시 삼성거리'
>>> faker.name()
'서성훈'
>>> faker.company()
'유한회사 하김류'
# 한글지원 안 되는 것도 있음
>>> faker.color()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Generator' object has no attribute 'color'
    
# 나가기
>>> exit()
```



* terminal

```python
# 앱 생성
(django-venv) chelseashin:~/workspace/PROJECT02 $ python manage.py startapp jobs
    # migration
(django-venv) chelseashin:~/workspace/PROJECT02 $ python manage.py makemigrations jobs
Migrations for 'jobs':
  jobs/migrations/0001_initial.py
    - Create model Job
(django-venv) chelseashin:~/workspace/PROJECT02 $ python manage.py migrate jobs
Operations to perform:
  Apply all migrations: jobs
Running migrations:
  Applying jobs.0001_initial... OK
```



