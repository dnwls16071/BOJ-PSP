# 이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.
#
#
#
# 예를 들어 위와 같은 이진 트리가 입력되면,
#
# 전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
# 중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
# 후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트) 가 된다.

def preorder(root):
    if root != ".":
        print(root, end = "")
        preorder(tree[root][0])
        preorder(tree[root][1])

def inorder(root):
    if root != ".":
        inorder(tree[root][0])
        print(root, end = "")
        inorder(tree[root][1])

def postorder(root):
    if root != ".":
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end = "")

N = int(input())
tree = {}
for _ in range(N):
    root, left, right = map(str, input().split(" "))
    tree[root] = [left, right]

preorder("A")
print()
inorder("A")
print()
postorder("A")

# 대표적인 트리 순회 문제이다.