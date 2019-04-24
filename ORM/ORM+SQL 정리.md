## < SQL / ORM  정리>

2019-04-21



### 1. SQL

##### Database SQL 기초

##### 데이터베이스(DB)

- 데이터베이스는 체계화된 데이터의 모임이다.
- 여러 사람이 공유하고 사용할 목적으로 통합 관리되는 정보의 집합
- 논리적으로 연관된 하나 이상의 자료의 모음으로, 그 내용을 고도로 구조화함으로써 검색과 갱신의 효율화를  꾀한 것이다.
- 즉, 몇 개의 자료 파일을 조직적으로 통합하여 자료 항목의 중복을 없애고 자료를 구조화하여 기억시켜 놓은 자료의 집합체

##### RDBMS(관계형 데이터베이스 관리 시스템)

- 관계형 모델을 기반으로 하는 데이터베이스 관리 시스템
- 대표적인 오픈소스 : RDBMS(MySQL, SQLite, PostgreSQL)과 ORACLE, MSSQL

##### 우리가 사용할 SQLite

- SQLite는 서버가 아닌 응용 프로그램에 넣어 사용하는 비교적 가벼운 DB.
- 구글 안드로이드 운영체제에 기본적으로 탑재된 DB이며, 임베디드 소프트웨어에도 많이 활용되고 있다.
- 로컬에서 간단한 DB구성을 할 수 있으며, 오픈소스 프로젝트이기 때문에 자유롭게 사용할 수 있다.

##### * 스키마

- 데이터베이스에서 자료의 구조, 표현방법, 관계 등을 정의한 구조

- 데이터베이스의 구조와 제약 조건에 관련한 전반적인 명세를 기술한 것

- 열(Column) : 각 열에는 고유한 데이터 형식이 지정된다. 

  * INTEGER, TEXT, NULL 등

- 행(Row) , 레코드 : 테이블의 데이터는 행에 저장된다.

  * 즉, user 테이블에 4행이 있다면 4명의 user 정보가 저장되어 있음.

- PK(기본키) : 각 행(레코드)의 고유 값으로 Primary Key로 불린다.

  - 반드시 설정해야 하며, DB 관리 및 관계 설정 시 주요하게 활용됨


##### 1. SQL 개념

* SQL(Structured Query Language)는 관계형 DB 관리 시스템(RDBMS)의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어이다.

-  관계형 DB 관리 시스템에서 자료의 검색과 관리 DB 스키마 생성과 수정, DB 객체 접근 조정 관리를 위해 고안되었다.



* SQL문법의 3가지 종류
  1. DDL(Data Definition Language) - 데이터 정의 언어
     * 데이터를 정의하기 위한 언어
     * 관계형 DB구조(테이블, 스키마)를 정의하기 위한 명령어
     * ex) CREATE, DROP, ALTER
  2. DML(Data Manipulation Language) - 데이터 조작 언어
     * 데이터를 저장, 수정, 삭제, 조회 등을 하기 위한 언어
     * ex) INSERT, UPDATE, DELETE, SELECT
  3. DCL(Data Control Language) - 데이터 제어 언어
     * DB 사용자의 권한 제어를 위해 사용되는 언어
     * ex)  GRANT, REVOKE, COMMIT, ROLLBACK

##### 2. HELLO, DB

```sql
# 터미널에서 sqlite3 켜기
$ sqlite3
sqlite> .mode csv   -- csv 모드 켜기
sqlite> SELECT * FROM examples; -- examples의 모든 정보 조회
-- SELECT문은 데이터베이스에서 특정한 테이블을 반환한다.
sqlite> .headers on -- 예쁘게 보기
```



##### 3. DB, Table 생성

1. database 생성

```sql
$ sqlite3 database -- 해당 DB파일을 만들고 sqlite에서 확인해 볼 수 있다.
$ sqlite3 tutorial.sqlite3
sqlite> .databases
```



2. Table 생성

```sql
sqlite> CREATE TABLE classmates(
	id INT PRIMARY KEY,
    name TEXT
	);
	-- sql문은 마지막에 ';'을 붙여준다
```



