2019.04.16



* model_review
* 새롭게 만들기 - 1:N 관계

```python
chelseashin:~/workspace $ mkdir model_review
chelseashin:~/workspace $ cd model_review/
chelseashin:~/workspace/model_review $ pyenv local insta-venv
(insta-venv) chelseashin:~/workspace/model_review $ django-admin startproject model_review .
(insta-venv) chelseashin:~/workspace/model_review $ python manage.py startapp onetomany
    # settings.py에 앱 등록하기
(insta-venv) chelseashin:~/workspace/model_review $ python manage.py makemigrations
(insta-venv) chelseashin:~/workspace/model_review $ python manage.py migrate
    
$ pip install ipython
$ pip install django_extentsions
(insta-venv) chelseashin:~/workspace/model_review $ python manage.py shell_plus
    >
    
In [1]: user1 = User.objects.create(name='kim')                                       
In [2]: user2 = User.objects.create(name='lee')                                       
In [3]: post1 = Post.objects.create(title='1글', user=user1)                           
In [4]: post2 = Post.objects.create(title='2글', user=user1)                           
In [5]: post3 = Post.objects.create(title='3글', user=user2)                           
In [6]: c1 = Comment.objects.create(content='1글1댓글', user=user1, post=post1)       
In [7]: c2 = Comment.objects.create(content='1글2댓글', user=user2, post=post1)       
In [8]: c3 = Comment.objects.create(content='1글3댓글', user=user1, post=post1)       
In [9]: c4 = Comment.objects.create(content='1글4댓글', user=user2, post=post1)       
In [10]: c5 = Comment.objects.create(content='2글1댓글', user=user1, post=post2)       
In [11]: c6 = Comment.objects.create(content='!1글5댓글', user=user2, post=post1)     
In [12]: c7 = Comment.objects.create(content='!1글6댓글', user=user2, post=post2)     
In [13]: user1.post_set.all()                                                         
Out[13]: <QuerySet [<Post: Post object (1)>, <Post: Post object (2)>]>
In [14]: for post in user1.post_set.all(): 
    ...:         for comment in post.comment_set.all(): 
    ...:                     print(comment.content) 
    ...:                                                                                                
1글1댓글
1글2댓글
1글3댓글
1글4댓글
!1글5댓글
2글1댓글
!1글6댓글

In [15]: c2.user                                                                       
Out[15]: <User: User object (2)>

In [16]: c2.user.post_set.all()                                                       
Out[16]: <QuerySet [<Post: Post object (3)>]>

In [17]: post1.comment_set.first().user.name                                           
Out[17]: 'kim'

In [18]: post1.comment_set.all()[0].user.name                                         
Out[18]: 'kim'

In [19]: post1.comment_set.all()[1:4]                                                 
Out[19]: <QuerySet [<Comment: Comment object (2)>, <Comment: Comment object (3)>, <Comment: Comment object (4)>]>

In [20]: post1.comment_set.all()[1].user.post_set.first().user.name                   
Out[20]: 'lee'

In [21]: c = Comment.objects.values('user').get(pk=1)                                 
In [22]: c                                                                             
Out[22]: {'user': 1}
    
In [23]: user2.comment_set.order_by('-content')                                       Out[23]: <QuerySet [<Comment: Comment object (4)>, <Comment: Comment object (2)>, <Comment: Comment object (7)>, <Comment: Comment object (6)>]>
        
In [24]: Post.objects.filter(title='1글')                                             Out[24]: <QuerySet [<Post: Post object (1)>]>

In [25]: Post.objects.filter(title__contains='글')                                     Out[25]: <QuerySet [<Post: Post object (1)>, <Post: Post object (2)>, <Post: Post object (3)>]>

In [26]: Comment.objects.filter(post__title__contains='1')                             Out[26]: <QuerySet [<Comment: Comment object (1)>, <Comment: Comment object (2)>, <Comment: Comment object (3)>, <Comment: Comment object (4)>, <Comment: Comment object (6)>]>
```



