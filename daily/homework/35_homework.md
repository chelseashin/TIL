Homework

대전 2반 17번 신채원

2019-04-30

< JS & ES6 >

1.  JS 는 ES6 이전과 이후로 많은 것이 바뀌었다. ES5 까지는 ‘var ‘키워드로 변수 를 선언했다면, ES6 이후로는 ‘let’ 과 ‘const’ 키워드가 등장했다. ‘let’ 과 ‘const’ 의 차이점과 언제 사용하는지 간략하게 기술하시오.

   

   두개의 공통점은 var와 다르게 `변수 재선언 불가능`이다.

   `let`과 `const`의 차이점은 변수의 `immutable`여부이다.

   * `let` : 변수 재할당이 가능, 일반적인 변수에 해당. 추후에 값이 바뀔 것이 확실할 경우 사용
   * `const` : 상수, 언제나 같은 값. 한번 할당되고 재할당, 재선언이 되지 않을 경우에 사용



2. JS 에서는 key – value 로 이루어진 자료구조를 Object 라고 부른다. Object 와 JSON 의 차이를 간략하게 기술하시오.
   * `Object` : JS engine 메모리 안에 있는 데이터 구조

   * `Json` : JS 객체 형식으로 데이터의 구조를 표기하기 위한 단순한 문자열. 객체 내용을 기술하기 위한 txt파일(json파일이므로, .json 파일이 존재)

     



3. 해당 코드에서 ‘Value’ 에 접근하는 두 가지 방법(코드)을 모두 작성하시오.

```javascript
const myObject = {
    key: 'Value'
}
```



* 정답

  ```javascript
  // 1.
  myObject.key
  
  // 2. 
  myObject["key"]
  ```



4. 아래 주석에 따라 JS코드를 작성하시오 

![image](https://user-images.githubusercontent.com/45935233/56943158-2ba4e900-6b59-11e9-9e7b-2a21420e9652.png)

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>Hello World!</h1>
    <script>
        // 1.
        let header = Document.querySelector('h1')
        // 2.
        console.log(header.innerText)
        // 3. 
        header.innerText = 'Happy Hacking'
    </script>
</body>
</html> 
```

