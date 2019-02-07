2019.02.01

< Datebase & SQL >



* user 테이블 생성

```sql
CREATE TABLE users (
id INTEGER PRIMARY KEY AUTOINCREMENT,  # 자동으로 1, 2, 3, ... 순으로 채워주는 것
first_name TEXT,
last_name TEXT,
age INTEGER,
country TEXT,
phone TEXT,
balance INTEGER
);
```



* 기초

```sql
-- classmate 테이블 확인 
sqlite> .tables
classmate

-- sqlite3 열기
sqlite> .open tutorial.sqlite3
sqlite> .database
seq  name             file                                                      

------

0    main             /home/ubuntu/workspace/tutorial.sqlite3                   
sqlite> .databases
seq  name             file                                                      

------

0    main             /home/ubuntu/workspace/tutorial.sqlite3 

-- 전체 데이터 보기
sqlite> SELECT * FROM classmate;
id          name          age         address   

------

1           보라돌이  25          대전    
2           나나        23          서울    
4           뚜비        23          제주   

-- age 데이터만 보기
sqlite> SELECT age FROM classmate;

-- age       

25        
23        
23        

-- 중복값 제거 : DISTINCT
sqlite> SELECT DISTINCT age FROM classmate;

-- age       

25        
23        

sqlite>  .headers on
sqlite> .mode column
sqlite> .mode csv
sqlite> .import users.csv users
sqlite> .table
classmate  users   

-- SCHEMA 생성
sqlite> .schema users
CREATE TABLE users(
  "id" TEXT,
  "first_name" TEXT,
  "last_name" TEXT,
  "age" TEXT,
  "country" TEXT,
  "phone" TEXT,
  "balance" TEXT
);

-- 테이블 삭제
sqlite> DROP TABLE users;
sqlite> .table
classmate

-- 새로 sql파일 불러오기
sqlite> .read create_users.sql

-- 조건을 주어 데이터 조회
sqlite> SELECT second_name, age  FROM users WHERE age >=30 and second_name = "김";

-- 총 인원 수
sqlite> SELECT COUNT(*) FROM users;

-- 평균 나이
sqlite> SELECT AVG(age) FROM users WHERE age >= 30;

sqlite> SELECT First_name, MAX(balance) FROM users;
first_name, MAX(balance)
"순옥",1000000

-- 평균 계좌잔액
sqlite> SELECT AVG(balance) FROM users WHERE age >= 30;                                
AVG(balance)
153541.425120773

-- 나이가 20대인 사람 조회 (맨 앞자리 수가 2로 시작하는 나이의 모든 사람을 뽑아옴)
sqlite> SELECT * FROM users WHERE age LIKE '2%' ; 

-- 전화번호 02- 로 시작하는 사람 조회
sqlite> SELECT * FROM users WHERE phone LIKE '02-%';

-- 이름이 준 으로 끝나는 사람 조회
sqlite> SELECT * FROM users WHERE first_name LIKE '%준';

sqlite> SELECT * FROM users WHERE phone LIKE "%2407%";
id,first_name,second_name,age,country,phone,balance
580,"현준","윤",31,"경상남도",010-2407-7369,740

-- 오름차순으로 상위 10개 뽑기!
sqlite> SELECT * FROM users ORDER BY age ASC LIMIT 10;

-- 계좌 잔액순으로 내림차순 정렬하여 해당하는 사람의 성과 이름을 10개 뽑기
sqlite> SELECT second_name, first_name FROM users ORDER BY balance DESC LIMIT 10;      second_name,first_name
"김","순옥"
"우","상철"
"민","진호"
"이","재호"
"강","민준"
"황","은정"
"김","영수"
"허","정남"
"김","선영"
"문","미영"

-- 테이블 삭제하고 
sqlite> DROP TABLE users;
sqlite> .tables
classmate

-- 새로 sql 파일 불러오기
sqlite> .read create_users.sql

-- 존재하는 테이블 확인
sqlite> .tables
classmate  users

-- schema 확인
sqlite> .schema users
CREATE TABLE users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
first_name TEXT,
last_name TEXT,
age INTEGER,
country TEXT,
phone TEXT,
balance INTEGER
);
```



```sql
# database SQL 기초

- File 보다 안전하고 편리하고 빠르게 자료를 보관하기 위해 이용한다.
- SQLite를 사용할 예정, C9에는 자동내장되어있음

-- 기본 용어 정리

-- 1. schema (틀) 생성
-- schema는 테이블의 틀을 만드는 것으로 속성을 기본으로 함

| colume | datatype |
| ------ | -------- |
|        |          |

- 데이터 베이스의 구조와 제약조건에 관련된 전반적인 명세를 기술한 것.

- PK(기본키) : Primary Key. 각 행, 레코드의 고유값으로 반드시 설정하여야 하며 데이터 베이스 관리 매치 관계 설정시 유용하게 사용된다. 절대 겹치면 안된다.

-- 2. SQL개념
1. DDL :데이터를 정의하기 위한 언어(테이블, 스키마)
2. DML : 데이터를 저장, 수정, 삭제, 조회등을 하기 위한 언어
3. DCL : 데이터 베이스 사용자의 권한제어를 위해 사용되는 언어

-- 3. Hello SQL : table 만들기
-- sqlite 켜기 
chelseashin:~/workspace $ sqlite3
SQLite version 3.8.2 2013-12-06 14:53:30
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
-- mode 변경
sqlite> .mode csv
sqlite> .headers on
sqlite> .mode column
-- csv 파일 불러오기
sqlite> .import hellodb.csv examples
-- 현재 생성된 테이블 보기
sqlite> .tables
examples

-- 전체 데이터 보기
sqlite> SELECT * FROM examples;
1,"길동","홍",600,"충청도",010-2424-1232

sqlite> SELECT * FROM examples;                                                                 
id          first_name  last_name   age         country     phone        
----------  ----------  ----------  ----------  ----------  -------------
1           길동      홍         600         충청도   010-2424-1232

-- sqlite에서 나가기
sqlite> .exit
```



