Daily Homework 

대전 2반 17번 신채원

2019-01-08



< 함수 >

1. List는 for 문을 실행하면 모든 요소를 순차적으로 돌면서 반복문을 수행합니다.
     임의의 리스트 my_list의 값을 하나씩 출력하는 코드를 아래에 작성하시오.

  ```python
  my_list = list(range(1, 11))
  for i in a:
      print(i)
      
      
  < 결과 >
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  ```

2. 위에 작성한 코드를 인덱스(index) 값과 함께 출력하는 코드로 변경하시오.

   ```python
   for x, y in enumerate(my_list):
       print(x, y)
       
       
   < 결과 >
   0 1
   1 2
   2 3
   3 4
   4 5
   5 6
   6 7
   7 8
   8 9
   9 10
   ```

3. 딕셔너리는 key, value로 구성되어 있습니다. 따라서, 딕셔너리 my_dict 각각의 상
     황에 따라 반복문을 수행할 수 있도록 빈칸을 채우시오.
       key : for key in ```my_dict.keys()```:
       value : for value in ```my_dict.values()```:
       key와 value : for key, value in ```my_dict.items()```:



4. result에 저장된 값은?  

   => return값이 없기 때문에 result에 저장된 값이 없다

   => 답 : None

   ```python def my_func(a, b):
   def my_func(a, b):
       c = a + b
       print(c)
       
   result = my_func(1, 5)
   print(result)
   
   < 결과 >
   6
   None
   ```