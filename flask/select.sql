-- 조회
-- 테이블 값 모두 가져오기
SELECT * FROM classmate;

-- 테이블의 특정 column만 가져오기(id, name)
SELECT id, name FROM classmate;

-- 상위 2줄만 가져오기(특정 row 개수 지정해 가져오기)
SELECT id, name FROM classmate LIMIT 2;

-- LIMIT와 OFFSET이 set!
-- 가져오는 row(레코드)의 시작점 지정(OFFSET)
SELECT * FROM classmate LIMIT 1 OFFSET 2;

-- 특정한 값을 가진 row만 조회하기
SELECT * FROM classmate WHERE address = '서울';
SELECT * FROM classmate WHERE id=2;

-- 서울에 사는 사람만 조회하기
SELECT name FROM classmate WHERE address='서울';

