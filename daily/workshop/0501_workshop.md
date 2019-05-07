Workshop

대전 2반 17번 신채원

2019-05-01

< Vue.js >

- Vue.js
- v-bind, v-for, v-if 디렉티브
- 인터폴레이션과 디렉티브의 활용

----

Problem) 다음과 같은 Vue 인스턴스가 있을 때, v-for와 v-if 디렉티브를 활용하여 짝수만 나타나도록 하는 리스트를 만들어 봅시다.

![image](https://user-images.githubusercontent.com/45935233/57284603-75a74500-70ec-11e9-934f-5565d3f4450a.png)

```html
<div id="app">
        <li v-for="number in numbers" v-if="number%2 === 0">{{ number }}</li>
    </div>
    <script>
        var app = new Vue({
            el: "#app",
            data: {
                numbers: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            },
        })
    </script>
```