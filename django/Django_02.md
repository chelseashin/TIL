## Django_02

[TOC]

**Content**

1. [DTL](https://github.com/djpy2/Django/blob/master/Django_02.md#0-dtl)
2. [static 파일 관리](https://github.com/djpy2/Django/blob/master/Django_02.md#1-static-%ED%8C%8C%EC%9D%BC-%EA%B4%80%EB%A6%AC)
3. [URL 설정 분리](https://github.com/djpy2/Django/blob/master/Django_02.md#2-url-%EC%84%A4%EC%A0%95-%EB%B6%84%EB%A6%AC)
4. [Template name spacing](https://github.com/djpy2/Django/blob/master/Django_02.md#3-template-name-spacing)
5. [Template inheritance](https://github.com/djpy2/Django/blob/master/Django_02.md#4-template-inheritance)
6. [디렉토리 구조](https://github.com/djpy2/Django/blob/master/Django_02.md#5-%EB%94%94%EB%A0%89%ED%86%A0%EB%A6%AC-%EA%B5%AC%EC%A1%B0)

----

>수업 전 사전작업
>
>`home/templates/index.html` 생성
>
>```
>{% extends 'base.html' %}
>{% block title %}Index{% endblock  %}
>{% block body %}
>	<h1>저녁 장고!</h1>
> 	<a href="/home/dinner">저녁 추천 받기</a> d
>{% endblock  %}
>def index(request):
> 	# return HttpResponse('Welcome to Django !')
> 	return render(request, 'index.html')
>```

