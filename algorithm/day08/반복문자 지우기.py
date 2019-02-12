import sys
sys.stdin = open("반복문자 지우기.txt")

T = int(input())
for tc in range(T):
    data = input()
    # print(data)
    # print(len(data))   # 5 10 21
    # print(data[0])     # A N U

    s = []
    for i in range(len(data)):
        if len(s) == 0:    # s에 아무것도 없는 경우
            s.append(data[i])
        else:   # 스택의 마지막 문자와 새로 들어오는 데이터 비교
            if s[-1] != data[i]:
                s.append(data[i])
            else:
                s.pop()
    print(f"#{tc + 1} {len(s)}")