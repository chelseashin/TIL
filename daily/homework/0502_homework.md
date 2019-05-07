Homework

대전 2반 17번 신채원

2019-05-02

< Vue.js >

* v-bind, v-on 디렉티브
*  Computed와 Watch 속성

----

![image](https://user-images.githubusercontent.com/45935233/57285948-41815380-70ef-11e9-9ec9-f7c46ac27be8.png)

> ```javascript
> (a) :href
> ```



![image](https://user-images.githubusercontent.com/45935233/57285988-56f67d80-70ef-11e9-9ff1-f50575649308.png)

> ```javascript
> (a) @click
> ```



3. computed 속성과 watch 속성에 대하여 간략하게 설명하고, 이 둘의 차이점에 대해 작성하시오.

```
* computed
 computed 속성은 종속 대상을 따라 저장(캐싱)된다. 해당 속성이 종속된 대상이 변경될 때만 함수를 실행합니다.

* watch
 데이터 변경에 대한 응답으로 비동기식 또는 시간이 많이 소요되는 조작을 수행하려는 경우에 가장 유용하다. watch 옵션을 사용하면 비동기 연산 (API 엑세스)을 수행하고, 우리가 그 연산을 얼마나 자주 수행하는지 제한하고, 최종 응답을 얻을 때까지 중간 상태를 설정할 수 있다.
```

