from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Hi, hello')

def info(request):
    return render(request, 'info.html')
    
    
student = {'보라돌이': 26, '뚜비': 23, '나나' : 21, '뽀' : 18}

def show(request, name):
    # age = student[name] # 에러 뿜기 때문에 선호 X
    age = student.get(name, 'unknown')
    teacher = {'address': '대전', 'name': '준호', 'age' : 30}
    return render(request, 'show.html', {'name': name, 'age': age, 'teacher' : age})   # 넘겨줄 값!