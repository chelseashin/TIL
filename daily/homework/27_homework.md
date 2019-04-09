Homework

대전 2반 17번 신채원

2019-04-09

< Django auth - 사용자인증/사용자권한관리 >

1. 로그인을 한 사용자만 게시물을 작성할 수 있도록 코드를 작성하려고 한다.
  빨간 박스에 들어갈 코드를 작성하세요

```python
from django.contrib.auth.decorators import login_required

@login_required
def create(request):
    if request.method == 'POST':
        board_form = BoardForm(request.POST)
```



2. Board 모델에 게시물을 작성한 사람을 저장할 칼럼을 추가하려고 한다.
   이를 위해 필요한 모듈과 ForeignKey() 에 넣어야 할 인자를 작성하세요.

```python
from django.conf import settings

class Board(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```