Workshop

대전 2반 17번 신채원

2019-03-13

< 데이터베이스 관계(1: N) >

* 설문 앱을 만들려고 한다. 이 앱은 질문에 대한 답변을 투표하여 각각의 항목이 몇 표
  를 받았는지 저장하는 기능을 가지고 있다.
  설문 앱은 Question 모델과 Choice 모델을 가지고 있으며, 각각의 모델은 다음과 같은
  컬럼을 가지고 있고 1:N 관계를 가지고 있다.

![1552548068013](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1552548068013.png)



* 해당 컬럼을 가지고 있는 Question 모델과 Choice 모델을 정의하는 코드(models.py)
  를 작성하시오.

![1552548124627](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1552548124627.png)

```python
class Question(models.Model):
    title = models.CharField(max_length=100)
    
class Choice(models.Model):
    question = models.ForeignKey(Question, ondelete=models.CASCADE)
    content = models.CharField(max_length=100)
    votes = models.IntegerField()
```

