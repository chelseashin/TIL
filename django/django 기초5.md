

< DJANGO 05 >

19.03.14

```python
from pprint import pprint

# Create your views here.
def index(request):
    pprint(request)
    pprint(type(request))
    # 객체가 가지고 있는 메서드들
    pprint(dir(request))
    pprint(request.scheme)
    pprint(request.get_host())
    # 경로
    pprint(request.get_full_path())
    # 전체 uri 보기
    pprint(request.build_absolute_uri())
    # 메타 정보 보기
    pprint(request.META)
    # request 방식 보기 - get
    pprint(request.method)
```



* 장고 extensions

```python
INSTALLED_APPS = [
    'boards.apps.BoardsConfig',
    'django_extensions',
    'django.contrib.admin',
```



* 명령어

```python
$ python manage.py show_urls
```



## on_delete

: 참조하는 부모객체가 사라졌을 때, 부모에 딸려있는 자식들을 어떻게 처리할지 정의한다.

데이터베이스 무결성 : 

1. 개체 무결성 제약  : PK - not null, unique
   - 식별자는 Null일 수 없고 중복일 수 없다.



2. 참조 무결성 : FK / 모든 외래키의 값은 2 가지 상태 가운데 하나에만 속함을 규정
3. 범위 / 도메인 무결성 : 컬럼은 지정된 형식을 반드시 만족해야 된다. (CHAR, TEXT)



## on_delete 속성값

1. `CASCADE` : 부모 객체가 삭제 됐을 경우, 이를 참조하는 객체도 삭제한다. 

2. `PROTECT` : 참조가 되어있는 경우,  삭제 오류발생.
3. `SET_NULL` : 부모 객체가 삭제 됐을 경우, 참조하는 모든 값을 NULL로 치환(NOT NULL 조건시 불가능)
4. `SET_DEFAULT` : 모든 값이 DEFAULT로 치환
5. `SET()` : 특정 함수 호출
6. `DO_NOTHING` : 아무것도 하지 않음. 다만 SQL에서는 on_delete 직접 설정해줘야 함.

* ##### boards_comment 테이블의 모습

| id   | content | creqted_at | updated_at | board_id |
| ---- | ------- | ---------- | ---------- | -------- |
| 1    | aa      | .          | .          | ?        |





* migration

```python
* 모델 저장 후
(django-venv) chelseashin:~/workspace/PROJECT03 (master) $ python manage.py makemigrations
Migrations for 'boards':
  boards/migrations/0002_comment.py
    - Create model Comment
(django-venv) chelseashin:~/workspace/PROJECT03 (master) $ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, boards, contenttypes, sessions
Running migrations:
  Applying boards.0002_comment... OK
(django-venv) chelseashin:~/workspace/PROJECT03 (master) $ python manage.py showmigrations
admin
 [X] 0001_initial
 [X] 0002_logentry_remove_auto_add
 [X] 0003_logentry_add_action_flag_choices
auth
 [X] 0001_initial
 [X] 0002_alter_permission_name_max_length
 [X] 0003_alter_user_email_max_length
 [X] 0004_alter_user_username_opts
 [X] 0005_alter_user_last_login_null
 [X] 0006_require_contenttypes_0002
 [X] 0007_alter_validators_add_error_messages
 [X] 0008_alter_user_username_max_length
 [X] 0009_alter_user_last_name_max_length
boards
 [X] 0001_initial
 [X] 0002_comment
contenttypes
 [X] 0001_initial
 [X] 0002_remove_content_type_name
sessions
 [X] 0001_initial
    
(django-venv) chelseashin:~/workspace/PROJECT03 (master) $ python manage.py sqlmigrate boards 0002
BEGIN;
--
-- Create model Comment
--
CREATE TABLE "boards_comment" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content" varchar(200) NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "board_id" integer NOT NULL REFERENCES "boards_board" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "boards_comment_board_id_76b617ec" ON "boards_comment" ("board_id");
COMMIT;
```



* sqlite3에서 모델 확인

```python
(django-venv) chelseashin:~/workspace/PROJECT03 (master) $ sqlite3 db.sqlite3
SQLite version 3.8.2 2013-12-06 14:53:30
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> .tables
auth_group                  boards_board              
auth_group_permissions      boards_comment            
auth_permission             django_admin_log          
auth_user                   django_content_type       
auth_user_groups            django_migrations         
auth_user_user_permissions  django_session 

# schema 확인
sqlite> .schema

# 나가기
sqlite> .exit
```



* terminal

```python
(django-venv) chelseashin:~/workspace/PROJECT03 (master) $ python manage.py shell_plus
    
>>> board = Board.objects.get(pk=10)
>>> board
<Board: 10: 아>
>>> comment = Comment()
>>> comment.content = 'first comment'
>>> comment.board = board
>>> comment.save()
>>> comment.pk
1
>>> comment.content
'first comment'
>>> comment.board
<Board: 10: 아>
>>> comment = Comment(board=board, content='second commit')
>>> comment.save()
>>> comment.pk
2
# 가지고 있는 모든 댓글 가져오기
>>> board = Board.objects.get(pk=10)
>>> board.comment_set.all()
<QuerySet [<Comment: first comment>, <Comment: second commit>]>
>>> comment = Comment.objects.get(pk=1)
>>> comment.board.pk
10
>>> exit()\
... exit()
  File "<console>", line 2
    exit()
       ^
SyntaxError: invalid syntax
>>> exit()
```

