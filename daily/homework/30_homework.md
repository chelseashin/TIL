Homework

대전 2반 17번 신채원

2019-04-09

< M:N 관계 >

```python
class Post(models.Model):
    content = models.CharField(max_length=140)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    likes = models.[   (A)   ](settings.AUTH_USER_MODEL, [   (B)   ]='like_post_set', blank=True)
```



1. Post 모델과 User모델을 M:N 관계로 설정하여 좋아요 기능을 구현하려고 한다. 이 때 (A) 박스에 들어갈 클래스의 이름은 무엇인가?

   ```python
   ManyToManyField
   ```

   



2. 좋아요 기능을 구현하기 위하여 User 모델과 M:N 관계설정을 하려고 한다. 그런데 user 칼럼에서 이미 User 모델과 관계설정이 되어있기 때문에, 이를 구분하기 위해 (B) 박스에 들어갈 옵션은 무엇인가?

   ```python
   related_name
   ```

   