* table과 Database의 관계 - users, movies, movie_rate 등

  * Datatype : SQLite은 동적 데이터 타입, 기본적으로 Affinity에 맞게 들어간다.
    * 종류 : INTEGER, TEXT, REAL, NUMERIC, BLOB

* table 및 schema 조회

  * 테이블 목록 조회 : `.table`

  * 특정 테이블 스키마 조회 : `.schema tablename` 

    ```sql
    sqlite> .tables
    sqlite> .schema classmates
    ```

*  Table 삭제(DROP)

  * 특정 테이블 삭제 : `DROP TABLE tablename`;

    ```sql
    sqlite> DROP TABLE classmates;
    sqlite> .tables
    ```

  ![1555838555301](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1555838555301.png)

  ```sql
  sqlite> CREATE TABLE classmates(
  	id INT PRIMARY KEY,
      name TEXT,
      age INT,
      address TEXT
  	);
  ```



#### 4. 데이터 추가, 읽기, 수정, 삭제(DML)

 1. data 추가(INSERT)

    * 특정 table에 새로운 행을 추가하여 데이터를 추가할 수 있다.

      ```sql
      INSERT INTO table(column1, column2, ...)
      	VALUES(values1, values2, ...);
      ```

    * Q . classmates테이블에 이름이 홍길동이고 나이가 23인 데이터를 넣어보자

      ```sql
      sqlite> INSERT INTO classmates(name, age)
      		VALUES(홍길동, 23);
      ```

    * Q. classmates테이블에 id가2이고, 이름이 홍길동이고, 나이가 30이고, 주소가 서울인데이터를넣어보자

      ```sql
      sqlite> INSERT INTO classmates VALUES (2, '홍길동', 30, '서울');
      ```

      * 모든 열에 데이터를 넣을 때에는 column을 명시할 필요가 없다.
      * 꼭 필요한 정보라면 비워두면 안됨

      * 또한 id는 PK이므로 반드시 필요하며, 값이 저장되면 자동으로 증가하도록 함(unique)



```sql
* 테이블 설정 변경 

sqlite> DROP TABLE classmates;   -- classmate테이블 삭제
sqlite> CREATE TABLE classmate(
	id INTEGER PRIMARY KEY AUTOINCREMENT,    -- INTEGER에서만 사용 가능!
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
	);
```



2. data 가져오기(SELECT)

```sql

  sqlite> SELECT column1, column2 FROM table;
  -- EX)
  sqlite> SELECT id, name FROM classmates;
  
  -- Q. classmates에서 id, name 값을 하나만 가져온다면?
  sqlite> SELECT id, name FROM classmates LIMIT 1;
  
  -- Q. classmates에서 특정 column값을 특정 위치에서부터 몇 개만 가져온다면?
  sqlite> SELECT column1, column2 FROM table LIMIT num OFFSET num;
  -- LIMIT과 OFFSET은 세트!
  
  -- Q. classmates에서 id, name column값을 세번째에 있는 값 하나만 가져온다면
  sqlite> SELECT id, name FROM classmates LIMIT 1 OFFSET 2;
  -- LIMIT : 몇 개 가져오는지, OFFSET : 몇 번째꺼 다음부터 가져오는지
  
  -- Q.classmates에서 id,name column 값 중에 특정한 값만 가져온다면?
  sqlite> SELECT column1, column2 FROM table WHERE column=value;
  
  -- Q. classmates에서 id, name column값 중에 주소가 서울인 사람만 가져온다면?
  sqlite> SELECT id, name FROM classmates WHERE address="서울";
  
  -- Q. classmates에서 특정 column값을 중복 없이 가져온다면?
  sqlite> SELECT DISTINCT column FROM tables;
  
  -- Q. classmates에서 age 값을 중복 없이 가져온다면?
  sqlite> SELECT DISTINCT age FROM classmates;
```


3. data 삭제 (DELETE)

   * 특정 table에 특정한 레코드를 삭제할 수 있다.

     ```sql
     DELETE FROM table WHERE condition;
     
     -- 무슨 기준으로 삭제?
     -- 중복이 불가능한(UNIQUE한) 값인 id를 기준으로 하자!
     sqlite> DELETE FROM classmates WHERE id=3 ;
     ```


