import sys
sys.stdin = open("이진탐색_input.txt")

# 중위순회
def inorder(node):
    if node != 0:
        inorder(tree[node][0])
        print("{}".format(node), end=" ")
        inorder(tree[node][1])


T = int(input())
for tc in range(T):
    N = int(input())
    tree = [0 for i in range(3)] for _ in range(N+1)

for i in range(E):
    n1 = temp[i * 2]
    n2 = temp[i * 2 + 1]
    if not tree[n1][0]:
        tree[n1][0] = n2
    else:
        tree[n1][1] = n2
    tree[n2][2] = n1


