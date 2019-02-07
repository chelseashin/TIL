-- CREATE
INSERT INTO users (username, email)
VALUES ('chelsea', 'chaewonshin95@gmail.com');

user = User(username = 'chelsea',
            email = 'chaewonshin95@gmail.com')
            
-- READ
SELECT * FROM users;
users = Users.query.all()

SELECT * FROM users WHERE username="chelsea";
users = User.query.filter_by(username="chelsea").all()

SELECT * FROM users WHERE username="chelsea" LIMIT 1;
miss = User.query.filter_by(username='ssafy').first()

-- Get one by id
-- PK만 get으로 가져올 수 있음
SELECT * FROM users WHERE id=1;
user = User.query.get(1)

-- LIKE
users = User.query.filter(User.email.like('%exam%')).all()
users = User.query.limit(1).offset(2).all()  -- 세번째부터 하나 가져옴

-- UPDATE
user = User.query.get(1)
user.username = 'ssafy'
db.session.commit()
user.username

-- DELETE
user = User.query.get(1)
db.session.delete(user)
db.session.commit()