4. data 수정(UPDATE)

   * 특정 table에 특정한 레코드를 수정할 수 있다.

     ```sql
     sqlite> UPDATE table SET column1=value1, column2=value2, ...
     		WHERE condition;
     		
     -- Q. classmates 테이블에 id가 4인 레코드를 수정해보자. 
     --   이름을 홍길동으로, 주소를 제주로 바꿔보자
     sqlite> UPDATE classmates
     		SET name="홍길동", address="제주"
     		WHERE id=4;
     ```


![1555842387103](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1555842387103.png)



* WHERE 심화

```sql
sqlite> SELECT * FROM users WHERE age >= 30;
sqlite> SELECT first_name FROM users WHERE age >= 30;
sqlite> SELECT last_name, age FROM users WHERE age >= 30 and last_name="김";
```



* Expressions

```sql
-- 레코드의 갯수 반환 표현식
sqlite> SELECT COUNT(column) FROM table;

-- Q. users 의 총 갯수
sqlite> SELECT COUNT(*) FROM users;

-- Q. AVG(), SUM(), MIN(), MAX()
sqlite> SELECT AVG(column) FROM table;
sqlite> SELECT first_name, MAX(balance) FROM users;
```



* LIKE

   ```sql
     -- 정확한 값에 대한 비교가 아닌, 패턴을 확인하여 해당하는 값을 반환
     sqlite> SELECT * FROM table WHERE column LIKE '';
     -- 2로 시작 : 2%
     -- 2로 끝 : %2
     -- 2가 들어있는 값 : %2%
     -- 아무 값이나 들어가고 두번째가 2로 시작하는 값 : _2%
     -- 1로 시작하고 4자리인 값 : 1___
     -- 2로 시작하고 적어도 3자리인 값 : 2_%_%  /  2__%
     
     sqlite> SELECT * FROM users WHERE age LIKE '2%';
     sqlite> SELECT * FROM users WHERE phone LIKE '02-%';
     sqlite> SELECT * FROM users WHERE name  LIKE '%준';
     sqlite> SELECT * FROM users WHERE phone LIKE '%5114%';
   ```

  

* ORDER(정렬)

   ```
   ​```sql
  SELECT columns FROM table ORDER BY column1, column2 ASC | DESC;
  -- ASC : 오름차순, DESC : 내림차순
  
  sqlite> SELECT * FROM users ORDER BY age ASC LIMIT 10;
  sqlite> SELECT * FROM users ORDER BY age, last_name ASC LIMIT 10;
  sqlite> SELECT name FROM users ORDER BY balance DESC LIMIT 10;
  ```








### 2. ORM

기본 : CRUD

SQL : SELECT / INSERT INTO / UPDATE / DELETE

ORM : READ / CREATE / UPDATE / DELETE



Database를 Code화하여 CRUD하도록 도와주는 언어가 바로 `SQL`!

DB의 행, 테이블 등을 객체로 취급할 수 있다. 



#### ORM(Object-Relational-Mapping)

![1555825858826](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1555825858826.png)

ORM은 DB를 SQL상태로 이를 파이썬 객체로 취급하여 파이썬 코드화하는 매개체



* ORM(Object-Relational-Mapping)을 단순하게 표현하면 객체와 관계와의 설정이라고 할 수 있다. ORM에서 말하는 `객체(Object)`의 의미는 우리가 흔히 알고 있는 OOP(Object_Oriented_Programming, 객체지향 프로그래밍)의 그 객체를 의미한다는 것을 쉽게 유추할 수 있을 것이다. `관계(Relationship)`라는 것은 개발자가 흔히 사용하고 있는 관계형 데이터베이스를 의미한다. 
* 객체형 데이터(JAVA Object)와 관계형 데이터(RDB의 테이블) 사이에서 개념적으로 일치하지 않는 부분을 해결하기 위해 이 둘 사이를 Mapping하는 것을 의미한다. 객체형 데이터와 관계형 데이터의 각 속성들을 매핑할 경우, 관계형 데이터처럼 사용 가능하다.
* 쉽게 말해 SQL문 작성 없이 간단한 매핑 설정으로 데이터 베이스의 테이블 데이터를 JAVA객체로 전달받을 수 있는 것이다. 



#### <장점>

1. 객체 지향적인 코드로 인해 직관적이고 비즈니스 로직에 더 집중할 수 있도록 한다. 
2. 재사용 가능, 유지 보수성이 향상
3. DB에 대한 종속성이 줄어든다.
   * DB schema를 그대로 객체의 class로 mapping하고 별도의 sql문을 사용하지 않고 schema를 디자인 할 수 있으며 query를 단 한줄도 안 써도 DB의 데이터를 추가/수정/삭제가 가능하다. 특정 DB에 한정되지 않기 때문에 나중에 어떤 DB로든 쉽게 migration이 가능하다

#### <단점>

1. 오로지 ORM으로만은 거대한 서비스를 구현하기가 어렵다.
   * 기본적으로 자동으로 생성되는 query를 사용하게 되고, 추후에 속도와 같은 문제가 생기면, 그 부분만 내가 직접 sql을 사용 가능하다. 하지만 이렇게 되면, 시스템이 복잡해질 수록 직접 추가한 sql의 비율이 점점 많아질 것이고, 코드가 점점 복잡해질 수 있다. 특정 쿼리마다 몇 개의 field(column)만 가져오고 싶어도 쉽게 구현하기 힘들고, 기본값은 모든 값을 가져오게 되어, performance에 영향을 준다. 
2. 어느 정도의 속도 저하가 발생할 수 있다. 



* ORM

```sql
-- CREATE
user = User(username = 'chelsea', 
           email = 'example@gmail.com')
           
