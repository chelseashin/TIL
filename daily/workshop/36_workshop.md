Workshop

대전 2반 17번 신채원

2019-05-01

< JS DOM 조작과 JS 응용 >

* 아래 Instruction 에 따라 JS 코드를 작성해 보자.



```html
<body>
    <button id="change-btn">클릭</button>
    <script>
    	// #change-btn을 button 변수에 할당
        const button = document.querySelector('#change-btn')
        // h1태그를 header 상수에 할당
        const header = document.querySelector('h1')
        // clickCount 변수를 0으로 초기화한다
        let clickCount = 0
        // button에 클릭 이벤트를 추가한다
        button.addEventListener('click', event => {
            //clickCount가 1씩 증가
            clickCount += 1 // ClickCount ++
            
            // header 안의 내용을 clickCount 숫자로 바꾼다.
            header.innerTEXT = clickCount
        })
    </script>
</body>
```

