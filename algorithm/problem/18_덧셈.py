import sys
sys.stdin = open("덧셈.txt")

N = 3
for n in range(N):
    S, X = input().split()
# S = input()
# X = int(input())
# print(S[2:])    # 문자열 슬라이싱을 이용해야 함!

    for i in range(1, len(S)):
        if int(''.join(S[:i])) + int(''.join(S[i:])) == int(X):
            SA = int(''.join(S[:i]))
            SB = int(''.join(S[i:]))
            print("{}+{}={}".format(SA, SB, X))
            break
    else:
        print("NONE")



