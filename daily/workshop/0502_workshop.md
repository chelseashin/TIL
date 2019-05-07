Workshop

대전 2반 17번 신채원

2019-05-02

< Vue.js >

* Vue.js
* v-bind, v-on 디렉티브

* 이벤트 핸들링의 이해 및 활용
* Computed와 Watch의 활용

Problem) v-on 디렉티브를 활용하여, 다음과 같이 ‘+1’ 버튼을 누르면 숫자가 하나씩 증가하는
Counter 앱을 만들어 봅시다.

![image](https://user-images.githubusercontent.com/45935233/57286899-421ae980-70f1-11e9-8576-c34e590e2a80.png)

```html
<div id="app">
    <button @click="plus">
         +1
    </button>
    <h1>
        Counter : {{ count }}
    </h1>

</div>
<script>
    const app = new Vue({
        el: '#app',
        data: {
            count: 0,
        },
        methods: {
            plus: function () {
                this.count++
            }
        }
    })
</script>
```

