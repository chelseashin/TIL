< CSS > 

2019-01-17



inline 레벨 요소 예

span, a, strong, img, br, input, select, textarea, button



##### static

* 기본값

##### relative

* 현재 위치에서 상하좌우 상대적으로 움직일 수 있게 된다.
* position 적용 전(static 일 때) 기준으로 움직임, 움직인 후 원래 있었던 공간이 유지됨.

##### absolute

* 기본 레이어 관계에서 벗어난다.(집나간 자식, 붕 뜬다)
* 즉 다른 도형들도 새로운 자리로 움직이게 된다.
* 움직인 후 원래 있었던 공간이 사라진다.
* 부모 영역을 벗어나 자유롭게 어디든 위치할 수 있다.
* 부모의 static 이외에 position 프로퍼티가 지정되어 있을 경우에만 부모를 기준으로 위치하게 된다.
* 만약 부모, 조상이 모두 static이면 document body를 기준으로 위치하게 된다.

##### fixed

* absolute 랑 동일하게 움직이지만 스크롤이 생길 때 움직이지 않고 고정되어 있다.

> TIP : 부모에게 position:relative를 줘서 자식이 absolute를 받을 때 기준점을 부모로 인식하도록 하는 것이 편하다.