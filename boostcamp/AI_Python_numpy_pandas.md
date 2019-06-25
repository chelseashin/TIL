## AI - Python(Numpy & Pandas)



2019-06-25



### < Python  Library - `Numpy` 다루기 >



#### 1. Numpy 배열 생성하기

넘파이(Numpy)는 파이썬 기반의 고성능의 수치 계산을 위한 라이브러리입니다.

넘파이는 계산의 기반이 되는 배열(array)을 간편하게 생성할 수 있는 여러 가지 함수들을 제공하고 있습니다.

이번 실습에서 넘파이의 여러 함수들을 이용하여 배열을 생성하는 방법을 익혀봅니다.

------

**넘파이 배열을 생성하는 함수들**

- **np.array(list):** list를 넘파이 배열로 생성
- **np.zeros(shape):** 0 이 들어있는 배열 생성
- **np.ones(shape):** 1 이 들어있는 배열 생성
- **np.empty(shape):** 초기화가 없는 값으로 배열을 반환
- **np.arange(n ,m):** arange 함수를 이용하여 배열을 생성
- **np.linspace(start ,end, num-points):**linspace 함수를 이용하여 시작점과 끝 사이에 균일한 값을 주는 배열을 생성
- **np.random.randit(start end, array-size):**radom.randit함수를 이용하여 랜덤값으로 배열을 생성



#### 실습

1. 파이썬 리스트로 만들어진 정수형 array를 만듭니다.
2. 파이썬 리스트로 만들어진 실수형 array 를 만듭니다.
3. 0으로 10개 채워진 정수형 array를 만듭니다.
4. 0부터 1사이에 균등하게 나눠진 5개의 값이 담긴 array를 만듭니다.
5. 0부터 10사이 랜덤한 값이 담긴 2x2 array 를 만듭니다.
6. 0부터 1사이에 균등하게 나눠진 5개의 값이 담긴 array를 만듭니다.
7. 0부터 10사이 랜덤한 값이 담긴 2x2 array를 만듭니다.

 ```python
from elice_utils import EliceUtils
import numpy as np

elice_utils = EliceUtils()


def main():
	
    print("Array1: 파이썬 리스트로 만들어진 정수형 array")
    array1 = np.array([1, 2, 3], dtype=int)
    print("데이터:", array1)
    print("array의 자료형:", type(array1))
    print("dtype:", array1.dtype, "\n")

    print("Array2: 파이썬 리스트로 만들어진 실수형 array")
    array2 = np.array([1.1, 2.2, 3.3, 4.4], dtype=float)
    print("데이터:", array2)
    print("dtype:", array2.dtype, "\n")

    print("Array3: 0으로 10개 채워진 정수형 array")
    array3 = np.zeros(10)
    print("데이터:", array3)
    print("dtype:", array3.dtype, "\n")

    print("Array4: 1으로 채워진 3x5형태 실수형 array")
    array4 = np.array([np.ones(5), np.ones(5), np.ones(5)])
    print("데이터:", array4)
    print("dtype:", array4.dtype, "\n")

    print("Array5: 0부터 9까지 담긴 정수형 array")
    array5 = np.arange(0, 10)
    print("데이터:", array5, "\n")

    print("Array6: 0부터 1사이에 균등하게 나눠진 5개의 값이 담긴 array")
    array6 = np.linspace(0, 1, 5)
    print("데이터:", array6, "\n")

    print("Array7: 0부터 10사이 랜덤한 값이 담긴 2x2 array")
    # array7 = np.array([np.random.randint(0, 10, 2), np.random.randint(0, 10, 2)])
    array7 = np.array(np.random.randint(0, 10, (2, 2)))
    print("데이터:", array7, "\n")
    
    
if __name__ == "__main__":
    main()
 ```

```python
# 결과
Array1: 파이썬 리스트로 만들어진 정수형 array
데이터: [1 2 3]
array의 자료형: <class 'numpy.ndarray'>
dtype: int64 

Array2: 파이썬 리스트로 만들어진 실수형 array
데이터: [1.1 2.2 3.3 4.4]
dtype: float64 

Array3: 0으로 10개 채워진 정수형 array
데이터: [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
dtype: float64 

Array4: 1으로 채워진 3x5형태 실수형 array
데이터: [[1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]]
dtype: float64 

Array5: 0부터 9까지 담긴 정수형 array
데이터: [0 1 2 3 4 5 6 7 8 9] 

Array6: 0부터 1사이에 균등하게 나눠진 5개의 값이 담긴 array
데이터: [0.   0.25 0.5  0.75 1.  ] 

Array7: 0부터 10사이 랜덤한 값이 담긴 2x2 array
데이터: [[6 8]
 [8 9]] 

코드 실행이 완료되었습니다.
```





