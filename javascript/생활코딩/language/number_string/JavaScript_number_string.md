## JavaScript - 숫자 /문자



2019-07-01



* 간단한 숫자 연산 - 알림으로 띄우기

```html
<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
	<script type="text/javascript">
		alert(1);
		alert(1+1);
		alert(1.2 + 1.3);
		alert(2 * 4);
		alert(6 / 2);
		document.write("Hello World!")
	</script>
</body>
</html>
```



* 복잡한 숫자 연산 - 숫자를 제어하는 방법

```javascript
Math.pow(3,2);       // 9,   3의 2승 
Math.round(10.6);    // 11,  10.6을 반올림
Math.ceil(10.2);     // 11,  10.2를 올림
Math.floor(10.6);    // 10,  10.6을 내림
Math.sqrt(9);        // 3,   3의 제곱근
Math.random();       // 0부터 1.0 사이의 랜덤한 숫자
```



* 문자

```javascript
alert('coding everybody');
alert('chelsea\'s javascript ')   // escape : 문자로 역할 해제. '' 안에 ' 쓰고 싶을 때는 \(역슬래시)를 써줌

alert(typeof "1")    // 값의 데이터 형을 알려주는 기능 
// 결과 : string
alert(typeof 1)
// 결과 : number

alert("안녕하세요.\n 저는 첼씨입니다.");    // \n는 줄바꿈을 의미
alert("coding"+" everybody");    // 문자와 문자를 더함
// 결과 : coding everybody
alert("coding everybody".length)    // 문자의 길이를 구함
// 결과 : 16
document.write("code".indexOf("d"))
// "code"에서 'd'의 인덱스번호를 알려줌
```

