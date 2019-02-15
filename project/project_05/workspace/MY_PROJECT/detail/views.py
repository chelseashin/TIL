from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'detail/index.html')
    
def qna(request):
    return render(request, 'detail/qna.html')
    
def mypage(request):
    return render(request, 'detail/mypage.html')
    
def signup(request):
    return render(request, 'detail/signup.html')
    
def not_found(request, word):
    return render(request, 'detail/not_found.html', {'word':word})
    