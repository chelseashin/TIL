# 월말평가 모의고사

### 1. 사전 준비 사항

1. 시스템 환경

   - Python 3.6.x

     ```bash
     $ python -V
     ```

   - Django 2.1.x

     ```bash
     $ pip list
     ```

2. `모의고사 ` 프로젝트 폴더 구조

   ```
   ├── accounts
   │   ├── __init__.py
   │   ├── __pycache__
   │   │   ├── __init__.cpython-36.pyc
   │   │   ├── admin.cpython-36.pyc
   │   │   ├── apps.cpython-36.pyc
   │   │   ├── forms.cpython-36.pyc
   │   │   ├── models.cpython-36.pyc
   │   │   ├── urls.cpython-36.pyc
   │   │   └── views.cpython-36.pyc
   │   ├── admin.py
   │   ├── apps.py
   │   ├── forms.py
   │   ├── migrations
   │   │   ├── __init__.py
   │   │   └── __pycache__
   │   │       └── __init__.cpython-36.pyc
   │   ├── models.py
   │   ├── templates
   │   │   └── accounts
   │   │       └── form.html
   │   ├── tests.py
   │   ├── urls.py
   │   └── views.py
   ├── db.sqlite3
   ├── manage.py
   ├── posts
   │   ├── __init__.py
   │   ├── __pycache__
   │   │   ├── __init__.cpython-36.pyc
   │   │   ├── admin.cpython-36.pyc
   │   │   ├── apps.cpython-36.pyc
   │   │   ├── forms.cpython-36.pyc
   │   │   ├── models.cpython-36.pyc
   │   │   ├── urls.cpython-36.pyc
   │   │   └── views.cpython-36.pyc
   │   ├── admin.py
   │   ├── apps.py
   │   ├── forms.py
   │   ├── migrations
   │   │   ├── 0001_initial.py
   │   │   ├── 0002_post_like_users.py
   │   │   ├── __init__.py
   │   │   └── __pycache__
   │   │       ├── 0001_initial.cpython-36.pyc
   │   │       ├── 0002_post_like_users.cpython-36.pyc
   │   │       └── __init__.cpython-36.pyc
   │   ├── models.py
   │   ├── templates
   │   │   └── posts
   │   │       ├── form.html
   │   │       └── list.html
   │   ├── tests.py
   │   ├── urls.py
   │   └── views.py
   └── test_study
       ├── __init__.py
       ├── __pycache__
       │   ├── __init__.cpython-36.pyc
       │   ├── settings.cpython-36.pyc
       │   ├── urls.cpython-36.pyc
       │   └── wsgi.cpython-36.pyc
       ├── settings.py
       ├── templates
       │   └── base.html
       ├── urls.py
       └── wsgi.py
   
   15 directories, 52 files
   ```

3. 프로젝트 기능사항

   - User의 회원가입, 로그인, 로그아웃이 가능합니다.
     - 기본 계정 없음
   - Post의 Create, Read, Update, Delete가 가능합니다.
     Post 데이터베이스 생성/수정/삭제 동작의 경우 모두 POST 요청으로 동작합니다.
     Post읽기(목록 및 상세보기), 생성/수정을 위한 Form 제공은 GET 요청으로 동작합니다.
   - About은 데이터베이스는 존재하지 않습니다.
   - Django Project
     Article과 Comment 모델에 저장된 날짜들은 **KST(Korea Standard Time)**으로 보여집니다.
     Django Project 설정은 **한국어**입니다.

4. 프로젝트 내 데이터베이스 모델링

5. 주의 사항

   - 주어진 내용을 제외한 어떠한 문서나 소스코드도 참고할 수 없습니다.
   - 감독관에게 해당 문제에 관련된 오류를 직접적으로 질문하거나 할 수 없습니다.
   - 감독관이 자러 가기 전까지 제출해야 합니다.
   - 단계별로 디버깅을 해결하지 못하고 넘어갈 수는 있으나 내일 시험에서 틀리는건 당신입니다.



## 2. 단계

#### 1. 서버 실행 및 환경 설정

