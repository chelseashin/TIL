Workshop

대전 2반 17번 신채원

2019-04-10

< 데이터베이스 유효성 검사 >

* 데이터베이스에 값을 추가할 때, 아래와 같이 검증하려고 한다. 적절한 코드를 작성하시오.

```python
class Person(models.Model):
    last_name = models.CharField(max_length= 50)
    email = models.CharField(max_length=100, validators=[   1   ])
    age = models.IntegerField(validator= [    2    ])
```



```python
class django.db import models
from django.core.validators import EmailValidator, MinValueValidator

class Person(models.Model):
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100, validators=[EmailValidator(message="이메일 형식에 맞지 않습니다.")])
    age = models.IntegerField(validators=[MinValueValidator(20, message="미성년자는 노노")])
```

