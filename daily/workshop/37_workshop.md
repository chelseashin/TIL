Workshop

대전 2반 17번 신채원

2019-05-02

< Web API 를 활용한 JS 응용 >

* 브라우저/node 환경에서 Axios를 활용해 GET/POST 요청을 보내보자.

![image](https://user-images.githubusercontent.com/45935233/57063381-01d8f700-6cfe-11e9-8a1f-c10babe3da6f.png)

```javascript
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
<script>
const axios = require("axios")
const url = "http://13.125.249.144:8080/ssafy/daejeon/2/posts"
axios.get(url)
    .then(res => {
    console.log(res.data.posts)
	})
    const data = {
        "post" : {
            "title" : "Hello, DJPY2",
            "content" : "NICE TO MEET YOU",
            "author" : "CHELSEA" 
        }
    }
    axios.post(url, data)
    	.then(() => console.log('message sent'))
</script>
```



* 요청예시. 아래형식으로 POST요청을 보내면, 생성된 post Object 를 응답으로 보냅니다.

![image](https://user-images.githubusercontent.com/45935233/57063413-203ef280-6cfe-11e9-91c6-175c27d2885c.png)