-- READ
user = Users.query.all()
users = User.query.filter_by(username="chelsea").all()
miss = User.query.filter_by(username="chelsea").first()
user = User.query.get(1)

-- LIKE
user = User.query.filter(User.email.like('%exam%')).all()
user = User.query.limit(1).offset(2).all()   -- 3번째부터 하나 가져옴

-- UPDATE
user = User.query.get(1)
user.username = "ssafy"
db.session.commit()
user.username     -- 수정된 것 확인

-- DELETE
user = User.query.get(1)
db.session.delete(user)
db.session.commit()
```



* models.py

```python
from flask_sqlalchemy import SQLAlchemy

# sqlalchemy 초기화
db = SQLAlchemy()

# sqlalchemy datatype 6가지
# Integer / String(size) / Text / DateTime / Float / Boolean
    
class User(db.Model):
	__tablename__='users'
	id = db.Column(db.Integer, primary_key=True)
	nickname = db.Column(db.String(20), nullable=False)
	address = db.Column(db.String(30), nullable=False)    --빈값으로 두면 안됨
```



* views.py

```python
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# model.py에서 db와 User class불러오기
from models import db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db에 app 연동
db.init_app(app)

# migrate 초기화
migrate = Migrate(app, db)

# 뷰 함수
@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/users/create/') # 후방 슬래쉬 없이 엑세스 하면 슬래쉬가 있는 url로 잡아줌(거의 이 경우를 사용)
def create():
    nickname = request.args.get('nickname')
    address = request.args.get('address')
    # 앞의 nickname은 column name!
    user = User(nickname=nickname, address=address)
    db.session.add(user)
    db.session.commit()
    # url_for은 뷰 함수의 이름을 씀. 그래서 index를 씀
    return redirect(url_for('index'))

@app.route('/users/delete/<int:id>/')
def delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/users/edit/<int:id>')
def edit(id):
    user = User.query.get(id)
    return render_template('edit.html', user=user)

@app.route('/users/update/<int:id>')
def update(id):
    user = User.query.get(id)
    nickname = request.args.get('nickname')
    address = request.args.get('address')
    
    user.nickname = nickname
    user.address = address
    
    db.session.commit()
    
    return redirect(url_for('index'))

# 아래에 위치 - 서버 꺼지지 않도록!
if __name__ == "__main__":
    app.run(host = os.getenv('IP'), port=os.getenv('PORT'), debug = True)
```











