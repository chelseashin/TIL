Workshop

대전 2반 17번 신채원

2019-04-09

< Django auth - 사용자인증/사용자권한관리 >

* 아래의 회원가입 페이지는 django.contrib.auth.forms 안에 있는 UserCreationForm()
  을 활용한 것이다. 아래 페이지를 위한 view, url, template 을 작성하세요

![1554791678007](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1554791678007.png)

* views.py

```python
# 회원가입
def signup(request):
    if request.user.is_authenticated:
        return redirect('boards:index')
        
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('boards:index')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/auth_form.html', context)
```



* urls.py

```python
from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    ]
```



* templates - signup.html

```html
{% extends 'boards/base.html' %}
{% block body %}
{% load crispy_forms_tags %}

<h1>회원가입</h1>
<form action="" method="POST">
    {% csrf_token %}
    {{ form | crispy }}
    <input type="submit" name="submit"/>
</form>

{% endblock %}
```

