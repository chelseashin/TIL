from django.shortcuts import render, redirect
from django.contrib.auth.forms import 
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            f = form.save()
            auth_login(request, user)
        return redirect('posts:list')
    else:
        form = UserCreationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/form.html', context)