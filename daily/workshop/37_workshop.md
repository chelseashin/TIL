Workshop

대전 2반 17번 신채원

2019-05-02

< Web API 를 활용한 JS 응용 >

* 브라우저/node 환경에서 Axios를 활용해 GET/POST 요청을 보내보자.

![image](https://user-images.githubusercontent.com/45935233/57063381-01d8f700-6cfe-11e9-8a1f-c10babe3da6f.png)

```javascript
<button id="button">게시글 작성</button>
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
    <script>
        const workShop = function () {
            const data = {
            "post" : {
                "title": "Today is Friday",
                "content": "hihi",
                "author" : "chelseashin",
            }
        }
        axios.post("http://13.125.249.144:8080/ssafy/daejeon/2/posts", data)
            .then(res => console.log('글이 작성되었습니다.'))
            .catch(error => console.log('에러가 발생했습니다.'))
        }
    	
    const workShopButton = document.querySelector("#button")
    workShopButton.addEventListener('click', workShop)
    </script>
```



* 요청예시. 아래형식으로 POST요청을 보내면, 생성된 post Object 를 응답으로 보냅니다.

![image](https://user-images.githubusercontent.com/45935233/57063413-203ef280-6cfe-11e9-91c6-175c27d2885c.png)