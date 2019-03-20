

### 이미지 경로

```python
(django-venv) chelseashin:~/workspace/PROJECT03 (master) $ pip install Pillow
(django-venv) chelseashin:~/workspace/PROJECT03 (master) $ python manage.py makemigrations
Migrations for 'boards':
  boards/migrations/0003_board_image.py
    - Add field image to board
(django-venv) chelseashin:~/workspace/PROJECT03 (master) $ python manage.py showmigrations
# 모델 변경 확인
$ python manage.py showmigrations
# 저장
$ python manage.py migrate

$ python manage.py sqlmigrate boards 0003
BEGIN;
--
-- Add field image to board
--
ALTER TABLE "boards_board" RENAME TO "boards_board__old";
CREATE TABLE "boards_board" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "image" varchar(100) NOT NULL, "title" varchar(10) NOT NULL, "content" text NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL);
INSERT INTO "boards_board" ("id", "title", "content", "created_at", "updated_at", "image") SELECT "id", "title", "content", "created_at", "updated_at", '' FROM "boards_board__old";
DROP TABLE "boards_board__old";
COMMIT;
```





#### 이미지 확인

```python
$ python manage.py shell_plus
>>> board = Board.objects.get(pk=16)
>>> board.image
<ImageFieldFile: porto.jpg>
>>> board.image.url
'/media/porto.jpg'
>>> board.image.name
'porto.jpg'
```



#### 이미지 크기를 맞추어 받기

```python
$ pip install pilkit
$ pip install django-imagekit
```



#### 이미지 조정

