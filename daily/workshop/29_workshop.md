Workshop

대전 2반 17번 신채원

2019-04-08

< 데이터베이스 관계 >

* 아래의 Django코드를 바탕으로 개체-관계 다이어그램을 작성해본다.



```python
from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=140)
    
class Album(models.Model):
    artist = models.ForeignKey(Musicial, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
```

> Musician과 Album의 1:N 관계

![image](https://user-images.githubusercontent.com/45935233/56702272-1fc2bc80-673e-11e9-8ad5-136d24e0350c.png)