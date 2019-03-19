# 연습문제3

asc = [[0,0,0,0],  # 0
       [0,0,0,1],  # 1
       [0,0,1,0],  # 2
       [0,0,1,1],  # 3
       [0,1,0,0],  # 4
       [0,1,0,1],  # 5
       [0,1,1,0],  # 6
       [0,1,1,1],  # 7
       [1,0,0,0],  # 8
       [1,0,0,1],  # 9
       [1,0,1,0],  # A
       [1,0,1,1],  # B
       [1,1,0,0],  # C
       [1,1,0,1],  # D
       [1,1,1,0],  # E
       [1,1,1,1]]  # F

password = [[0,0,1,1,0,1],  #0
            [0,1,0,0,1,1],  #1
            [1,1,1,0,1,1],  #2
            [1,1,0,0,0,1],  #3
            [1,0,0,0,1,1],  #4
            [1,1,0,1,1,1],  #5
            [0,0,1,0,1,1],  #6
            [1,1,1,1,0,1],  #7
            [0,1,1,0,0,1],  #8
            [1,0,1,1,1,1]]  #9

def xtoo(x):
    if x <= '9':
        return ord(x) - ord('0')
    else:
        return ord(x) - ord('A') + 10

def otob(x):
    global B
    for i in range(4):
        B.append(asc[x][i])

# A = '0DEC'
A = '0269FAC9A0'
# 0000 1111 1001 0111 1010 0011
B = []

for i in range(len(A)):
    otob(xtoo(A[i]))

def findp(x):
    for i in range(10):
        cnt = 0
        for j in range(6):
            if x+j > len(B)-1:
                return 0
            if B[x+j] == password[i][j]:
                cnt += 1
            else:
                break
        if cnt == 6:
            ans.append(i)
            return 6
    return 0

id = 0
ans = []
while id < len(B):
    a = findp(id)
    if a == 0:
        id += 1
    else:
        id += a
print(*ans)
