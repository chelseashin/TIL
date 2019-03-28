import sys
sys.stdin = open("02.txt")

def pack(ni):
    global cnt
    ni.insert(0, ni.pop(0) + ni.pop(0))
    cnt += ni[0]

N = int(input())
ni = list(map(int, input().split()))
ni.sort()
cnt = 0
while len(ni) >= 2:
    pack(ni)
print(cnt)