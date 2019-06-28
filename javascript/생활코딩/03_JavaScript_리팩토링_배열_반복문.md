## JavaScript - 리팩토링/배열/반복문



2019-06-04

------

< 생활코딩 Web2 - Javascript >



* #### 리팩토링(Refactoring)

  * 동작하는 것을 그대로 두고 코드 자체를 효율적으로 만들어서 가독성을 높이고 유지보수하기 편하게 하고, 중복된 것을 줄이는 방향으로 코드를 개선하는 것을 `리팩토링`이라고 함. 틈틈이 해주면 효율도 오르고 좋다. 

```html
<body>
    <h1><a href="web_day_and_night4.html">WEB</a></h1>
    <!-- 이 부분 변경 - night/day 모드 'this'사용하여 버튼 만들기 -->
    <input this type="button" value="night" onclick="
      var target = document.querySelector('body');
      if(this.value === 'night'){
        target.style.backgroundColor = 'black';
        target.style.color = 'white';
        this.value ='day';
      } else {
        target.style.backgroundColor = 'white';
        target.style.color = 'black';
        this.value ='night';
      }      
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
```



​	

* #### 배열(Array)

  * 데이터가 많아짐에 따라 감당해야 할 데이터를 복잡하지 않게, 서로 연관된 데이터를 수납상자에 담는 느낌으로 단순하게 정리한 것이라고 생각해보자.
  * 정보를 순서대로 담는 그릇.
  * 배열 정의 ex) var chelsea = ['name', 'nickname', 'email', 'age']; 
  * 값 가져오기
  * 데이터 추가하기
  * 데이터 갯수 보여주기

```html
<body>
    <!-- 배열 정의 -->
    <h1>Array</h1>
    <h2>Syntax</h2>
    <script>
    var coworkers = ["egoing", "leezche"];
    </script>

    <!-- 값 가져오기 -->
    <h2>get</h2>
    <script>
    document.write(coworkers[0]);
    document.write(coworkers[1]);
    </script>

    <!-- 데이터 추가 -->
    <h2>add</h2>
    <script>
    coworkers.push('duru');
    coworkers.push('taeho');
    </script>

    <!-- 데이터 갯수(array length property) -->
    <h2>count</h2>
    <script>
    document.write(coworkers.length);
    </script>
</body>
```

#### 

* #### 반복문(loop)

  * 코드의 불필요한 중복을 막기 위해 존재

```html
<body>
    <h1>Loop</h1>
    <ul>
    <script>
        document.write('<li>1</li>');
        // 이 두 줄의 코드를 3번 반복하도록 함
        var i = 0;
        while(i < 3) {
            document.write('<li>2</li>');
            document.write('<li>3</li>');
            i = i + 1;
        }
        document.write('<li>4</li>');
    </script>
    </ul>
</body>
```



* #### 실습 - while/for loop

```html
<body>
    <h1>Loop & Array</h1>
    <script>
        var coworkers = ['egoing','leezche','duru','taeho'];
    </script>
    <h2>Co workers</h2>
    <h5>while loop</h5>
    <ul>
        <script>
            // coworkers 배열의 길이만큼 반복 실행
            var i = 0;
            while(i < coworkers.length){
                document.write('<li><a href="http://instagram.com/'+coworkers[i]+'">'+ coworkers[i]+'</a></li>');
                i = i + 1;
            }
        </script>
    </ul>
    <hr>
    <h5>for loop</h5>
    <ul>
        <script>
            for (var j = 0; j < coworkers.length; j++) {
                document.write('<li><a href="http://instagram.com/'+ coworkers[j] +'">'+ coworkers[j] + '</li>');
            }
        </script>
    </ul>
</body>
```



* day_and_night.html의 콘솔창에서 실행

```javascript
var alist = document.querySelectorAll('a');
var i = 0;
while(i < alist.length){
    console.log(alist[i]);
    i = i + 1;
}

// 결과 확인
// 모든 a link를 볼 수 있음
```



* 모든 a태그의 글씨를 'crimson' 색으로 바꾸기

```javascript
var alist = document.querySelectorAll('a');
var i = 0;
while(i < alist.length){
    console.log(alist[i]);
	alist[i].style.color = 'crimson';
    i = i + 1;
}
```



* #### 실습 - day/night마다 a태그 글씨색 바꾸기

```html
<h1><a href="ex3.web_day_and_night4.html">WEB</a></h1>
    <!-- 이 부분 변경 - night/day 모드 'this'사용하여 버튼 만들기 -->
    <input this type="button" value="night" onclick="
      var target = document.querySelector('body');
      if(this.value === 'night'){
        target.style.backgroundColor = 'black';
        target.style.color = 'white';
        this.value ='day';
        // 추가
        var alist = document.querySelectorAll('a');
        var i = 0;
        while(i < alist.length){
            alist[i].style.color = 'powderblue';
            i = i + 1;
        }

      } else {
        target.style.backgroundColor = 'white';
        target.style.color = 'black';
        this.value ='night';

        // 추가
        var alist = document.querySelectorAll('a');
        var i = 0;
        while(i < alist.length){
            alist[i].style.color = 'blue';
            i = i + 1;
        }
      }      
    ">
```

