# 트리찾기 - 전위순회
def searchTree(node):
    global count
    if node != 0:
        count += 1
        searchTree(tree[node][0])
        searchTree(tree[node][1])
    return count

import sys
sys.stdin = open("서브트리_input.txt")

T = int(input())
for tc in range(T):
    E, N = map(int, input().split())
    temp = list(map(int, input().split()))
    tree = [[0 for _ in range(3)] for _ in range(E+2)]
    count = 0

    for i in range(E):
        n1 = temp[i * 2]     # 왼쪽 노드
        n2 = temp[i * 2 + 1] # 오른쪽 노드
        if not tree[n1][0]:  # 값이 비어있으면 왼쪽값을 넣는다
            tree[n1][0] = n2
        else:  # 왼쪽값이 채워져 있으면 오른쪽 값을 넣는다
            tree[n1][1] = n2
        tree[n2][2] = n1  # 부모값 채우기

    # print(tree)
    print("#{} {}".format(tc+1, searchTree(N)))