* models.py

```python
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    
# user와 1:N 관계
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=20)
```



* djpy2.py - 객체생성

```python
user1 = User.objects.create(name='kim')
user2 = User.objects.create(name='lee')
post1 = Post.objects.create(title='1글', user=user1)
post2 = Post.objects.create(title='2글', user=user1)
post3 = Post.objects.create(title='3글', user=user2)
c1 = Comment.objects.create(content='1글1댓글', user=user1, post=post1)
c2 = Comment.objects.create(content='1글2댓글', user=user2, post=post1)
c3 = Comment.objects.create(content='1글3댓글', user=user1, post=post1)
c4 = Comment.objects.create(content='1글4댓글', user=user2, post=post1)
c5 = Comment.objects.create(content='2글1댓글', user=user1, post=post2)
c6 = Comment.objects.create(content='!1글5댓글', user=user2, post=post1)
c7 = Comment.objects.create(content='!1글6댓글', user=user2, post=post2)
```



* ORM문법 - Shell에서 실행

```python


$ python manage.py shell_plus

# 1번 사람이 작성한 게시글은?
user1.post_set.all()

# 1번 사람이 작성한 게시글별로 댓글을 출력해보세요
for post in user1.post_set.all():
    for comment in post.comment_set.all():         # comment와 post도 1:N관계이기 때문
        print(comment.content)
        
# 2번 댓글을 쓴 사람은?
c2.user

# 2번 댓글을 쓴 사람의 게시글들은?
c2.user.post_set.all()

# 1번 글의 첫번째 댓글을 작성한 사람의 이름은?
post1.comment_set.first().user.name    # 권장
post1.comment_set.all()[0].user.name

# 1번 글의 2번째부터 4번째까지의 댓글을 가져오세요.
post1.comment_set.all()[1:4]

# 1번 글의 2번째 댓글을 작성한 사람의 첫번째 게시글의 작성자의 이름은?
post1.comment_set.all()[1].user.post_set.first().user.name

# 1번 댓글의 user 정보만 가져온다면?
# c = Comment.objects.values('user').get(pk=1)
c = Comment.objects.all().values('user')

# 2번 user가 작성한 댓글을 content의 내림차순으로 가져오면?
user2.comment_set.order_by('-content')

# '1글'이라는 제목인 게시글들을 가져오세요.
Post.objects.filter(title='1글')

# 제목에 '글'이라는 단어가 있는 게시글은?
Post.objects.filter(title__contains='글')

# 댓글 중에 해당 글의 제목에 1이 포함된 댓글은?
Comment.objects.filter(post__title__contains='1')
```





* 다대다(N:M) 관계

* models.py

```python
from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()
    
    def __str__(self):
        return self.name
    
    
class Patient(models.Model):
    name = models.TextField()
    doctors = models.ManyToManyField(Doctor, related_name='patients')   
    # doctor와 patient 둘 중에 하나에 쓰면 됨
    # doctor에는 Patient_set라는 필드가 생성되어 참조
    # 역참조하기 위한 처리 - doctor가 patient를 참조하기 위함
    # (related_name 사용하여 의사가 가진 환자들의 목록 보려면 doctor.patients.all()로 가져올 수 있음!)
    
    def __str__(self):
        return self.name
        
# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
```



