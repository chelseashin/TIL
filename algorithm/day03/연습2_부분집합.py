'''
n개의 정수를 입력 받아 부분집합의 합이 0이 되는 것이 존재하는지를 계산하는 함수를 작성해보자.
'''
arr = [-7, -3, -2, 5, 8]
sum = 0
cnt = 0
for i in range(1, 1 << len(arr)):        # 1<<n : 부분 집합의 개수
    sum = 0
    for j in range(len(arr)):            # 원소의 수만큼 비트를 비교함
        if i & (1 << j): sum += arr[j]   # i의 j번째 비트가 1이면 j번재 원소 출력

    if sum == 0:
        cnt += 1
        for j in range(len(arr)):
            if i & (1 << j):
                print(arr[j], end= " ")
        print()
print("개수 : {}".format(cnt))