#### 2. Numpy 배열의 특정요소 추출하기

넘파이 배열을 사용할 때, 행렬 전체가 아닌 특정 성분 또는 구간 만을 사용할 때가 있습니다.

이에 대하여 넘파이는 특정 성분 또는 구간을 추출하는 편리한 기능을 제공하고 있습니다.

이번 실습에서는 이러한 배열의 특정 성분들을 출력하는 것을 실습을 통해서 익혀봅시다.

------

**배열을 인덱싱/슬라이싱 하는 함수들**

- **ndarray[n, m]:** n 행 m 열의 원소를 추출.
- **ndarray[n, :]:** n 행을 추출.
- **ndarray[:, m]:** m 열을 추출.



#### 실습

1. 배열의 특정 성분을 출력합니다.
2. 배열의 특정 행을 출력합니다.
3. 배열의 특정 열을 출력합니다.
4. 배열의 특정 행을 추출하고, 그것을 바탕으로 새로운 배열을 만들어 출력합니다.

```python
import numpy as np

array_1 = np.array([[4,2,5],[5,3,2],[9,1,2]])

#1. 배열 array_1에 대하여 2행 3열의 원소를 추출하세요. 
element_1 = array_1[1, 2]
print("2행 3열의 원소는 ", element_1, " 입니다.")

#2. 배열 array_1에 대하여 3행을 추출하세요. 
row_1 = array_1[2,:]
print("3행은 배열 ", row_1, " 입니다.")

#3. 배열 array_1에 대하여 2열을 추출하세요. 
col_1 = array_1[:,1]
print("2열은 배열 ", col_1, " 입니다.")

#4. x의 1행과 3행을 바꾼 행렬을 만들어보세요. 
y = array_1[::-1]
print(y)
```

```python
# 결과
2행 3열의 원소는  2  입니다.
3행은 배열  [9 1 2]  입니다.
2열은 배열  [2 3 1]  입니다.
[[9 1 2]
 [5 3 2]
 [4 2 5]]
코드 실행이 완료되었습니다.
```





#### 3. Numpy 배열의 통계적 정보 나타내기

Numpy는 배열의 원소에 대하여 최솟값, 최댓값, 평균, 분산 등의 통계적인 정보를 간단하게 계산하는 함수들을 제공하고 있습니다.

이번 시간에는 Numpy 에서 제공하는 함수들을 이용하여 배열 원소들의 여러 통계적 정보들을 출력해 봅시다.

------

**배열의 통계적 정보를 나타내주는 함수들**

- **np.min(x):** 배열 x 의 최솟값을 나타냅니다.
- **np.max(x):** 배열 x 의 최댓값을 나타냅니다.
- **np.mean(x):** 배열 x 의 평균값을 구합니다.
- **np.median(x):** 배열 x 의 중앙값을 구합니다.
- **np.var(x):** 배열 x 의 분산을 구합니다.
- **np.std(x):** 배열 x 의 표준편차를 구합니다.



#### 실습

1. [[5,2,3,0], [3,4,5,1], [3,2,7,9]] 값을 갖는 A 메트릭스를 선언합니다.
2. 주어진 A 메트릭스의 원소의 합이 1이 되도록 표준화 (Normalization) 합니다.
3. 표준화 된 A 메트릭스의 분산을 구하여 리턴합니다.
4. 모든 값이 1인 4 × 4의 메트릭스 A를 생성합니다.
5. 표준화 된 메트릭스 A의 분산을 구하여 리턴합니다.

```python
import numpy as np


def main():
    print(matrix_nom_var())
    print(matrix_uni_std())

def matrix_nom_var():
    
    # [[5,2,3,0], [3,4,5,1], [3,2,7,9]] 값을 갖는 A 메트릭스를 선언합니다.
    A = np.array([[5,2,3,0], [3,4,5,1], [3,2,7,9]])

    # 주어진 A 메트릭스의 원소의 합이 1이 되도록 표준화 (Normalization) 합니다.
    # A = np.array([[(a - np.mean(lst)) / np.std(lst) for a in lst] for lst in A])
    # A = np.array([[a / sum(lst) for a in lst] for lst in A])
    A = A / np.sum(A)
    print(A)

    # 표준화 된 A 메트릭스의 분산을 구하여 리턴합니다.
    return np.var(A)

def matrix_uni_std():
    
    # 모든 값이 1인 4 by 4 A 메트릭스를 생성합니다.
    # A = np.array([[1] * 4 for _ in range(4)])
    A = np.zeros((4, 4)) + 1
    print(A)

    # 표준화 된 A 메트릭스의 분산을 구하여 리턴합니다.
    return np.var(A)

main()
```

