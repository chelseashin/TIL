import sys
sys.stdin = open("종이붙이기.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    # print(N)    # 30, 50, 70
    #  [1, 3, 5, 11, 21, ... ] 순으로 행렬 존재 => 점화식 찾기

    result = [1, 3]
    for i in range(2, N // 10):
        # 점화식 : i =  i-2번째 값 * 2 + i-1번째 값
        i = result[i-2] * 2 + result[i-1]
        result.append(i)

    print(f"#{tc + 1} {result[-1]}")