# 부분집합
bit = [0,0,0,0]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print(bit)

# 부분집합 2
arr = [1, 2, 3]
n = len(arr)
for i in range(1 << n):     # 1<<n : 부분 집합의 개수
    for j in range(n):      # 원소의 수만큼 비트를 비교함
        if i & (1 << j):    # i의 j번째 비트가 1이면 j번재 원소 출력
            print(arr[j], end = ', ')
    print()
print()



# 부분집합(Subset Sum) 문제

arr = [-7, -3, -2, 5, 8]
sum = 0
cnt = 0
for i in range(1, 1 << len(arr)):
    sum = 0
    for j in range(len(arr)):
        if i & (1 << j):
            sum += arr[j]

    if sum == 0:
        cnt += 1
        for j in range(len(arr)):
            if i & (1 << j):
                print(arr[j], end =" ")
        print()

print("개수 : {}".format(cnt))