Homework

대전 2반 17번 신채원

2019-05-02

< Web API 를 활용한 JS 응용 >

1. Axios 를 사용하는 아래 코드를 완성하시오.
   - Browser 는 axios CDN을 통해,
   - Node 는 npm install 과 require 를 통해 axios 를 가져와야 합니다.

![image](https://user-images.githubusercontent.com/45935233/57061865-73627680-6cf9-11e9-837e-1504fb4d0982.png)



```javascript
const URL = "https://dog.ceo/api/breeds/image/random"
axios.get(URL)
	.then(res => {
    	const imgSrc = res.data.message
        return imgSrc
	})
    .then(imageSource => {
        console.log(imageSource) 
})
```

