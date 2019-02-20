Workshop

대전 2반 17번 신채원

2019-02-20

< SQL / Django Model >



1. 자신의 반에 있는 사람들의 데이터를 저장하는 Student모델을 생성합니다.

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    birthday = models.DateTimeField(auto_now_add=True)
    age = models.IntegerField()
```



2. 모델 마이그레이션 작업을 거친 후
   Admin페이지에서 주변 학생들의 이름을 세명 저장합니다.

```python
# 설계도 생성
python manage.py makemigrations students
# migration 파일들을 DB에 넣기! 이렇게 해야 모델 만들어짐
python manage.py migrate

student = Student()
student.name = '보라돌이'
student.email = 'boradori@gmail.com'
board.save()
student2 = Student(name="뚜비", email="dduby@gmail.com")
student3 = Student(name="나나", email='nana@gmail.com')
student4 = Student(name="뽀", email="bbo@gmail.com")
student.save()
```



3. 저장 후 Admin페이지에서 학생들의 목록을 보기 쉽게 만들기 위해서
   __str__메소드를 오버라이드 하여 name이 출력되게 만듭니다.

```python
from django.contrib import admin
from .models import Board

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    def __str__(self):
        return f'{self.name}'
    list_display = ("name")
admin.site.register(Student, StudentAdmin)
```

