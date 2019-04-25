Workshop

대전 2반 17번 신채원

2019-04-11

< 데이터베이스 시딩 >

* 아래는 Django에서 myapp의 Musician class에 저장된 기본 시드 데이터이다 . 이를 적용하기 위해 필요한 json 파일을 만들어 적용해보자

![image](https://user-images.githubusercontent.com/45935233/56711213-cde15d00-6764-11e9-8d2d-91e7a5b079d8.png)



> models.py

```python
from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
```



> admin.py

```python
from django.contrib import admin
from .models import Person

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name', )
admin.site.register(Person, PersonAdmin)
```



> 결과 : sample.json

```json
[
  {
    "model": "myapps.person",
    "pk": 1,
    "fields": {
      "first_name": "John",
      "last_name": "Lennon"
    }
  },
  {
    "model": "myapps.person",
    "pk": 2,
    "fields": {
      "first_name": "Paul",
      "last_name": "McCartney"
    }
  }
]
```

