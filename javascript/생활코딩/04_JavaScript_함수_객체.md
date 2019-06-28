## JavaScript - 함수/객체



2019-06-04~05

------

< 생활코딩 Web2 - Javascript >



* #### 함수 

  * 유지보수가 편해짐
  * 웹페이지의 크기가 확 줄어짐
  * 똑같은 로직을 가질 때 사용
  * 함수 이름을 붙일 수 있기 때문에 사용처나 기능을 분명히 알 수 있게 됨



* #### 실습 - day_and_night.html 에서 함수만들기

```html
<head>
  <title>WEB1 - JavaScript</title>
  <meta charset="utf-8">
  <script>
    // 함수 생성
    function nightDayHandler(self){
    var target = document.querySelector('body');
        if(self.value === 'night'){
            target.style.backgroundColor = 'black';
            target.style.color = 'white';
            self.value ='day';
 
            var alist = document.querySelectorAll('a');
            var i = 0;
            while(i < alist.length){
                alist[i].style.color = 'powderblue';
                i = i + 1;
            }

        } else {
            target.style.backgroundColor = 'white';
            target.style.color = 'black';
            self.value ='night';

            var alist = document.querySelectorAll('a');
            var i = 0;
            while(i < alist.length){
                alist[i].style.color = 'blue';
                i = i + 1;
            }
        }
    } 
  </script>
</head>
<body>
    <h1><a href="ex3.web_day_and_night4.html">WEB</a></h1>
    <input this type="button" value="night" onclick="
        nightDayHandler(this);
    ">
    <input this type="button" value="night" onclick="
        nightDayHandler(this);
    ">
</body>
```





* #### 객체

  * 함수라는 기반 위에 객체라는 것이 존재

  * 함수와 변수가 많아짐에 따라 연관된 것들을 그루핑해서 정리정돈해주는 도구

  * 순서 없이 정보를 저장하는 것

  * 이름이 있는 정리정돈 상자의 개념

  * `배열`은 대괄호, `객체`는 중괄호로 표현

  * 설명하기 어려움 ..

  * 객체의 특성, 기능에 대해 무엇인지 알기 위해 경험을 쌓아갈 필요가 있음

    ```html
    <body>
        <h1>Object</h1>
        <h2>Create</h2>
        <script>
            var coworkers = {
                "programmer" : "chaewon",
                "development" : "chaeonny",
                "designer" : "chelsea"
            };
            document.write("programmer : "+coworkers.programmer + "<br>");
            document.write("development : "+coworkers.development + "<br>");
            document.write("designer : "+coworkers.designer + "<br>" );
            coworkers.bookeeper = "yuna";
            document.write("bookeeper : "+coworkers.bookeeper + "<br>" );
            coworkers["data scientist"] = "rabbit";
            document.write("data scientist : "+coworkers["data scientist"] + "<br>" );
        </script>
    </body>
    ```





* #### 실습 - day_and_night.html 에서 함수만들기

```html
<head>
  <title>WEB1 - JavaScript</title>
  <meta charset="utf-8">
  <script>
    //   객체화 - Links, Body
    var Links = {
        setColor: function (color){
            var alist = document.querySelectorAll('a');
            var i = 0;
            while(i < alist.length){
            alist[i].style.color = color;
            i = i + 1;
            }
        }
    }
  var Body = {
    setColor: function (color){
        document.querySelector('body').style.color = color;
    },
    setBackgroundColor: function (color) {
        document.querySelector('body').style.backgroundColor = color;
    }
  }
  function nightDayHandler(self){
    var target = document.querySelector('body');
    if(self.value === 'night'){
      Body.setBackgroundColor('black');
      Body.setColor('white');
      self.value = 'day';
      Links.setColor('powderblue');
    } else {
      Body.setBackgroundColor('white');
      Body.setColor('black');
      self.value = 'night';
      Links.setColor('blue');
    }
  }
  </script>
</head>
<body>
    <h1><a href="index.html">WEB</a></h1>
  <input id="night_day" type="button" value="night" onclick="
    nightDayHandler(this);
  ">
</body>
```



함수와 객체는 정말 배울수록 어려운 개념이다. 이들을 잘 다룰 줄 아는 것이 진짜 실력이라고 생각한다. 실력있는 개발자가 되고싶다:smile: 