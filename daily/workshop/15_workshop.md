Workshop

대전 2반 17번 신채원

2019-01-30



< Database & SQL >

1.  아래 표와 같은 스키마를 가진 DB 테이블을 생성하고, 아래와 같이 Data 를 입력해 봅 시다.

![1549499982686](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1549499982686.png)

```sql
sqlite> CREATE TABLE bands (
   ...> id INTEGER PRIMARY KEY AUTOINCREMENT,
   ...> name TEXT,
   ...> debut INTEGER
   ...> );
sqlite> .tables
bands
```

```sql
sqlite> INSERT INTO bands (id, name, debut)
   ...> VALUES(1, "Queen", 1973);                                                    
sqlite> INSERT INTO bands (id, name, debut)
   ...> VALUES(2, "Coldplay", 1998);
sqlite> INSERT INTO bands (id, name, debut)
   ...> VALUES(3, "MCR", 2001);
sqlite> SELECT * FROM bands;
1|Queen|1973
2|Coldplay|1998
3|MCR|2001

# 한번에 삽입하기
sqlite> INSERT INTO bands(name, debut)
   ...> VALUES('Queen', 1973), ('Coldplay', 1998), ('MCR', 2001);
```





2. bands 테이블에서 모든 데이터 레코드의 id 와 name 만 조회하는 Query 를 작성하라.

```sql
sqlite> SELECT id, name FROM bands;
1|Queen
2|Coldplay
3|MCR
```



3.  bands 테이블에서 debut 가 2000 보다 작은 밴드들의 이름만을 조회하는 Query 를 작성하라.

```sql
sqlite> SELECT name FROM bands WHERE debut < 2000;
Queen
Coldplay
```

