## JavaScript - 데이터타입/변수/연산자/태그선택



2019-06-03

----

< 생활코딩 Web2 - Javascript >



- #### 데이터 타입

  - Number - 무한히 많은 수 데이터

  - String - 무한히 많은 문자 데이터

  - Boolean - 단 두 개의 데이터만 존재(True/False)

    

#### * 변수(Variable) vs 상수(Constant)

```javascript
var name = 'egoing';
alert("hi my name is " + name)
```



#### * 연산자

* 산술연산자
* 삼향연산자





1. CSS의 중요한 문법들

2. JavaScript를 이용해서 제어하고자 하는 태그를 선택하는 것



#### * 실습 - 주간/야간 모드

###### body태그를 선택하여 style 속성을 동적으로, 상호작용적으로 넣으려고 함!

```html
<!doctype html>
<html>
<head>
  <title>WEB1 - JavaScript</title>
  <meta charset="utf-8">
</head>
<body>
    <h1><a href="index.html">WEB</a></h1>
    <!-- 이 부분 변경 - night/day 모드 버튼 만들기 -->
    <input type="button" value="night" onclick="
      document.querySelector('body').style.backgroundColor = 'black';
      document.querySelector('body').style.color = 'white';
    ">
    <input type="button" value="day" onclick="
      document.querySelector('body').style.backgroundColor = 'white';
      document.querySelector('body').style.color = 'black';
    ">
    <ol>
      <li><a href="1.html">HTML</a></li>
      <li><a href="2.html">CSS</a></li>
      <li><a href="3.html">JavaScript</a></li>
    </ol>
    <h2>JavaScript</h2>
    <p>
      JavaScript (/ˈdʒɑːvəˌskrɪpt/[6]), often abbreviated as JS, is a high-level, dynamic, weakly typed, prototype-based, multi-paradigm, and interpreted programming language. Alongside HTML and CSS, JavaScript is one of the three core technologies of World Wide Web content production. It is used to make webpages interactive and provide online programs, including video games. The majority of websites employ it, and all modern web browsers support it without the need for plug-ins by means of a built-in JavaScript engine. Each of the many JavaScript engines represent a different implementation of JavaScript, all based on the ECMAScript specification, with some engines not supporting the spec fully, and with many engines supporting additional features beyond ECMA.
    </p>
</body>
</html>

```



* 결과 확인

  <!doctype html>
  <html>
  <head>
    <title>WEB1 - JavaScript</title>
    <meta charset="utf-8">
  </head>
  <body>
      <h1><a href="web_day_and_night2.html">WEB</a></h1>
      <!-- 이 부분 변경 - night/day 모드 버튼 만들기 -->
      <input type="button" value="night" onclick="
        document.querySelector('body').style.backgroundColor = 'black';
        document.querySelector('body').style.color = 'white';
      ">
      <input type="button" value="day" onclick="
        document.querySelector('body').style.backgroundColor = 'white';
        document.querySelector('body').style.color = 'black';
      ">
      <ol>
        <li><a href="1.html">HTML</a></li>
        <li><a href="2.html">CSS</a></li>
        <li><a href="3.html">JavaScript</a></li>
      </ol>
      <h2>JavaScript</h2>
      <p>
        JavaScript (/ˈdʒɑːvəˌskrɪpt/[6]), often abbreviated as JS, is a high-level, dynamic, weakly typed, prototype-based, multi-paradigm, and interpreted programming language. Alongside HTML and CSS, JavaScript is one of the three core technologies of World Wide Web content production. It is used to make webpages interactive and provide online programs, including video games. The majority of websites employ it, and all modern web browsers support it without the need for plug-ins by means of a built-in JavaScript engine. Each of the many JavaScript engines represent a different implementation of JavaScript, all based on the ECMAScript specification, with some engines not supporting the spec fully, and with many engines supporting additional features beyond ECMA.
      </p>
  </body>
  </html>