```python
# 결과
[[0.11363636 0.04545455 0.06818182 0.        ]
 [0.06818182 0.09090909 0.11363636 0.02272727]
 [0.06818182 0.04545455 0.15909091 0.20454545]]
0.0030417814508723606
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]]
0.0
코드 실행이 완료되었습니다.
```





#### 4. Numpy 함수로 행렬연산 다루기

Numpy는 행렬과 관련된 여러 편리한 연산과 기능들을 제공하고 있습니다. 행렬의 곱, 전치 행렬, 역행렬 등을 간편하게 구할 수 있게끔 합니다.

이번 시간에는 Numpy의 함수를 이용해서 행렬의 여러 연산들을 적용하여 봅시다.

------

**행렬의 연산과 관련된 함수들**

- np.transpose(x) / (ndarray)x.T: 배열 x의 전치 행렬을 나타낸다.
- np.dot(x, y): 배열 x와 y의 행렬곱을 나타낸다.
- (ndarray)x * (ndarray)y : 행렬x와 y의 요소별 곱을 나타낸다.
- np.linalg.inv(x): 행렬 x의 역행렬을 배열로 나타낸다.



#### 실습

1. array1과 array1의 전치 행렬의 행렬곱을 구해보자.
2. array1과 array1의 전치 행렬의 요소별 곱을 구해보자.
3. array2의 역행렬을 만들어보자.
4. array2와 array2의 역행렬을 곱한 행렬을 만들어보자.

```python
import numpy as np

array1 = np.array([[1,2,3], [4,5,6], [7,8,9]])

#array1의 전치 행렬을 구해보자.
# transposed = np.transpose(array1)
transposed = array1.T
print(transposed, '는 array1을 전치한 행렬입니다.')    

#array1과 array1의 전치 행렬의 행렬곱을 구해보자.
power = np.dot(array1, transposed)
print(power,'는 array1과 array1의 전치 행렬을 행렬곱한 것입니다.')

#array1과 array1의 전치 행렬의 요소별 곱을 구해보자.
elementwise_prod = array1 * transposed
print(elementwise_prod, '는 array1과 array1의 전치행렬을 요소별로 곱한 행렬입니다.')


array2 = np.array([[2,3],[1,7]])

# array2의 역행렬을 만들어보자.
inverse_array2 = np.linalg.inv(array2)
print(inverse_array2,'는 array2의 역행렬입니다.')

# array2와 array2의 역행렬을 곱한 행렬을 만들어보자.
producted = np.dot(array2, inverse_array2)
print(producted,'는 array2와 array2의 역행렬을 곱한 행렬입니다.')
```

```python
# 결과
[[1 4 7]
 [2 5 8]
 [3 6 9]] 는 array1을 전치한 행렬입니다.
[[ 14  32  50]
 [ 32  77 122]
 [ 50 122 194]] 는 array1과 array1의 전치 행렬을 행렬곱한 것입니다.
[[ 1  8 21]
 [ 8 25 48]
 [21 48 81]] 는 array1과 array1의 전치행렬을 요소별로 곱한 행렬입니다.
[[ 0.63636364 -0.27272727]
 [-0.09090909  0.18181818]] 는 array2의 역행렬입니다.
[[ 1.00000000e+00  5.55111512e-17]
 [-2.77555756e-17  1.00000000e+00]] 는 array2와 array2의 역행렬을 곱한 행렬입니다.
코드 실행이 완료되었습니다.
```





### < Python  Library - `Pandas` 다루기 >



#### 1. Pandas 선언

Pandas는 데이터 분석 기능을 제공하는 라이브러리로 csv, xls 파일 등의 데이터를 읽고 원하는 데이터 형식으로 변환해줍니다.

자주 사용되는 라이브러리 중 하나로 주로 pd 라고 줄여 사용하게 됩니다.

##### 1. Series

pd.Series는 1차원 데이터를 다룰 때 사용합니다. 변수를 출력해보면 인덱스 번호와 이름, 자료형도 함께 출력됩니다.

##### 2. DataFrame

DataFrame은 Series와 달리 여러개의 column을 가질 수 있습니다.

DataFrame을 정의할 때는 2차원 리스트를 매개 변수로 전달하며 여러개의 Series 데이터를 합쳐 DataFrame을 만들 수도 있습니다.

------

**Series/ DataFrame 생성 함수**

- Series(data, name): data를 name 이라는 이름의 Series형태로 만들어 줍니다.
- DataFrame(data): data를 DataFrame 구조로 만들어 줍니다.



#### 실습

1. 1차원 데이터를 Series 형태로 만들어 보세요.
2. Dictionary 데이터를 Series 형태로 만들어 보세요.
3. 2차원 데이터를 DataFrame 형태로 만들어 보세요.

