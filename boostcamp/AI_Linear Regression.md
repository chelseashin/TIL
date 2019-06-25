## Linear Regression



2019-06-25

/*** elice* **/  코딩  - AI/ML 교육

< Linear Regression 이해하기 >



#### 1. 기울기와 절편

단순 선형회귀 분석 수식은 다음과 같습니다.

![image](https://user-images.githubusercontent.com/45935233/60066531-68005a00-9742-11e9-9bf5-547400f08071.png)

여기서 *β0* 은 `기울기`, *β1* 은 `y절편`을 의미합니다.

코드를 실행하여 기울기와 *y*절편이 의미하는 것을 이해하여 봅니다.



#### 실습

1. 코드를 실행해보고 결과를 확인해보세요.
2. 베타 값을 수정하면 그래프가 어떻게 변하는지 실행하여 확인해 봅시다.

```python
# 실습에 필요한 패키지입니다. 수정하지 마세요.
import elice_utils
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
eu = elice_utils.EliceUtils()

# 실습에 필요한 데이터입니다. 수정하지마세요. 
X = [8.70153760, 3.90825773, 1.89362433, 3.28730045, 7.39333004, 2.98984649, 2.25757240, 9.84450732, 9.94589513, 5.48321616]
Y = [5.64413093, 3.75876583, 3.87233310, 4.40990425, 6.43845020, 4.02827829, 2.26105955, 7.15768995, 6.29097441, 5.19692852]

'''
beta_0과 beta_1 을 변경하면서 그래프에 표시되는 선을 확인해 봅니다.
기울기와 절편의 의미를 이해합니다.
'''

beta_0 = 0.5   # beta_0에 저장된 기울기 값을 조정해보세요. 
beta_1 = 2 # beta_1에 저장된 절편 값을 조정해보세요.

plt.scatter(X, Y) # (x, y) 점을 그립니다.
plt.plot([0, 10], [beta_1, 10 * beta_0 + beta_1], c='r') # y = beta_0 * x + beta_1 에 해당하는 선을 그립니다.

plt.xlim(0, 10) # 그래프의 X축을 설정합니다.
plt.ylim(0, 10) # 그래프의 Y축을 설정합니다.

# 엘리스에 이미지를 표시합니다.
plt.savefig("test.png")
eu.send_image("test.png")
```

![image](https://user-images.githubusercontent.com/45935233/60063545-41d5bc80-9738-11e9-96bd-c458f7e34c19.png)



#### 2. Loss Function

앞서 배운 선형 회귀분석 모델에서 Loss Function을 구하는 방법을 알아보겠습니다.

![image](https://user-images.githubusercontent.com/45935233/60066531-68005a00-9742-11e9-9bf5-547400f08071.png)

Loss function 은 예측한 데이터와 실제 데이터와의 차이로 다음과 같이 정의 할 수 있습니다.

![image](https://user-images.githubusercontent.com/45935233/60070242-e663f880-9750-11e9-8ece-91045ee16335.png)

----

#### 실습

1. loss(x, y, beta_0, beta_1) 함수를 완성합니다.
2. beta_0, beta_1 값을 바꿔가며 loss값을 출력해봅니다.
3. loss값이 줄어들었다면 그래프 상으로 어떤 변화가 있었는지 확인합니다.
4. loss값이 최소값이 되도록 beta_0, beta_1값을 찾는 좋은 방식이 있을까 생각해봅니다.

```python
import elice_utils
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
eu = elice_utils.EliceUtils()

def loss(x, y, beta_0, beta_1):
    N = len(x)
    loss = 0
    for a, b in zip(x, y):
        ypredict = beta_0 * a + beta_1
        loss = (b - ypredict) ** 2
    return loss

X = [8.70153760, 3.90825773, 1.89362433, 3.28730045, 7.39333004, 2.98984649, 2.25757240, 9.84450732, 9.94589513, 5.48321616]
Y = [5.64413093, 3.75876583, 3.87233310, 4.40990425, 6.43845020, 4.02827829, 2.26105955, 7.15768995, 6.29097441, 5.19692852]

beta_0 = 0.5 # 기울기
beta_1 = 2 # 절편

print("Loss: %f" % loss(X, Y, beta_0, beta_1))

plt.scatter(X, Y) # (x, y) 점을 그립니다.
plt.plot([0, 10], [beta_1, 10 * beta_0 + beta_1], c='r') # y = beta_0 * x + beta_1 에 해당하는 선을 그립니다.

plt.xlim(0, 10) # 그래프의 X축을 설정합니다.
plt.ylim(0, 10) # 그래프의 Y축을 설정합니다.
plt.savefig("test.png") # 저장 후 엘리스에 이미지를 표시합니다.
eu.send_image("test.png")
```

![image](https://user-images.githubusercontent.com/45935233/60063545-41d5bc80-9738-11e9-96bd-c458f7e34c19.png)



#### 3. Scikit-learn을 이용한 linear regression

기계학습 라이브러리 `Scikit-learn`을 사용하면 최적화 된 β0,  *β1* 을 쉽게 구할 수 있습니다.

주어진 데이터와 다음 선형 모델을 이용하여 최적의 β0,  *β1*  값을 [scikit-learn](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html) 라이브러리를 사용하여 구할 수 있습니다.

![image](https://user-images.githubusercontent.com/45935233/60066531-68005a00-9742-11e9-9bf5-547400f08071.png)

----

#### 실습

1. `np.array(X).reshape(-1, 1)` 명령어를 이용해 길이 10인 1차원 리스트 `X` 를 10\times 110×1 형태의 `np.array`로 변경하세요.

2. 리스트 `Y`를 `np.array` 형식으로 변경하세요.

3. 모델을 학습

   ```python
   lrmodel = LinearRegression()
   lrmodel.fit(train_X, train_Y)
   ```

4. 모델을 이용해 얻은 최적의 `beta_0`, `beta_1`값을 확인합니다.

```python
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

import elice_utils
eu = elice_utils.EliceUtils()

    
X = [8.70153760, 3.90825773, 1.89362433, 3.28730045, 7.39333004, 2.98984649, 2.25757240, 9.84450732, 9.94589513, 5.48321616]
Y = [5.64413093, 3.75876583, 3.87233310, 4.40990425, 6.43845020, 4.02827829, 2.26105955, 7.15768995, 6.29097441, 5.19692852]

train_X = np.array(X).reshape(-1, 1)
train_Y = np.array(Y).reshape(-1, 1)

'''
여기에서 모델을 트레이닝합니다.
'''
lrmodel = LinearRegression()
lrmodel.fit(train_X, train_Y)

beta_0 = lrmodel.coef_[0]
beta_1 = lrmodel.intercept_

print("beta_0: %f" % beta_0)
print("beta_1: %f" % beta_1)

plt.scatter(X, Y) # (x, y) 점을 그립니다.
plt.plot([0, 10], [beta_1, 10 * beta_0 + beta_1], c='r') # y = beta_0 * x + beta_1 에 해당하는 선을 그립니다.

plt.xlim(0, 10) # 그래프의 X축을 설정합니다.
plt.ylim(0, 10) # 그래프의 Y축을 설정합니다.
plt.savefig("test.png") # 저장 후 엘리스에 이미지를 표시합니다.
eu.send_image("test.png")
```



![image](https://user-images.githubusercontent.com/45935233/60064505-96c70200-973b-11e9-9ed7-b22c612abd06.png)





#### 4. 선형 회귀 구현하기

`선형 회귀`는 종속 변수 y와 한 개 이상의 독립 변수 X와의 선형 상관 관계를 모델링하는 회귀분석 기법을 말한다.

이번 시간에는 y와 x가 주어졌을 때, `y = ax+b` 라는 형태의 직선을 회귀식으로 하는 단순한 선형 회귀(Linear Regression) 파이썬을 통해 직접 구현해보도록 하자.

------

**선형 회귀의 절차**

1. x라는 값이 입력되면 'ax+b’라는 계산식을 통해 값을 산출하는 예측 함수를 정의한다.
2. 예측 함수를 통해 예측값과 실제값 y 간의 차이를 계산한다.
3. a와 b를 업데이트 하는 규칙을 정의하고 이를 바탕으로 a와 b의 값을 조정한다.
4. 위의 과정을 특정 반복횟수 만큼 반복한다.
5. 반복적으로 수정된 a와 b를 바탕으로 `y=ax+b` 라는 회귀식을 정의한다.

------

#### 실습

1. 학습률을 직접 설정해 본다.
2. 반복횟수를 설정한다.
3. Numpy 배열 a, b, x 를 받아서 'ax+b’를 계산하는 prediction 함수를 정의한다.
4. 실제값과 예측값의 차이를 계산하여 error를 정의한다.
5. matplotlib을 사용해 그래프를 그려보고 위 설정 값에 따라 회귀 직선이 어떻게 변화하는지 살펴보자.

```python
import numpy as np
import elice_utils
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use("Agg")
eu = elice_utils.EliceUtils()

#학습률(learning rate)를 설정한다.(권장: 0.0001~0.01)
learning_rate = 0.001
#반복 횟수(iteration)를 설정한다.(자연수)
iteration = int(1e5)

def prediction(a,b,x):
    # 넘파이 배열 a,b,x를 받아서 'x*(transposed)a + b'를 계산하는 식을 만든다.
    equation = x * a.T + b
    
    return equation
    
def update_ab(a,b,x,error,lr):
    # a를 업데이트하는 규칙을 정의한다.
    delta_a = -(lr*(2/len(error))*(np.dot(x.T, error)))
    # b를 업데이트하는 규칙을 정의한다.
    delta_b = -(lr*(2/len(error))*np.sum(error))
    
    return delta_a, delta_b
    
def gradient_descent(x, y, iters):
    #초기값 a= 0, a=0
    a = np.zeros((1,1))
    b = np.zeros((1,1))
    
    for i in range(iters):
        #실제 값 y와 예측 값의 차이를 계산하여 error를 정의한다.
        error =  y - prediction(a, b, x)
        a_delta, b_delta = update_ab(a,b,x,error,lr=learning_rate)
        a -= a_delta
        b -= b_delta
        
    return a, b

def plotting_graph(x,y,a,b):
    y_pred=a[0,0]*x+b
    plt.scatter(x, y)
    plt.plot(x, y_pred)
    plt.savefig("test.png")
    eu.send_image("test.png")

def main():

    x = 5*np.random.rand(100,1)
    y = 3*x + 5*np.random.rand(100,1)
    
    a, b = gradient_descent(x,y,iters=iteration)
    
    print("a:",a, "b:",b)
    plotting_graph(x,y,a,b)
    
main()
```

![image](https://user-images.githubusercontent.com/45935233/60066407-05a75980-9742-11e9-8896-21982529413e.png)





#### 5. 릿지 회귀(Ridge Regression) 구현하기

`릿지 회귀`는 일반적인 선형회귀에서 L2 규제 항(regularization terms)이 추가된 회귀를 의미합니다.

이번 시간에는 릿지 회귀를 직접구현해보고, 파라미터를 변경해가며 회귀 결과가 어떻게 변화하는지 살펴봅니다.

------

1. x라는 값이 입력되면 'ax+b'라는 계산식을 통해 값을 산출하는 예측 함수를 정의합니다.
2. 예측 함수를 통해 예측값과 실제값 y 간의 차이를 계산합니다.
3. a와 b를 업데이트 하는 규칙을 정의하고 이를 바탕으로 a와 b의 값을 조정합니다. (alpha 값을 이용하여 규제 항을 설정합니다.)
4. 위의 과정을 특정 반복횟수 만큼 반복합니다.
5. 반복적으로 수정된 a와 b를 바탕으로 ‘y=ax+b’ 라는 회귀식을 정의합니다.



#### 실습

1. 학습률을 직접 설정해 봅니다.
2. 반복횟수를 설정합니다.
3. alpha 값을 설정합니다.
4. Numpy 배열 a, b, x 를 받아서 'ax+b’를 계산하는 prediction 함수를 정의합니다.
5. 규제항을 alpha값과 a의 곱으로 설정하고 a와 b를 업데이트하는 규칙에 이를 추가합니다.
6. 실제값과 예측값의 차이를 계산하여 error를 정의합니다.
7. matplotlib을 사용해 그래프를 그려보고 위 설정 값에 따라 회귀 직선이 어떻게 변화하는지 살펴봅니다.

```python
import numpy as np
import elice_utils
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use("Agg")
eu = elice_utils.EliceUtils()

#학습률(learning rate)를 설정한다.(권장: 0.0001~0.01)
learning_rate = 0.001
#반복 횟수(iteration)를 설정한다.(자연수)
iteration = int(1e5)
#릿지회귀에 사용되는 알파(alpha) 값을 설정한다.(권장: 0.0001~0.01)
alpha = 0.001

def prediction(a,b,x):    
    return a.T * x + b
    
def update_ab(a,b,x,error,lr, alpha):
    #alpha와 a의 곱으로 regularization을 설정한다.  
    regularization = alpha * a
    delta_a = -(lr*(2/len(error))*(np.dot(x.T, error)) + regularization)
    delta_b = -(lr*(2/len(error))*np.sum(error))
    return delta_a, delta_b
    
def gradient_descent(x, y, iters, alpha):
    #초기값 a= 0, a=0
    a = np.zeros((1,1))
    b = np.zeros((1,1))    
    
    for i in range(iters):
        error = y - prediction(a, b, x)
        a_delta, b_delta = update_ab(a,b,x,error,lr=learning_rate, alpha=alpha)
        a -= a_delta
        b -= b_delta
    
    return a, b

def plotting_graph(x,y,a,b):
    y_pred=a[0,0]*x+b
    plt.scatter(x, y)
    plt.plot(x, y_pred)
    plt.savefig("test.png")
    eu.send_image("test.png")

def main():
    #x, y 데이터를 생성한다.
    x = 5*np.random.rand(100,1)
    y = 10*x**4 + 2*x + 1+ 5*np.random.rand(100,1)
    # a와 b의 값을 반복횟수만큼 업데이트하고 그 값을 출력한다. 
    a, b = gradient_descent(x,y,iters=iteration, alpha=alpha)
    print("a:",a, "b:",b)
    #회귀 직선과 x,y의 값을 matplotlib을 통해 나타낸다.
    plotting_graph(x,y,a,b)
    
main()
```