```sql
-- Database 만들기
chelsea:~/workspace $ sqlite3 tutorial.sqlite3
SQLite version 3.8.2 2013-12-06 14:53:30
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> .databases
seq  name             file
---  ---------------  ----------------------------------------------------------
0    main             /home/ubuntu/workspace/tutorial.sqlite3

-- table 생성
sqlite> CREATE TABLE classmates (
   ...> id INT PRIMARY KEY,
   ...> name TEXT
   ...> );
sqlite> .tables
classmates

sqlite> .schema classmates
CREATE TABLE classmates (
id INT PRIMARY KEY,
name TEXT
);
-- table DROP
sqlite> DROP TABLE classmates;
sqlite> .tables
sqlite> .database
seq  name             file
---  ---------------  ----------------------------------------------------------
0    main             /home/ubuntu/workspace/tutorial.sqlite3
1    temp

-- table 새로 생성
sqlite> CREATE TABLE classmate (
   ...> id INT PRIMARY KEY,
   ...> name TEXT,
   ...> age INT,
   ...> address TEXT
   ...> );
sqlite> .tables
classmate

-- 전체 데이터 확인
sqlite> SELECT * FROM classmate;
sqlite> .read class_table.sql
sqlite> .tables
classmate

sqlite> .schema classmates
sqlite> .headers on
sqlite> .mode column
sqlite> .read insert.sql

sqlite> SELECT * FROM classmate;
id          name        age         address
----------  ----------  ----------  ----------
            홍길동   23
sqlite> .read insert.sql

Error: incomplete SQL: INSERT INTO classmate (id, name, age, address)
VALUES(2, '홍길동', 30, '서울')
sqlite> .read insert.sql

sqlite> SELECT
   ...> * FROM classmate
   ...> ;
id          name        age         address
----------  ----------  ----------  ----------
            홍길동   23
2           홍길동   30          서울
sqlite> DROP TABLE classmate;
sqlite> .tables
sqlite> .table
sqlite> .read create_table.sql

sqlite> .read create_table.sql
Error: near line 1: table classmate already exists

sqlite> .read insert.sql
VALUES('신채원', 15)
INSERT INTO classmate (name, age)
VALUES('박수현', 5)
sqlite> SELECT * FROM classmate;

sqlite> .read insert.sql

sqlite> SELECT * FROM classmate;
id          name        age         address
----------  ----------  ----------  ----------
1           안상현   43          대전
2           신채원   15          서울
sqlite> .read insert.sql

sqlite> SELECT * FROM classmate;
id          name        age         address
----------  ----------  ----------  ----------
1           안상현   43          대전
2           신채원   15          서울
3           안상현   43          대전
4           신채원   15          서울

sqlite> SELECT id, name FROM classmate;
id          name
----------  ----------
1           안상현
2           신채원
3           안상현
4           신채원

sqlite> SELECT id, name FROM classmate LIMIT 2;
id          name
----------  ----------
1           안상현
2           신채원

-- offset은 해당 행부터 LIMIT개 행만큼 출력
sqlite> SELECT * FROM classmate LIMIT 1 OFFSET 2;
id          name        age         address
----------  ----------  ----------  ----------
3           안상현   43          대전

sqlite> SELECT * FROM classmate WHERE address='서울';
id          name        age         address
----------  ----------  ----------  ----------
2           신채원   15          서울
4           신채원   15          서울

sqlite> SELECT * FROM classmate WHERE id=2;
id          name        age         address
----------  ----------  ----------  ----------
2           신채원   15          서울

sqlite> SELECT name FROM classmate WHERE address='서울';
name
----------
신채원
신채원
sqlite> .read delete.sql

sqlite> SELECT * FROM classmate;
id          name        age         address
----------  ----------  ----------  ----------
1           안상현   43          대전
2           신채원   15          서울
4           신채원   15          서울
sqlite> .read update.sql

sqlite> SELECT * FROM classmate;
id          name        age         address   
----------  ----------  ----------  ----------
1           안상현   43          대전    
2           신채원   15          서울    
4           강예원   15          제주    
sqlite> .read update.sql                                                                         
sqlite> SELECT * FROM classmate;
id          name        age         address   
----------  ----------  ----------  ----------
1           안상현   43          대전    
2           신채원   15          서울    
4           박성주   15          제주    
```

