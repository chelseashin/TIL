Homework

대전 2반 17번 신채원

2019-01-31



< SQLite RDBMS >

* 아래 동작을 수행하기 위한 SQL 을 각각 작성하세요.

1. 다음과 같은 스키마를 가지는 DB 테이블 friends 를 생성한다.

![1549501043003](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1549501043003.png)

```sql
CREATE TABLE friends (
id INTEGER PRIMARY KEY,
name TEXT,
location TEXT
);
```



2. 해당 테이블에 다음과 같이 데이터를 입력한다.

   ![1549501237450](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1549501237450.png)

```sql
sqlite> INSERT INTO friends
   ...> VALUES(1, "JUSTIN", "Seoul"), (2, "Simon", "New York"), (3, "Chang", "Las Vegas"),(4, "Chang", "Sydney");
  
sqlite> SELECT * FROM friends;
```



3. 데이터를 다음과 같이 추가한다. (행 추가)

```sql
-- 1. ADD new table
ALTER TABLE friends ADD COLUMN married INTEGER;

-- 2. Rename Table
ALTER TABLE friends
RENAME TO new_table_name;
```



4. married 가 0 인 데이터를 모두 삭제한다. / 테이블을 삭제한다.

```sql
UPDATE friends SET location = "LA", married = 1 WHERE id = 1;
UPDATE friends SET married = 0 WHERE id = 2;
UPDATE friends SET married = 0 WHERE id = 3;
UPDATE friends SET married = 1 WHERE id = 4;

DELETE FROM friends WHERE married = 0;

DROP TABLE friends;
```

