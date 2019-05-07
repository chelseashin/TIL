Workshop

대전 2반 17번 신채원

2019-05-03

< Vue.js >

• 양방향 데이터 바인딩
• v-model 디렉티브

----

Problem) v-bind와 v-model 디렉티브를 활용하여, 다음와 같이 'Go!' 링크를 누르면 입력 창에 작성한 URL로 가도록 하는 '주소가 변하는 링크'를 만들어 봅시다.

```html
<div id="app">    
    <input type="text" v-model="url">    
    <a :href="url">Go!</a>
</div>
<script>    
    const app = new Vue({        
        el: '#app',        
        data: {            
            url: '',
        },    
    })
</script>
```

