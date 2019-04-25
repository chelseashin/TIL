Workshop

대전 2반 17번 신채원

2019-04-09

< M:N 관계 >

* 게시물의 해시태그를 구현하기 위하여 아래와 같이 객체 관계 다이어그램을 작성하였다. 다이어그램을 바탕으로 models.py에 Post모델과 Hashtag 모델을 정의해본다.

![image](https://user-images.githubusercontent.com/45935233/56703157-a11c4e00-6742-11e9-8118-f8cbeb1583a4.png)



>models.py

```python
from django.db import models

class Hashtag(models.Model):
    content = models.TextField(unique=True)
    
    def __str__(self):
        return self.content
    
class Post(models.Model):
    hashtags = models.ManyToManyField(Hashtag, blank=True)
```