- 프로젝트 기능사항의 Django Project 부분의 설정 사항을 확인하시고, 서버를 실행 하세요.



## * signup, login은 form.html 으로 통합되어있습니다.

## * 각각 url_name 으로 접근할때 각 페이지 상단에 해당 url_name이 표출되도록 하십시오.

## * form.html 경로는 임의로 변경하거나 추가로 생성할 수 없습니다.

#### 2. Sign Up 페이지

- `/accounts/signup/` 페이지를 생성하십시오.

- 아래 이미지와 같이 보이면 됩니다.

  ![image](https://user-images.githubusercontent.com/45934087/56739015-c643a780-67a8-11e9-9adb-596322fdb8dc.png)

#### 3. Sign In 페이지

- `/accounts/login/` 페이지를 생성하십시오.

- 아래 이미지와 같이 보이면 됩니다.

  ![image](https://user-images.githubusercontent.com/45934087/56739079-e1aeb280-67a8-11e9-8c25-c814e33d6478.png)

## * create, edit 은 form.html 으로 통합되어있습니다.

## * 각각 url_name 으로 접근할때 각 페이지 상단에 해당 url_name이 표출되도록 하십시오.



#### 4. Post List 페이지(전체 목록)

- `/posts/list/` 로 들어가면 게시글 목록이 보이지 않습니다.

- 아래 이미지와 같이 보일 수 있도록 수정하세요.

- 데이터베이스에는 동일하게 값이 들어 있습니다. (값을 추가할 필요는 없습니다.)

- 현재 로그인 된 유저의 이름이 표출됩니다.

- 현재 로그인 된 상태라면 **로그아웃**만 출력됩니다.

- 현재 로그인 된 상태가 아니라면 **로그인**과 **회원가입**이 출력됩니다.

- 각 게시글에 대한 좋아요 버튼이 존재하고

- 현재 좋아요를 누른상태라면 `unlike` 가 표출되며, 누를시 좋아요가 감소합니다.

- 좋아요를 누르지 않은 상태라면 `like` 가 표출되며, 누를시 좋아요가 증가합니다.

- 게시글에 **좋아요를 누른 유저**가 모두 표출되게 하십시오. (for 문)

  ![image](https://user-images.githubusercontent.com/45934087/56739940-dc526780-67aa-11e9-8c65-ee4b9c72d4aa.png)

#### 5. Post 생성

- `/accounts/signup/` 에서 회원가입을 한 이후 **로그인** 됨을 확인하세요.
- `posts/forms.py`에 제목과 내용을 `fields`로 하는 **PostForm**을 활용하십시오.
- `reate` 뷰 함수가 없습니다. 로그인 상태일 때만 생성 할수 있도록 만드십시오.
- `/posts/create/` 에서 새로운 글을 작성하세요.
- **본인**이 작성한 글에만 **수정 버튼** 과 **삭제 버튼**이 생성되도록 하세요.



#### 6. Post 수정

- `edit` 뷰 함수가 없습니다. 로그인 상태일 때만 수정 할수 있도록 만드십시오.
- `GET /posts/edit/` 으로 접근시 로그인 화면으로 이동하도록 하십시오.
- 수정 버튼을 눌러 글을 수정 할 수 있도록 해주십시오.



#### 7. Post 삭제

- `delete` 뷰 함수가 없습니다. 로그인 상태일 때만 삭제 할수 있도록 만드십시오.
- `GET /posts/delete/` 으로 접근시 로그인 화면으로 이동하도록 하십시오.
- `POST /posts/delete/` 방식으로만 삭제 할 수 있도록 하십시오.



#### 8. 게시글 좋아요

- `like_post` 뷰 함수가 없습니다. 로그인 상태일 때만 생성 할수 있도록 만드십시오.

- `GET /posts/like_post/` 으로 접근시 로그인 화면으로 이동하도록 하십시오.


#### 9. 로그아웃

- 수고하셨습니다. 마지막으로 로그아웃을 생성하고 로그아웃 해주세요. `accounts/logout`
- 로그인 된 상태가 아닐때 `GET /accounts/logout/`으로 접근시 로그인 화면으로 이동합니다.