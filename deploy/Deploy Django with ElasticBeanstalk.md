## Deploy Django with EB

> ['https://docs.aws.amazon.com/ko_kr/elasticbeanstalk/latest/dg/create-deploy-python-django.html#python-django-deploy](https://docs.aws.amazon.com/ko_kr/elasticbeanstalk/latest/dg/create-deploy-python-django.html#python-django-deploy)
>
> - 반드시 오류가 없는 프로젝트를 바탕으로 배포 작업을 준비한다.
> - AWS 회원가입을 완료한다.
> - 해당 내용은 프로젝트 내용에 따라서 유동적으로 변경해서 해야 함.

### 0. 코드 준비

`.gitignore` 설정을 확인하고, `pip freeze > requirements.txt` 를 한 후 마지막 커밋을 하자.

**[주의] test_plus, psycopg2 가 requirements.txt 에 있으면 오류 뿜음**

------

### 1. Elastic Beanstalk

Elastic Beanstalk를 사용하면, 애플리케이션을 실행하는 인프라에 대한 염려 없이 AWS 클라우드에서 애플리케이션을 신속하게 배포 및 관리할 수 있습니다. 선택 또는 제어에 대한 제약 없이 Elastic Beanstalk의 관리 복잡성이 줄어듭니다. 애플리케이션을 업로드하기만 하면 에서 용량 프로비저닝, 로드 밸런싱, 조정, 애플리케이션 상태 모니터링에 대한 세부 정보를 자동으로 처리합니다.

```python
$ pip install awsebcli # win, linux, mac with python
$ brew install awsebcli # mac with homebrew
```

------

### 2. AWS 설정

#### 2.1 IAM 설정

- IAM 부여는 이전에 S3 파일 업로드 수업에서 사용자를 만들었다고 가정하고 추가하는 것만 설명합니다.
- 권한 추가

[![1](https://user-images.githubusercontent.com/18046097/57970424-1edb1e80-79bc-11e9-82aa-cc734ba26955.png)](https://user-images.githubusercontent.com/18046097/57970424-1edb1e80-79bc-11e9-82aa-cc734ba26955.png)

- `AWSElasticBeanstalkFullAccess` 추가

[![2](https://user-images.githubusercontent.com/18046097/57970426-269ac300-79bc-11e9-8442-dce6a32bd30a.png)](https://user-images.githubusercontent.com/18046097/57970426-269ac300-79bc-11e9-8442-dce6a32bd30a.png)

- 권한 추가

[![3](https://user-images.githubusercontent.com/18046097/57970428-2b5f7700-79bc-11e9-890a-595fa225eb91.png)](https://user-images.githubusercontent.com/18046097/57970428-2b5f7700-79bc-11e9-890a-595fa225eb91.png)

- 기존의 `KEY` , `SECRET` 활용 : 없으면 생성시 반드시 저장. 다시 못 구함

------

### 2. AWS 계정 설정 추가

```python
$ pip install awscli
$ aws --version
```

- `awscli`가 설치 완료 되었으면 설정 값을 입력하자.

  ```python
  $ aws configure
  AWS Access Key ID: 본인 KEY ID 입력
  AWS Secret Access Key: 본인 Secret Access 입력
  Default region name: ap-northeast-2 # seoul
  Default output format: json
  ```

- 입력된 정보 확인

  ```python
  $ vi ~/.aws/config
  $ vi ~/.aws/credentials
  ```

------

### 3. EB 설정

```python
$ eb init
```

1. Region

   ```python
    Select a default region
    1) us-east-1 : US East (N. Virginia)
    2) us-west-1 : US West (N. California)
    3) us-west-2 : US West (Oregon)
    4) eu-west-1 : EU (Ireland)
    5) eu-central-1 : EU (Frankfurt)
    6) ap-south-1 : Asia Pacific (Mumbai)
    7) ap-southeast-1 : Asia Pacific (Singapore)
    8) ap-southeast-2 : Asia Pacific (Sydney)
    9) ap-northeast-1 : Asia Pacific (Tokyo)
    10) ap-northeast-2 : Asia Pacific (Seoul)
    11) sa-east-1 : South America (Sao Paulo)
    12) cn-north-1 : China (Beijing)
    13) cn-northwest-1 : China (Ningxia)
    14) us-east-2 : US East (Ohio)
    15) ca-central-1 : Canada (Central)
    16) eu-west-2 : EU (London)
    17) eu-west-3 : EU (Paris)
    18) eu-north-1 : EU (Stockholm)
    (default is 3): 10
   ```

2. Application Name

   ```python
    (defualt is "..."): 
   ```

3. 개발 환경

   ```python
    It appears you are using Python. Is this correct? y
   ```

4. python 버전

   ```python
    Select a platform version.
    1) Python 3.6
    2) Python 3.4
    3) Python 3.4 (Preconfigured - Docker)
    4) Python 2.7
    5) Python
    (default is 1): 1
   ```

5. codecommit 사용

   ```python
    Do you wish to continue with CodeCommit? (y/N) (default is n): n
   ```

   - 여기서 codec 오류 나오면 `eb init --debug` 해보면 되는데, 99% `.gitignore` 에 한글 있어서임. `.gitignore` 파일 다시 갈아치우는 것 추천

   - 혹시나 그래도 안된다면, 방법은 `~/.pyenv/versions/[가상환경이름]/lib/python3.6/site-packages/ebcli/objects/sourcecontrol.py` 여기에서 실제로 소스코드 수정하는.. 무식한 방법이 있음.

     > `with open('.gitignore', 'r') as f:` 를 아래와 같이 수정
     >
     > `with open('.gitignore', 'r', encoding="utf-8") as f:`

6. ssh 사용

   ```python
    Do you want to set up SSH for your instances?(Y/n): n
   ```

7. 완료

프로젝트 디렉토리내에 `.elasticbeanstalk/` 자동 생성 완료.

`.gitignore` 에 아래의 정보 추가되어 있음. (직접 추가 NO)

```python
# Elastic Beanstalk Files
.elasticbeanstalk/*
!.elasticbeanstalk/*.cfg.yml
!.elasticbeanstalk/*.global.yml
```

------

### 4. Django 설정

- Django 서버 실행과 관련된 내용을 작성한다.

  ```python
  $ mkdir .ebextensions 
  ```

  ```
  # bash
  # .ebextensions/default.config
  option_settings:
    aws:elasticbeanstalk:application:environment:
      DJANGO_SETTINGS_MODULE: [프로젝트폴더명].settings
    aws:elasticbeanstalk:container:python:
      WSGIPath: [프로젝트폴더명]/wsgi.py
  ```


------

### 5. EB create

> 설정에 3~5분이 걸린다.

```
$ eb create

Enter Environment Name
(default is instagram-dev):
Enter DNS CNAME prefix
(default is instagram-dev):

Select a load balancer type
1) classic
2) application
3) network
(default is 2): 2
Creating application version archive "app-43f7-190512_190916".
Uploading instagram/app-43f7-190512_190916.zip to S3. This may take a while.
Upload Complete.
Environment details for: instagram-dev
  Application name: instagram
  Region: ap-northeast-2
  Deployed Version: app-43f7-190512_190916
  Environment ID: e-b2hcwx3a5q
  Platform: arn:aws:elasticbeanstalk:ap-northeast-2::platform/Python 3.6 running on 64bit Amazon Linux/2.8.3
  Tier: WebServer-Standard-1.0
  CNAME: instagram-dev.ap-northeast-2.elasticbeanstalk.com
  Updated: 2019-05-12 10:09:21.046000+00:00
...
2019-05-12 10:13:16    INFO    Application available at instagram-dev.ap-northeast-2.elasticbeanstalk.com.
2019-05-12 10:13:16    INFO    Successfully launched environment: instagram-dev
```

------

### 6. 환경변수 설정

- 각자 설정한 환경변수에 따라서 등록할 것이 있으면 진행할 것.

  ```
  
  ```

$ eb setenv SECRET_KEY='6s6bt4742aavjhp=tuxwcu_#iff45x#t2qwtm#*sglx28n=^7*' AWS_ACCESS_KEY_ID='AKIAVY4R36G5L127XBYF4' AWS_SECRET_ACCESS_KEY='LYbRs8CJQyk1Stmn2LJiCi32ziZ/xG5yizBrxPs7' ```

- 혹은 aws eb 해당 어플리케이션에 직접 들어가서 `구성 - 소프트웨어 수정- 환경 속성` 에 직접 입력 가능

  ![Screen Shot 2019-05-18 at 10 45 08 PM](https://user-images.githubusercontent.com/18046097/57970622-9ca02980-79be-11e9-93ac-f41e38cf42ed.png)

------

### 7. ALLOWED_HOST 설정

```python
$ eb status
Environment details for: instagram-dev
  Application name: instagram
  Region: ap-northeast-2
  Deployed Version: app-43f7-190512_190916
  Environment ID: e-b2hcwx3a5q
  Platform: arn:aws:elasticbeanstalk:ap-northeast-2::platform/Python 3.6 running on 64bit Amazon Linux/2.8.3
  Tier: WebServer-Standard-1.0
  CNAME: instagram-dev.ap-northeast-2.elasticbeanstalk.com
  Updated: 2019-05-12 10:15:11.725000+00:00
  Status: Ready
  Health: Red
(django-venv)
# settings.py
ALLOWED_HOST = [
	'instagram-dev.ap-northeast-2.elasticbeanstalk.com'
]
```

- 루트로 보여주고 싶은 페이지가 있다면 아래와 같이 설정하자.

  ```python
  path('', views.list)
  ```

```python
$ git add .
$ git commit -m 'ALLOWED_HOT settings'
```

------

### 8. 배포

```python
$ eb deploy
$ eb open
```

------

### 9. 배포 이후 DB 반영 등 명령어 자동화

들어가보면, table이 없다고 한다. `migrate` 가 되지 않았기 때문인데, 아래와 같이 작성하자.

`.ebextensions` 디렉토리에 `XXX.config` 로 파일명을 작성하면 된다.

```python
.ebextensions/migrate.config
container_commands:
  01_migrate:
    command: "python manage.py migrate"
    leader_only: true
  02_chown_sqlitedb:	# 필수
    command: "sudo chown wsgi db.sqlite3"
    leader_only: true
```

그리고 다시 배포

```python
$ git add .
$ git commit -m 'migrate config'
$ eb deploy
```

#### 9.1 DB관련 명령어 추가 - Fixture가 매우 중요하다..!

```python
# .ebextensions/migrate.config
container_commands:
  01_migrate:
    command: "python manage.py migrate"
    leader_only: true
	02_chown_sqlitedb: 
    command: "sudo chown wsgi db.sqlite3"
    leader_only: true
	# 이런식으로 유동적으로 추가가능.
  03_seed:
    command: "python manage.py loaddata example.json"
    leader_only: true
```

------

### 10. admin

> <https://docs.djangoproject.com/en/2.1/howto/custom-management-commands/>
>
> <https://realpython.com/deploying-a-django-app-to-aws-elastic-beanstalk/#configure-eb-create-an-environment>
>
> <http://connorleech.info/blog/deploy-django-to-aws/>

```python
# 관리자 계정 생성
$ python manage.py createsuperuser
# 유저 정보 담긴 json 생성
$ python manage.py dumpdata accounts.User --indent 4 > users.json

# 만들어진 users.json accounts/fixtures 폴더로 이동
# .ebextensions/migrate.config
container_commands:
  01_migrate:
    command: "python manage.py migrate"
    leader_only: true
	02_chown_sqlitedb:
    command: "sudo chown wsgi db.sqlite3"
    leader_only: true
  03_seed:
    command: "python manage.py loaddata seed.json"
    leader_only: true

	# 이런식으로 추가
	04_superuser:
		command: "python manage.py loaddata users.json"
		leader_only: true
```

------

### 11. collectstatic

- admin페이지를 들어가면 css가 적용되지 않은 페이지가 보임

- static파일을 못불러 오기 때문

- `settings.py` 수정

  ```python
  # settings.py
  
  STATIC_URL = '/static/'
  STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
  
  # 얘는 프로젝트마다 선택사항 (없는 경로를 쓰면 deploy 시 에러)
  STATICFILES_DIRS = [
      STATIC_DIR = os.path.join(BASE_DIR, 'static'),
  ]
  ```

- 명령어 수정

  - django에서는 collectstatic 명령어를 사용해서 static 파일을 모아서 특정 폴더에 저장한다
  - 이 특정폴더는 위에서 설정했던 STATIC_ROOT

  ```python
  # .ebextensions/migrate.config
  container_commands:
      01_migrate:
          command: "python manage.py migrate"
          leader_only: true
      02_chown_sqlitedb:
          command: "sudo chown wsgi db.sqlite3"
          leader_only: true
      03_createsuperuser:
          command: "python manage.py loaddata users.json"
          leader_only: true
      04_collectstatic:
      command: "python manage.py collectstatic"
  ```

- 설정파일 수정

  - 슬래시(`/`) 신경쓸 것!!!

  ```python
  # .ebextensions/default.config
  option_settings:
      aws:elasticbeanstalk:application:environment:
          DJANGO_SETTINGS_MODULE: insta.settings
      aws:elasticbeanstalk:container:python:
          WSGIPath: insta/wsgi.py
      aws:elasticbeanstalk:container:python:staticfiles:
      /static/: staticfiles/
  ```

- 배포

  ```python
  $ git add .
  $ git commit -m "update"
  $ eb deploy
  ```

- aws에서 수정

  - **위처럼 작성 후 안된다면** EB 페이지에서 수정
  - 애플리케이션 들어간 후 구성 ⇒ 소프트웨어 수정 클릭
  - 아래 이미지와 같이 경로 추가 후 저장