## AI_Naive Bayes



2019-06-25

/*** elice* **/  코딩  - AI/ML 교육

### < Naive Bayes 이해하기 >



#### * `Naive Bayes` 소개 

나이브 베이즈는 분류기를 만들 수 있는 간단한 기술로써 단일 알고리즘을 통한 훈련이 아닌 일반적인 원칙에 근거한 여러 알고리즘들을 이용하여 훈련된다. 모든 나이브 베이즈 분류기는 공통적으로 모든 특성 값은 서로 독립임을 가정한다. 예를 들어, 특정 과일을 사과로 분류 가능하게 하는 특성들 (둥글다, 빨갛다, 지름 10cm)은 나이브 베이즈 분류기에서 특성들 사이에서 발생할 수 있는 연관성이 없음을 가정하고 각각의 특성들이 특정 과일이 사과일 확률에 독립적으로 기여 하는 것으로 간주한다.

나이브 베이즈의 장점은 다음과 같다. 첫째, 일부의 확률 모델에서 나이브 베이즈 분류는 [지도 학습](https://ko.wikipedia.org/wiki/지도_학습) (Supervised Learning) 환경에서 매우 효율적으로 훈련 될 수 있다. 많은 실제 응용에서, 나이브 베이즈 모델의 파라미터 추정은 [최대우도방법](https://ko.wikipedia.org/wiki/최대가능도방법) (Maximum Likelihood Estimation (MLE))을 사용하며, [베이즈 확률론](https://ko.wikipedia.org/wiki/베이즈_확률론)이나 베이지안 방법들은 이용하지 않고도 훈련이 가능하다. 둘째, 분류에 필요한 파라미터를 추정하기 위한 트레이닝 데이터의 양이 매우 적다는 것이다. 셋째, 간단한 디자인과 단순한 가정에도 불구하고, 나이브 베이즈 분류는 많은 복잡한 실제 상황에서 잘 작동한다. 2004 년의 한 분석[[3\]](https://ko.wikipedia.org/wiki/나이브_베이즈_분류#cite_note-3)은 나이브 베이즈 분류의 이러한 능력에 명확한 이론적인 이유가 있음을 보여 주었다. 또한 2006 년에는 다른 분류 알고리즘과의 포괄적인 비교를 통하여 베이지안 분류는 부스트 트리 또는 [랜덤 포레스트](https://ko.wikipedia.org/wiki/랜덤_포레스트)와 같은 다른 접근 방식을 넘어섰다는 것이 밝혀졌다. - wikipedia



* 간단설명
  * 연구자들이 가장 기본으로 사용하는 알고리즘
  * 인과관계가 뚜렷한 알고리즘
  * 스팸 메일 필터링에 적용할 수 있다.
  * 조건부 확률과 베이즈 정리로부터 나온 알고리즘
  * 모델의 Generalization을 위해선 Smoothing이 중요
  * Feature들이 모두 독립임을 가정



* prior : P(Y)

  ![image](https://user-images.githubusercontent.com/45935233/60083993-aa8d5b00-9771-11e9-9b9f-6dc2f3679c3e.png)



### <실습>

#### Bayes Probability

#### 유방암 검사 키트

40대 여성이 mammogram(X-ray) 검사를 통해 유방암 양성 의심 판정을 받았을 때 유방암을 실제로 가지고 있을 확률은 어떻게 될까요?

`mammogram_test()` 함수를 구현하며 베이즈 법칙을 직접 응용해보겠습니다. `mammogram_test()` 함수는 세 가지 숫자를 입력 받습니다.

- `sensitivity` - 검사의 민감성을 뜻합니다. 유방암 보유자를 대상으로 검사 결과가 양성이 표시될 확률입니다. 0부터 1 사이의 값을 갖습니다.
- `prior_prob` - 총 인구를 기준으로 유방암을 가지고 있을 사전 확률(prior probability)입니다. 0.004 정도로 매우 낮은 값입니다.
- `false_alarm` - 실제로는 암을 갖고 있지 않지만 유방암이라고 진단될 확률입니다. 0.1 정도로 생각보다 높은 값입니다.

나이브 법칙을 이용해 입력 받은 세 값을 바탕으로 유방암 보유 여부를 확률로 출력합니다.

```
>>> 0.8
>>> 0.004
>>> 0.1
3.11%
Copy
```

----

#### 실습

1. A=1*A*=1 은 Mammogram 검사를 통해 암으로 진단되는 경우, B = 1*B*=1 은 실제로 유방암을 가지고 있는 경우입니다.
2. `sensitivity`는 P(A=1|B=1)*P*(*A*=1∣*B*=1)로 표현할 수 있습니다. 암을 실제로 가지고 있을 때 암으로 진단될 확률이 80%라면 P(A=1|B=1) = 0.8*P*(*A*=1∣*B*=1)=0.8입니다.
3. 일반적으로 유방암을 가지고 있을 확률은, 즉 `prior_prob`의 값은 매우 낮습니다: P(B=1) = 0.004*P*(*B*=1)=0.004
4. 유방암을 가지고 있지 않을 확률은 1에서 `prior_prob`를 빼면 됩니다: P(B=0)=1 - P(B=1)=0.996*P*(*B*=0)=1−*P*(*B*=1)=0.996
5. 실제로 암을 가지고 있지 않지만 암으로 진단되는 확률, `false_alarm`는 생각보다 매우 높습니다: P(A=1|B=0)=0.1*P*(*A*=1∣*B*=0)=0.1
6. Mammogram 검사를 통해 암으로 진단되는 경우의 확률, P(A=1)*P*(*A*=1)를 구해보겠습니다: P(A=1) =*P*(*A*=1)= P(A=1|B=0)P(B=0) + P(A=1|B=1)P(B=1)*P*(*A*=1∣*B*=0)*P*(*B*=0)+*P*(*A*=1∣*B*=1)*P*(*B*=1)= 0.10280.1028.
7. 유방암 진단을 받았을 때 실제로 유방암을 가지고 있을 확률을 베이즈 법칙을 이용해 계산하면 다음과 같습니다: \displaystyle P(B=1|A=1)=*P*(*B*=1∣*A*=1)= \displaystyle \frac{P(A=1|B=1)P(B=1)}{P(A=1)}=*P*(*A*=1)*P*(*A*=1∣*B*=1)*P*(*B*=1)= \displaystyle\frac{0.8\times 0.004}{0.1028}\sim0.10280.8×0.004∼ 0.03110.0311.

```python
def main():
    sensitivity = float(input())   # 의사가 유방암이라고 했는데 실제로 유방암인 경우
    prior_prob = float(input())    # 환자가 유방암을 가지고 있는 경우
    false_alarm = float(input())   # 실제 암을 가지고 있지 않은데 유방암인 경우

    print(mammogram_test(sensitivity, prior_prob, false_alarm))

def mammogram_test(sensitivity, prior_prob, false_alarm):

    """
    x=1 : 검진 결과 유방암 판정
    x=0 : 검진 결과 유방암 미판정
    y=1 : 유방암 발병됨
    y=0 : 유방암 미발병
    """

    # The likelyhood probability : 유방암을 가지고 있는 사람이 검진 결과 유방암 판정 받을 확률
    p_x1_y1 = sensitivity # p(x = 1|y = 1)

    # The prior probability : 유방암을 가지고 있을 확률로 매우 낮다.
    p_y1 = prior_prob # p(y = 1)

    # False alram : 유방암을 가지고 있지 않지만 검사 결과 유방암 판정을 받을 확률
    p_x1_y0 =  false_alarm # p(x = 1|y = 0)

    # Bayes rule 
    p_y1_x1 =  ((p_x1_y1 * p_y1)/((p_x1_y1 * p_y1) + (p_x1_y0*(1-p_y1))))
 # p(y = 1|x = 1)

    # 검사 결과 유방암 판정을 받은 환자가 정확한 검진을 받았단 확률
    return p_y1_x1

if __name__ == "__main__":
    main()

```





#### 뉴스 데이터 분류하기

`Scikit-learn`에는 머신러닝을 위한 다양한 라이브러리가 내장되어 있습니다.

`Scikit-learn`을 이용하여 뉴스 데이터 기반 간단한 Naive Bayes 분류를 진행해보겠습니다.

이를 위해 4가지 내장 모듈을 불러옵니다.

1. `fetch_20newsgroups`
2. `CountVectorizer`
3. `MultinomialNB`
4. `accuracy_score`

위의 모듈을 토대로 Train과 Test 데이터 세트를 구성하고 Multinomial Naive Bayes 모델을 학습하여 Test 데이터로 정확도를 예측해보겠습니다.

----

#### 실습

1. 머신러닝 전용 라이브러리를 사용하면 간단한 코드로 Naive Bayes 분류를 연습해볼 수 있습니다.
2. 스켈레톤 코드를 따라가며 코드를 이해하고 학습해보세요.

```python
from sklearn.datasets import fetch_20newsgroups             # 20 News group 데이터 로드
from sklearn.feature_extraction.text import CountVectorizer # 단어를 Bag of Word로 만들기 위한 모듈
from sklearn.naive_bayes import MultinomialNB               # 다항분포 나이브 베이즈 모델
from sklearn.metrics import accuracy_score                  # 정확도 계산을 위한 모듈

# Train & Test 데이터 준비
newsdata=fetch_20newsgroups(subset='train')
newsdata_test = fetch_20newsgroups(subset='test', shuffle=True) 

# 데이터 분석
print('데이터 속성                  : ',newsdata.keys())
print('Train 데이터 개수            : ',len(newsdata.data))
print('Train 데이터의 Label 개수    : ',len(newsdata.target))
print('Train 데이터의 카테고리 개수 : ',newsdata.target_names,'\n')

# 뉴스 데이터의 단어를 학습 가능하도록 BoW로 변환
tdmvector = CountVectorizer()
X_train_tdm = tdmvector.fit_transform(newsdata.data)
print('Train Data의 개수, Data안의 단어 개수 : ',X_train_tdm.shape)

# 사이킷런에 내장되어 있는 Naive-Bayes 모델 불러오기
mod = MultinomialNB()

# 뉴스 데이터 학습
mod.fit(X_train_tdm, newsdata.target)

# Test 데이터를 BoW으로 변환
X_test_tdm = tdmvector.transform(newsdata_test.data) 

# Test 데이터에 대한 예측
predicted = mod.predict(X_test_tdm) 
print("Test 데이터 정확도 : ", accuracy_score(newsdata_test.target, predicted)) #예측값과 실제값 비교
```



* 결과

```python
Downloading 20news dataset. This may take a few minutes.
Downloading dataset from https://ndownloader.figshare.com/files/5975967 (14 MB)
데이터 속성                  :  dict_keys(['data', 'filenames', 'target_names', 'target', 'DESCR', 'description'])
Train 데이터 개수            :  11314
Train 데이터의 Label 개수    :  11314
Train 데이터의 카테고리 개수 :  ['alt.atheism', 'comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware', 'comp.windows.x', 'misc.forsale', 'rec.autos', 'rec.motorcycles', 'rec.sport.baseball', 'rec.sport.hockey', 'sci.crypt', 'sci.electronics', 'sci.med', 'sci.space', 'soc.religion.christian', 'talk.politics.guns', 'talk.politics.mideast', 'talk.politics.misc', 'talk.religion.misc'] 

Train Data의 개수, Data안의 단어 개수 :  (11314, 130107)
Test 데이터 정확도 :  0.7728359001593202
코드 실행이 완료되었습니다.
```





#### 나이브 베이즈 분류기

나이브 베이즈 분류기를 직접 구현해 보겠습니다. 두 개의 사탕 기계를 살펴보겠습니다.

- 첫 번째 기계 M_1*M*1 - \{\theta_{red} = 0.7, \theta_{green} = 0.2, \theta_{blue} = 0.1\}{*θ**r**e**d*=0.7,*θ**g**r**e**e**n*=0.2,*θ**b**l**u**e*=0.1}
- 두 번째 기계 M_2*M*2 - \{\theta_{red} = 0.3, \theta_{green} = 0.4, \theta_{blue} = 0.3\}{*θ**r**e**d*=0.3,*θ**g**r**e**e**n*=0.4,*θ**b**l**u**e*=0.3}

두 기계에서 사탕을 뽑을 확률은 다음과 같습니다.

- p(M_1) = 0.7*p*(*M*1)=0.7
- p(M_2) = 0.3*p*(*M*2)=0.3

다음과 같이 10개의 사탕을 뽑았을 때 이 사탕들이 몇 번째 기계에서 나왔을지 확률로 표현해보는 코드를 작성해보겠습니다.

- red - 4
- green - 3
- blue - 3

이 확률은 p(M_k|x)*p*(*M**k*∣*x*), k \in \{1, 2\}*k*∈{1,2} 로 나타낼 수 있습니다. 나이브 법칙을 적용하면 p(M_k|x) =\frac{p(M_k)p(x|M_k)}{p(x)}*p*(*M**k*∣*x*)=*p*(*x*)*p*(*M**k*)*p*(*x*∣*M**k*)가 됩니다. 이때 두 기계의 p(x)*p*(*x*) 는 같으므로 무시하겠습니다.

p(M_1)*p*(*M*1) 와 p(M_2)*p*(*M*2) 의 상대적인 확률은 다음과 같습니다.

p(M_1|x)\propto p(M_1)p(x|M_1)=*p*(*M*1∣*x*)∝*p*(*M*1)*p*(*x*∣*M*1)= 0.7 * (0.7^4 * 0.2^3 * 0.1^3) = 1.345 * 10^{-6}0.7∗(0.74∗0.23∗0.13)=1.345∗10−6

p(M_2|x)\propto p(M_2)p(x|M_2)=*p*(*M*2∣*x*)∝*p*(*M*2)*p*(*x*∣*M*2)= 0.3 * (0.3^4 * 0.4^3 * 0.3^3) = 4.199 * 10^{-6}0.3∗(0.34∗0.43∗0.33)=4.199∗10−6

두 번째 기계에서 뽑혔을 확률이 훨씬 더 높은 것을 알 수 있습니다. 두 확률을 표준화(Normalize)하면 다음과 같습니다.

(1.345 * 10^{-6}, 4.199 * 10^{-6}) \rightarrow (0.243, 0.757)(1.345∗10−6,4.199∗10−6)→(0.243,0.757)

즉 나이브 베이즈 분류기를 사용했을 때 10개의 사탕이 두번째 기계에서 뽑혔을 확률은 75.7\%75.7%입니다.

----

#### 실습

1. 위의 설명을 읽고, naive_bayes() 함수를 직접 구현해보세요.
2. 이 함수는 두 개의 원소로 이루어진 리스트 하나를 출력합니다.
   - 첫 번째 원소 = P(M1|test)P(M1∣test)
   - 두 번째 숫자 = P(M2|test)P(M2∣test)

의 표준화된 값입니다. 즉, 두 값을 합은 1이 되어야 합니다.

```python
import re
import math
import numpy as np

def main():
    M1 = {'r': 0.7, 'g': 0.2, 'b': 0.1} # M1 기계의 사탕 비율
    M2 = {'r': 0.3, 'g': 0.4, 'b': 0.3} # M2 기계의 사탕 비율
    
    test = {'r': 4, 'g': 3, 'b': 3}

    print(naive_bayes(M1, M2, test, 0.7, 0.3))

# def naive_bayes(M1, M2, test, M1_prior, M2_prior):
#     M1_likelyhood = M1['r'] ** test('r') * M1['g'] ** test['g'] * N
#     return [1, 0]
def naive_bayes(M1, M2, test, M1_prior, M2_prior):
    p_M1_test = M1_prior * ((M1['r'] ** test['r']) * (M1['g'] ** test['g']) * (M1['b'] ** test['b']))  
    p_M2_test = M2_prior * ((M2['r'] ** test['r']) * (M2['g'] ** test['g']) * (M2['b'] ** test['b']))  
    arr = np.array([p_M1_test, p_M2_test])
    return arr/sum(arr)

if __name__ == "__main__":
    main()
```



* 결과

```python
[0.24254275 0.75745725]
코드 실행이 완료되었습니다.
```

