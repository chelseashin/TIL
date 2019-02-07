Workshop

대전 2반 17번 신채원

2019-01-31



< SQLite RDBMS >

1. 

```sql
-- 1. 해당 테이블을 수정하여, 다음과 같이 컬럼을 추가하고, 데이터를 삽입하라.
ALTER TABLE bands ADD COLUMN members INTEGER;

UPDATE bands SET members = 4 WHERE id = 1;
UPDATE bands SET members = 5 WHERE id = 2;
UPDATE bands SET members = 9 WHERE id = 3;

-- 2. Id 가 3인 레코드의 members 를 5로 수정하라.
UPDATE bands SET members = 5 WHERE id = 3;

-- 3. Id 가 2인 레코드를 삭제하라
DELETE FROM bands WHERE id = 2;
```



1. 
2. 