```python
import pandas as pd

def main():
    # Series()를 사용하여 1차원 데이터를 만들어보세요.
    # 5개의 age 데이터와 이름을 age로 선언해보세요.
    data = [19, 18, 27, 22, 33]
    age = pd.Series(data, name = "age")
    
    # Python Dictionary 형태의 데이터가 있습니다.
    # class_name 데이터를 Series로 만들어보세요.
    class_name = {'국어' : 90,'영어' : 70,'수학' : 100,'과학' : 80}
    class_name = pd.Series(class_name)
    print(class_name,'\n')
    
    
    # DataFrame 만들기
    # DataFrame()을 사용하여 2차원 데이터를 생성해보세요.
    # index와 columns 값을 설정해보세요.
    data=[['name', 'age'],['철수',15],['영희',23],['민수',20],['다희', 18],['지수',20]]
    data = pd.DataFrame(data)
    print(data,'\n')
    
    
if __name__ == "__main__":
    main()
```

```python
# 결과
국어     90
영어     70
수학    100
과학     80
dtype: int64 

      0    1
0  name  age
1    철수   15
2    영희   23
3    민수   20
4    다희   18
5    지수   20 

코드 실행이 완료되었습니다.
```





#### 2. Pandas 데이터 추출 및 추가

DataFrame에서 원하는 데이터를 추출하기 위해 loc(), iloc() 기능을 사용할 수 있습니다.

- `loc()`: 명시적인 인덱스를 참조하는 인덱싱/슬라이싱
- `iloc()` : 정수 인덱스 인덱싱/슬라이싱. 단 iloc의 경우 리스트와 같이 마지막 인덱스는 포함되지 않습니다.

`loc`, `iloc` 함수에 Index 값을 입력하여 원하는 데이터 인덱스를 추출/ 추가할 수 있습니다.



#### 3. Pandas 데이터 삭제

`drop()` 기능을 이용하여 DataFrame의 Index 및 Column을 삭제할 수도 있습니다.

- `drop()` : index, column 삭제

`drop()`함수에 Index 값을 입력하여 원하는 데이터 인덱스를 삭제할 수 있습니다.



#### 실습

1. `human` DataFrame을 만들어보세요.
2. `loc()` , `iloc()` 을 이용해 `age`를 추출해보세요.
3. `loc()` , `iloc()`을 이용해 `weight`와 `height`만 추출해보세요.
4. 새로운 데이터 `sex`를 `human`에 추가해보세요.
5. `drop()`으로 `human`에서 `height`를 삭제해보세요.

```python
from elice_utils import EliceUtils
elice_utils = EliceUtils()
import pandas as pd

a = pd.Series([20, 15, 30, 25, 35], name='age')
b = pd.Series([68.5, 60.3, 53.4, 74.1, 80.7], name='weight')
c = pd.Series([180, 165, 155, 178, 185], name ='height')
human = pd.DataFrame([a, b, c])

def main():
    print(human)
    # loc(), iloc() 함수를 이용하여 특정 행, 열 추출 
    print(human.loc['age'],'\n')
    print(human.iloc[0],'\n')
    
    # loc(), iloc() 함수를 이용하여 데이터의 특정 범위 추출
    print(human.loc['weight' : 'height'],'\n')
    print(human.iloc[1:3],'\n')
     
    sex = ['F','M','F','M','F']
    # 새로운 데이터 추가하기
    human.loc['sex'] = sex 
    print(human,'\n')
    
    #원하는 행/열 데이터 삭제하기
    tmp = human.drop(['height'])
    print(tmp,'\n')


if __name__ == "__main__":
    main()
```

```python
# 결과
           0      1      2      3      4
age      20.0   15.0   30.0   25.0   35.0
weight   68.5   60.3   53.4   74.1   80.7
height  180.0  165.0  155.0  178.0  185.0
0    20.0
1    15.0
2    30.0
3    25.0
4    35.0
Name: age, dtype: float64 

0    20.0
1    15.0
2    30.0
3    25.0
4    35.0
Name: age, dtype: float64 

            0      1      2      3      4
weight   68.5   60.3   53.4   74.1   80.7
height  180.0  165.0  155.0  178.0  185.0 

            0      1      2      3      4
weight   68.5   60.3   53.4   74.1   80.7
height  180.0  165.0  155.0  178.0  185.0 

           0     1     2     3     4
age       20    15    30    25    35
weight  68.5  60.3  53.4  74.1  80.7
height   180   165   155   178   185
sex        F     M     F     M     F 

           0     1     2     3     4
age       20    15    30    25    35
weight  68.5  60.3  53.4  74.1  80.7
sex        F     M     F     M     F 

코드 실행이 완료되었습니다.
```

