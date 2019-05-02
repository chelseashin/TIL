Homework

대전 2반 17번 신채원

2019-05-01

< JS DOM 조작과 JS 응용 >

1. DOM에서 특정 요소를 선택할 때 document.querySelector() 뿐만 아니라
   document.querySelectorAll() 역시 사용할 수 있다. 둘의 차이를 검색하여 기
   술하시오.

- document.querySelector() : 제일 처음에 등장하는 요소 하나만 리턴 . 없으면 Null이 리턴
- document.querySelectorAll() : 모두 검색해서 배열로 리턴. 없으면 빈 배열이 리턴 



2. JS에서 자주 사용하는 EventListener 들 중 아래와 같은 것들이 있다. 각각 간략하게 어떤 Trigger 를 의미하는지 조사하여 간략하게 기술하시오.
   – click : 마우스 누르는 순간
   – mouseover/mouseout/mousemove :  마우스를 올려놓을 때, 마우스가 벗어날 때, 마우스 움직일 때마다
   – keypress/keydown/keyup : 키를 누르고 있는 동안 계속 발생, 누를 때 발생, 눌렀다 떼는 순간에 발생
   – load : 모든 파일의 다운로드가 완료되었을 때
   – scroll : 스크롤바를 드래그하거나 , 키보드를 위아래로 움직일 때, 스크롤바를 위아래로 움직일 때
   – change : 버튼이 눌리거나 form 구조가 바뀌었을 때.



3. DOM 에 요소를 추가할 때, innerHTML += 의 방법과 appendChild() 함수를 통해 추가하는 방법이 있다. 둘의 차이를 간략하게 기술하시오.

* innerHTML += : 기존 데이터 + 새로운 데이터를 추가하면서 새로 쓰는 느낌, property
* appendChild() : method.