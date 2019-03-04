import sys
sys.stdin = open("연습1.txt")

V, E = map(int, input().split())
print(V, E)
tree = [[0 for _ in range(3)] for i in range(V+1)]
print(tree)
temp = list(map(int, input().split()))

# 전위순회
def preorder(node):
    if node != 0:
        print("{}".format(node), end =" ")
        preorder(tree[node][0])
        preorder(tree[node][1])

# 중위순회
def inorder(node):
    if node != 0:
        inorder(tree[node][0])
        print("{}".format(node), end=" ")
        inorder(tree[node][1])

# 후위순회
def postorder(node):
    if node != 0:
        postorder(tree[node][0])
        postorder(tree[node][1])
        print("{}".format(node), end=" ")

def printTree():
    for i in range(1, V+1):
        print("%2d %2d %2d %2d" % (i, tree[i][0], tree[i][1], tree[i][2])


for i in range(E):
    n1 = temp[i*2]
    n2 = temp[i*2 + 1]
    if not tree[n1][0]:
        tree[n1][0] = n2
    else:
        tree[n1][1] = n2
    tree[n2][2] = n1

printTree()
print("전위순회 : ", end="")
preorder(1)
print()

printTree()
print("중위순회 : ", end="")
inorder(1)
print()

printTree()
print("후위순회 : ", end="")
postorder(1)
print()