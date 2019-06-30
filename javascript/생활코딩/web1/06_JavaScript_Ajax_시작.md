## JavaScript - Ajax



2019-06-15

------

< 생활코딩 Web3 - Javascript - Ajax >



## Ajax

(**A**synchronous **J**avascript **A**nd **X**ml)

* 웹페이지의 정보를 부분적으로 변경
* 브라우저와 웹서버가 실시간으로 통신을 주고 받을 때 `Ajax`를 이용
* 웹페이지에서 일부 정보가 달라졌음에도 전체 페이지를 리로드하는 것은 효율적이지 않음
* `Ajax`는 리로드 없이 웹서버에게 정보를 요청해서 부분적으로 정보를 갱신해주는 기술
* `Ajax`를 이용하여 필요한 정보만을 부분적으로 낚아챌 수 있음



#### * Ajax의 효과

 * 사용자가 변경한 부분에만 집중할 수 있는 사용성 증대
 * 필요한 부분만 부분적으로 로드 할 수 있기 때문에 시간과 돈과 네트워크 자원을 절약
 * 기본적인 구조를 재사용하고 바뀔 수 있는 부분과 고정되는 것을 구분해서 바뀔 수 있는 부분만 동적으로 표현 가능
 * 폭발적으로 생산성 향상
 * 하나의 페이지로 여러개의 정보를 표현 : `Single Page Application`



#### * fetch API

* ajax를 구현하는 여러가지 최신 기술 중 하나
* fetch API는 기존의 방식에 비해서 더 유연하고, 분명
* `fetch('javascript')` 라고 하면 '웹브라우저야, javascript라는 파일을 서버에게 응답해줘'라고 요청한 것
* `then` : 응답이 끝나면 다음을 실행해줘. `callbackme`(함수)라는 것을 하도록 약속하는 것

```html
<body>
    <article>

    </article>
    <input type="button" value="fetch" onclick="
        // then 다음에 있는 것들 - 익명함수
        // fetch('html').then(function(response){
        //     response.text().then(function(text){
        //         document.querySelector('article').innerHTML = text;
        //     })
        // })
        // Asynchronous(비동기) - 병렬적. 실행되는 동안 다른 것들을 실행하도록 하는 것
        // then 다음에 오는 callback 함수가 호출될 때, response 객체라고 하는 입력값으로 주면서 호출함
        // response 객체 : fetch를 통해 요청했을 때 웹서버가 응답한 그 결과를 담고 있는 객체, 데이터를 의미. 그 안에서 여러가지 속성을 통해서 어떤 상태를 가지고 있는지 귀중한 단서들을 담고 있다.
        fetch('html').then(function(response){
            // console.log(response);
            // 상태 알고 싶을 때
            console.log(response.status);
            // 해당 파일 없으면 404 알람
            if(response.status == '404'){
                alert('Not found')
            }
        });
        // 위와 같은 함수
        // callbackme = function(){
        //     console.log('response end');
        // }
        // fetch('html').then(callbackme);
        console.log(1);
        console.log(2);
        console.log(3);
        // 결과 : 1 2 3 response end
        ">
</body>
```



----

 예전에 JavaScript를 배울 때 Ajax를 접했었는데 당시에는 비동기화를 하기 위함이라는 느낌만을 받았었다. 오늘 공부를 하면서 왜 Ajax를 사용하는 것이 좋은지, 어떤 효과가 있는지, 그 중 Fetch API라는 최신 기술이 있다는 것에 대해 많이 고민해볼 수 있던 시간이었다.  내가 요청한 부분에 한해서만 정보가 변경되어 전체의 리로딩 없이 부분에 집중할 수 있도록 함에 있어 보다 효율적일 수 있을 것이라 생각하였다. 이로 인해 생산량 역시 훨씬 좋아질 것이고 사용하는 사람 입장에서도 필요한 정보만을 캐치하기 수월하게 해준다는 점에서 꼭 필요한 기술이라고 생각한다. 빨리 나의 프로젝트에도 적용해보고 싶어졌고, 아직은 많이 낯설기 때문에 좀더 연습이 필요할 것이다. 이렇게 수업을 듣는 것에 그치지 않고 스스로 많이 연습하면서 JavaScript 실력을 길러야겠다.:smile: 