```python
$ python manage.py shell_plus

In [2]: doctor = Doctor.objects.create(name='kim')                                                                                                                                               

In [3]: patient = Patient.objects.create(name='john)                                                                                                                                             
  File "<ipython-input-3-63995ff5f14c>", line 1
    patient = Patient.objects.create(name='john)
                                                ^
SyntaxError: EOL while scanning string literal


In [4]: patient = Patient.objects.create(name='john')                                                                                                                                            

In [5]: Reservation.objects.create(doctor=doctor, patient=patient)                                                                                                                               
Out[5]: <Reservation: Reservation object (1)>

In [6]:                                                                                                                           In [6]:                                                     In In [6]: doctor.reservation_set.all()   # 의사가 가지고 있는 모든 예약 가져오기                                                                                                                   
Out[6]: <QuerySet [<Reservation: Reservation object (1)>]>

In [7]: patient.reservation_set.all()                                                                                                                                                            
Out[7]: <QuerySet [<Reservation: Reservation object (1)>]>

In [8]: patient2 = Patient.objects.create(name='Tom')                                                                                                                                            

In [9]: Reservation.objects.create(doctor=doctor, patient=patient2)                                                                                                                              
Out[9]: <Reservation: Reservation object (2)>

In [10]: doctor.reservation_set.all()                                                                                                                                                            
Out[10]: <QuerySet [<Reservation: Reservation object (1)>, <Reservation: Reservation object (2)>]>

In [11]: for reservation in doctor.reservation_set.all(): 
    ...:    print(reservation.patient.name) 
    ...:                                                                                                                                                                                         
john
Tom

In [12]: exit
```





```python
In [1]: patient = Patient.objects.get(pk=1)                                                                                                                                                      

In [2]: patient                                                                                                                                                                                  
Out[2]: <Patient: john>

In [3]: patient.doctors.all()                                                                                                                                                                    
Out[3]: <QuerySet [<Doctor: kim>]>

In [4]: doctor = Doctor.objects.create(name='park')                                                                                                                                              

In [5]: doctor.pk                                                                                                                                                                                
Out[5]: 2

In [6]: Reservation.objects.create(doctor=doctor, patient=patient)                                                                                                                               
Out[6]: <Reservation: Reservation object (3)>

In [7]: patient                                                                                                                                                                                  
Out[7]: <Patient: john>

In [8]: doctor.patient_set.all()                                                                                                                                                                 
Out[8]: <QuerySet [<Patient: john>]>

In [9]: doctor.patient_set.all()    # 의사가 가진 환자들의 목록                                                                                                                                  
Out[9]: <QuerySet [<Patient: john>]>

In [10]: exit                           
```



```python
In [1]: doctor = Doctor.objects.get(pk=1)                                                                                                                                                        

In [2]: doctor.patients.all()                                                                                                                                                                    
Out[2]: <QuerySet [<Patient: john>, <Patient: Tom>]>

In [3]: exit
```



```python
# DB 확인 - <manytomany_patient_doctors> 테이블 생긴 것 확인
(insta-venv) chelseashin:~/workspace/model_review $ sqlite3 db.sqlite3
SQLite version 3.8.2 2013-12-06 14:53:30
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> .tables
auth_group                  django_migrations         
auth_group_permissions      django_session            
auth_permission             manytomany_doctor         
auth_user                   manytomany_patient        
auth_user_groups            manytomany_patient_doctors
auth_user_user_permissions  onetomany_comment         
django_admin_log            onetomany_post            
django_content_type         onetomany_user            
sqlite> .schema manytomany_patient_doctors
CREATE TABLE "manytomany_patient_doctors" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "patient_id" integer NOT NULL REFERENCES "manytomany_patient" ("id") DEFERRABLE INITIALLY DEFERRED, "doctor_id" integer NOT NULL REFERENCES "manytomany_doctor" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE UNIQUE INDEX "manytomany_patient_doctors_patient_id_doctor_id_23ab539b_uniq" ON "manytomany_patient_doctors" ("patient_id", "doctor_id");
CREATE INDEX "manytomany_patient_doctors_patient_id_cb4ef2b1" ON "manytomany_patient_doctors" ("patient_id");
CREATE INDEX "manytomany_patient_doctors_doctor_id_7b77037d" ON "manytomany_patient_doctors" ("doctor_id");
```





* user는 여러 post에 like할 수 있고, 
* post는 여러 user로부터 like받을 수 있다.
* 중개 모델(조인 테이블)이 조인 테이블을 다로 생성해서 관계를 설정하는 게 M:N:bridge_at_night:
* 