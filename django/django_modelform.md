



* urls.py

```python
from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('new/', views.create, name='create'),
]
```



* models.py - 먼저 하는 것이 좋다.

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
```



```python 
$ python manage.py makemigration
$ python manage.py migrate
```



* views.py

```python
from django.shortcuts import render, redirect
from .forms import PostForm

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:list')     # 리턴 인덴테이션(위치) 주의!
    else:
    	form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/create.html', context)
```



* create.html

```python
<form method='POST'>    # action이 없으면 자기 자신을 다시 보여주는데 대신 방식은 post방식으로!
	{% csrf_token %}
    {{ form }}
    <input type="submit">
</form>
```



* form을 쓰는 이유는 코드의 일관성을 유지하기 위해
* 내가 model을 만들었기 때문에 하나하나 일일이 치지 않더라도 한번에 가져올 수 있음



* forms.py

```python
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:     # 어떤 데이터를 담고있는지에 대한 데이터 - 메타데이터로 관리하겠다.
        model = Post
        fields = ('title', 'content',)
```

