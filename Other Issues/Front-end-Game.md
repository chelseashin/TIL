## Front-end  Game



장소 : GDG 500 startups



#### 1. 천민호 - 여러분이 Angular를 안해봤다면 살아갈 이유가  더 있는 겁니다.

#### - React

어떤 프레임워크를 쓰면 좋을까 - Vue, Angular, React

리액트의 철학 : 리액트는 우리를 개발자로 바라보고 있다

앱의 상태와 화면의 상태의 동기화는 어떻게 할까요?

- setState 

동기화하는 시점을 개발자에게 맡긴다.



#### - Angular

- 앵귤러의 철학 : 앵귤러는 우리를 사용자로 바라보고 있다

- 앱의 상태와 화면의 상태의 동기화는 어떻게 일어날까?

-> 앱 상태 변화가 일어날 것 같으면 앵귤러가 알아서!





##### 각각의 프레임워크마다 장단점이 있음

- TypeScript
- RxJS : Angular를 하려면 무조건 해야 함.



#### Angular

- Angular : 제약 사항이 많음 . 이미 다 정해져 있음 - 모든 것은 Angular의 뜻대로

- 이를 커버할 장점들 - 제약사항이 많다는 것으 잘못된 길로 빠지는 것을 방지

- Best Practice가 잘 없음

- Angular 자체가 모범사례

- [Angular란]: https://poiemaweb.com/angular-basics

[Angular](https://angular.io/)는 SPA(Single Page Application) 개발을 위한 구글의 오픈소스 자바스크립트 프레임워크이다. 웹 애플리케이션은 물론 모바일 웹, 네이티브 모바일과 데스크탑 애플리케이션까지 프론트엔드 개발에 필요한 대부분의 기능을 갖추고 있다. 정적 타입을 제공하는 TypeScript를 주력 언어로 채택하여 대규모 애플리케이션 개발에 보다 적합한 환경을 제공한다.



#### TypeScript

* 간단하게 빠르게 짤 수 있다
* type이 없는 언어에 type을 만들어 넣는다.
* 10명 이상이 되는 팀에 type이 없다면?



### 그래서  **ANGULAR**는!

- 앞으로의 웹 어플리케이션은 점점 더 복잡해질 것이다.

- 단순 웹 소켓 재연결인데 코드의 파편화가 느껴짐

- 데이터의 흐름을 한 곳에서 조작할 수 있음

- 비동기 스트리밍의 lodash
- 디자인과 기능이 같은데 엔드 포인트만 다르다면?



#### 2. 한재엽(FEDG-프론트엔드 개발 그룹)  - UX 빼면 시체 프런트엔드

React

javascript 진짜 잘하고 싶다....

개발을 하기 위한 도구 -> 환경을 바라본다면?

- 정보량 과다
- 작은 모바일 화면
- 복잡해진 화면
- 문서 그 이상의 매체



#### 프론트엔드의 본질이 바로 : `UX`

1. 성능 최적화
   - 초기 로딩 최적화
   - 빠르다는 느낌을 전달
   - 부드러운 애니메이션
2. SEO/SMO
   * 검색엔진 최적화
   * 소셜미디어 공유 최적화
3. 측정과 개선
   * 사용자는 어떻게 우리 서비스를 사용하는가?(트래킹)
   * 상황에 따라 그 비율을 어떻게 되는가?
   * 이탈률은 어떻게 줄일 수 있는가
     * google analytics 등



#### 3. 서재원 - 푸른중학교

`FRT` : Functional Reactive Programming(함수형 )

- Pure Function
- RP: Reactive Programming
  - 필요에 의해 발명
  - 연산존재(Operator)



#### 4. 나석주 - 프런트엔드 개발끝장내기(feat. Angular)

앵귤러를 사랑하는 리액트 개발자

`Web` 

* 인터넷 상에서 정보를 웹 브라우저로 읽을 수 있는 서비스
* 뛰어난 접근성
* "JavaScript가 세상을 먹어치우고 있다."



`Angular`의 템플릿 문법

* Angular component

* Property & Event BInding
* Change Detection과 별개로 수행
* 성능을 높이고 싶다면 컴포넌트의 Change Detection
* 컴포넌트끼리 어떻게 상태 공유?
  * 간단하게 싱글톤의 인스턴스를 이용
  * 간편하고 쉽게 사용 가능

* 의존성 주입(Dependency Injection)
  * 의존성을 직접 생성하지 않고 프레임워크 대신 생성 및 의존서잉 필요한 클래스에 전달해줌

