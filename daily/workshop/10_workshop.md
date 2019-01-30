Daily Workshop

대전 2반 17번 신채원

2019-01-17



< CSS >

##### # Selector 를 활용한 DOM 탐색 실습.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
        #ssafy> p:nth-child(2){
            color: red;
        }
    </style>
</head>
<body>
    <div id="ssafy">
        <h2>어떤 게 선택될까?</h2>
        <p>첫번째 단락</p>
        <p>두번째 단락</p>
        <p>세번째 단락</p>
        <p>네번째 단락</p>
    </div>
</body>
</html>
```





#### nth-child(n)

* 모든 자식의 순서에서 찾음

* 해당 태그의 순서


#### nth-of-type(n)

- 해당하는 자식 태그 요소에서의 순서를 찾음
- 부모 속성에서 특정 태그를 가진 자식 속성에서 몇번째에 해당하는지