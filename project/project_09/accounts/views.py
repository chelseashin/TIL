from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from .models import User
from .forms import UserCustomCreationForm

# Create your views here.
@require_http_methods(["GET", "POST"])
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:list')
    if request.method == 'POST':
        user_form = UserCustomCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            auth_login(request, user)
            return redirect('movies:list')
    else:
        user_form = UserCustomCreationForm()
    context = {'form': user_form}
    return render(request, 'accounts/forms.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('movies:list')
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect('movies:list')
    else:
        login_form = AuthenticationForm()
    context = {'form': login_form}
    return render(request, 'accounts/forms.html', context)


def logout(request):
    auth_logout(request)
    return redirect('movies:list')
    
@login_required
def user_list(request):
    users = User.objects.all()
    context = {
        'users' : users,
    }
    return render(request, 'accounts/user_list.html', context)
    
def user_detail(request, user_pk):
    User = get_user_model()
    movie_user = get_object_or_404(User, pk=user_pk)
    context = {
        'movie_user' : movie_user,
    }
    return render(request, 'accounts/user_detail.html', context)
    
@login_required
def follow(request, user_pk):
    target_user = get_object_or_404(get_user_model(), pk=user_pk)
    # target_user이 팔로워하고 있는 모든 유저에 현재 접속 유저가 있다면,
    if request.user in target_user.followers.all():
        target_user.followers.remove(request.user)    # 언팔로우
    else:  # 아니면 
        target_user.followers.add(request.user)       # 팔로우
    return redirect('accounts:user_detail', user_pk)
    # return redirect(target_user)