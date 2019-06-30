## JavaScript - 비교연산자/Boolean/조건문



2019-06-03

----

< 생활코딩 Web2 - Javascript >



meaning of `program` : 음악회 공연 순서. '순서' 순서를 만드는 행위가 `programming`
이러한 행위를 하는 사람이 `programmer`.

* `JavaScript` : programming language, 어떤 것을 순서대로 작동시킴. 사용자와의 상호작용을 위해 순서대로, 동적으로 기능하도록 함. 조건, 반복, 정리정돈할 수 있는 형태로 발전해나감.  

* `HTML` : language, html은 웹페이지를 묘사하는 것이기 때문에 시간의 순서와 상관 없음



#### JavaScript 조건문

 하나의 프로그램이 하나의 흐름으로 가는 것이 아니라 조건에 따라 다른 순서의 기능이 실행되도록 하는 것. 단순한 반복문이 아니라 아주 복잡한 업무까지 가능케하는 혁명적인 도구.



* #### 조건문 실습 - day/night 버튼 하나로 만들기(toggle)

  * if/else문 적용하기 

```html
<body>
    <h1><a href="web_day_and_night3.html">WEB</a></h1>
    <!-- 이 부분 변경 - night/day 모드 'Toggle버튼' 만들기 -->
    <input id="night_day" type="button" value="night" onclick="
      if(document.querySelector('#night_day').value === 'night'){
        document.querySelector('body').style.backgroundColor = 'black';
        document.querySelector('body').style.color = 'white';
        document.querySelector('body').dataset.mode = 'night';
        this.value ='day';
      } else {
        document.querySelector('body').style.backgroundColor = 'white';
        document.querySelector('body').style.color = 'black';
        document.querySelector('body').dataset.mode = 'day';
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





* #### 비교 연산자 

  ```html
  <h1>Comparison operators & Boolean</h1>
  <h2>===</h2>
  <h3>1===1</h3>
  <script>
      document.write(1===1); 
      // true
  </script>
  
  <h3>1===2</h3>
  <script>
      document.write(1===2);
      // false
  </script>
  
  <!-- 1이 2보다 작은가? -->
  <h3>1&lt;2</h3>
  <script>
      document.write(1<2);
      // True
  </script>
  
  <!-- 1이 1보다 작은가? -->
  <h3>1&lt;1</h3>
  <script>
      document.write(1<1);
      // false
  </script>
  ```

  

* #### Boolean 데이터타입

  ```html
  <h1>Conditional Statements</h1>
  <h2>Program</h2>
  <script>
      // 줄바꿈 <br>
      document.write("1<br>");
      document.write("2<br>");
      document.write("3<br>");
      document.write("4<br>");
  </script>
  <h2>IF-true</h2>
  <!-- 실행 순서 확인 : 1 2 4 -->
  <script>
      document.write("1<br>");
      if(true){
          document.write("2<br>");
      } else {
          document.write("3<br>");
      }
      document.write("4<br>");
  </script>
  
  <h2>IF-false</h2>
  <!-- 실행 순서 확인 : 1 3 4 -->
  <script>
      document.write("1<br>");
      if(false){
          document.write("2<br>");
      } else {
          document.write("3<br>");
      }
      document.write("4<br>");
  </script>
  ```

  