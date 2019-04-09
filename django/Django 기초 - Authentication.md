### Django 기초 - Authentication

- django
- 새로운 앱 생성 - accounts
- views.py

```python
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
# 회원가입
def signup(request):
    # 회원가입 create 동작
    if request.user.is_authenticated:    # 로그인 되어 있으면
        return redirect('boards:index')
    # 분기
    if request.method == "POST":
        form = UserCreation Form(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('boards:index')
    # 페이지 띄워주기
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)
```



* urls.py

```python
from django.urls import path
from . import views
# 앱이름 등록
app_name = "accounts"

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    ]
```



* signup.py

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

