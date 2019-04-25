Homework

대전 2반 17번 신채원

2019-04-11

< 데이터베이스 시딩 >

1. Django에서 모델의 기초 데이터베이스의 값을 제공하기 위해서는 Fixtures를 사용한다. 해당 파일은 기본적으로 각각의 app에 fixtures폴더를 있어야 하며, 파일 형식은  [     A     ]이거나 [      B      ]이다.

> A : json
>
> B : yaml



2. 워크샵처럼 실제 Django에 데이터가 저장되어 있을 때, 아래의 fixtures파일을 만들고자 한다. 사용해야 하는 명령어를 작성하라

![image](https://user-images.githubusercontent.com/45935233/56711392-860f0580-6765-11e9-9f17-2215ebe40f96.png)

```python
# 터미널 명령어
기본 설치 명령어 : $ pip install pyyaml
# 변환 명령어
$ python manage.py dumpdata myapps.person --format yaml > final.yaml
```

> 결과

```yaml
[
  {
    "model": "myapps.person",
    "pk": 1,
    "fields": {
      "first_name": "John",
      "last_name": "Lennon"
    }
  },
  {
    "model": "myapps.person",
    "pk": 2,
    "fields": {
      "first_name": "Paul",
      "last_name": "McCartney"
    }
  }
]
```

