Homework

대전 2반 17번 신채원

2019-04-16

< REST API >

1. HTTP 상태 코드에서 200 Ok는 요청에 대해 성공적으로 수행하였음을 나타낸 다. 아래의 HTTP 응답 코드의 의미를 작성하시오.

   ```python
   - 404 - Not Found, 서버가 요청한 페이지(Resource)를 찾을 수 없다. 
   - 405 - 허용되지 않은 메서드 : 요청에 지정된 방법을 사용할 수 없다. 클라이언트가 요청한 리소스에서는 사용불가능한  method를 이용했을 경우 응답하는 코드
   - 500 - (internal server error) : 내부 서버 오류, 서버에 오류가 발생하여 요청을 수행할 수 없다. 
   ```



2.  Django에서 지정된 레코드에 값이 없을 때 404에러를 나타나도록 하는 shortcut은 무엇인가?

   ```python
   from django.shortcuts import get_object_or_404
   ```



3. 아래의 설명 중 REST API 설계 기본 규칙에 어긋난 것은? - **(1)**
   **(1) 자원에 필요한 경우 CRUD 동사 표현이 들어갈 수 있다.** 

   (2) 자원은 대문자보다 소문자를 사용한다. 

   (3) URL에 HTTP Method를 사용하지 않는다.

   (4) 자원간의 연관 관계가 있는 경우 posts/1/comments/ 와 같이 작성한다.

   (5) URL에서 변하는 부분은 posts/<int:post_pk>/ 와 같이 유일한 값이다. 