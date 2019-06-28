## JavaScript - Ajax적용_fetch API _hash



2019-06-16

------

< 생활코딩 Web3 - Javascript - Ajax >



## Ajax 적용



#### * 초기 페이지 구현 - index.html

```html
<body>
  <!-- <h1><a href="index.html">WEB</a></h1> -->
  <h1><a href="#!welcome">WEB</a></h1>
  <input id="night_day" type="button" value="night" onclick="
    nightDayHandler(this);
  ">
  <div id="grid">
    <ol id="nav">
      <!-- 방법 4 - list 파일로 쪼개기 -->
      <!-- list 파일로 외부로 빼서 추가/수정할 수 있음 -->
      <!-- data가 들어있는 list파일을 수정함으로써 app입장에서 사용자들이 마음대로 변경하는 사고를 방지하고 contents를 입력하는 입장에서 어떻게 해야하는 것으로부터 자유로울 수 있음. -->

      <!-- 방법 3 - 리팩토링(함수화) -->
      <!-- # : 북마크기능 / ! : hash bang -->
      <!-- hash bang을 이용해서 어떤 사이트에 처음 들어왔을 때 초기 페이지를 로드하는 방법 -->
      
      <!-- 방법 2 - fetch API 적용 -->
        <!-- <li><a onclick="
          fetch('html').then(function(response){
            response.text().then(function(text){
              document.querySelector('article').innerHTML = text;
            })
          });
        ">HTML</a></li>
        <li><a onclick="
          fetch('css').then(function(response){
            response.text().then(function(text){
              document.querySelector('article').innerHTML = text;
            })
          });
        ">CSS</a></li>
        <li><a onclick="
          fetch('javascript').then(function(response){
            response.text().then(function(text){
              document.querySelector('article').innerHTML = text;
            })
          });
        ">JavaScript</a></li> -->
      
        <!-- 방법 1 - 기본 -->
      <!-- <li><a href="1.html">HTML</a></li>
      <li><a href="2.html">CSS</a></li>
      <li><a href="3.html">JavaScript</a></li> -->
    </ol>
    <article>

    </article>
    <script>
    function fetchPage(name){
      fetch(name).then(function(response){
        response.text().then(function(text){
          document.querySelector('article').innerHTML = text;
        })
      });
    }
    if(location.hash){
      fetchPage(location.hash.substr(2));
    } else {
      fetchPage('welcome');
    }
    // 방법 4 - list 파일 불러오기 
    fetch('list').then(function(response){
      response.text().then(function(text){
        // ','를 기준으로 나누어 배열을 만들어서 하나씩 꺼내 사용해보자
        var items = text.split(',');
        var i = 0;
        var tags = '';
        while(i<items.length){
          var item = items[i];
          item = item.trim();
          var tag = '<li><a href="#!'+item+'" onclick="fetchPage(\''+item+'\')">'+item+'</a></li>';
          tags = tags + tag;
          i = i + 1;
        }
        // id값이 'nav'인 태그 선택
        document.querySelector('#nav').innerHTML = tags;
      })
    });
    </script>
</body>
```

* 위 html파일은 data면서 logic(application)이 공존함
* 사용자 입장에서 list라는 파일에만 집중하면 됨
* 글 목록이 ajax를 사용하게 됨
* 사소한 장식들이 구현하기가 훨씬 어려움을 느낌....
* data를 compact하게, data를 중심으로 만드는 방법.



#### * list 파일

```
html,css,javascript,ajax
```





#### * fetch API polyfill

* 2018년 현재 fetch API는 비교적 최신 기능 
* 따라서 아직 지원되지 않는 브라우저를 사용자가 사용하는 경우 동작하지 않을 수 있음
* 오래된 브라우저에서 fetch 기능을 사용할 때 사용 
* polypill을 이용하면 fetch API를 지원하지 않는 웹브라우저에서도 이용할 수 있음
* 지원되지 않는 브라우저에서 코드가 실행되면 polyfill 이 활성화되서 대신 동작
*  fetch API의 ployfill을 적용해보자





#### * caniuse.com

* 어떤 특정 기능이 어떤 브라우저에서 현재 지원되는가 볼 수 있는 사이트.

![image](https://user-images.githubusercontent.com/45935233/59564719-20643900-9085-11e9-8d42-c0ba65374cb1.png)



* index.html - fetch 사용하기

```html
<head>
  <!-- fetch를 잘 사용할 수 있도록! 우리가 원하는 대로 동작할 수 있도록! -->
  <!-- fetch API가 없는 (오래된) 브라우저일 때 사용 -->
  <script src="fetch/fetch.js"></script>
</head>
```





----

 Ajax를 사용하여 페이지의 전환 없이 서버로부터 데이터를 부분적으로 가져와서 동적으로 페이지의 내용을 교체하는 방법을 살펴보았다. 페이지 단위로 머물러있던 웹은 문서에서 확장되어서 본격적인 애플리케이션 대열에 합류하게 된다. 웹은 문서라는 토대 위에 애플리케이션이라는 사용자 친화적인 기능을 가지게 된 것. 검색이 되면서도 애플리케이션으로서 역할을 할 수 있는 것이 web이 가지고 있는 특성을 가지게 되었다고 볼 수 있다. 보다 풍부한 정보를 동적으로 표현하기 위한 이러한 Ajax를 잘 사용할 줄 알면 참 좋을 것이라고 생각했다. 조금씩 머릿 속에 정리되어가는 느낌이다. 조금 더 나를 위한 프로젝트를 하면서 많이 연구하고 Trial and Error을 거듭해볼 필요가 있을 것이다. 오늘도 수고했습니다. 내일도 화이팅:smiley: