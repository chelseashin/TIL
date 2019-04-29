from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

    return render(request)
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