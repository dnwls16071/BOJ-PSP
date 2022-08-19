# 어떤 수 X가 주어졌을 때, X의 모든 자리수가 역순이 된 수를 얻을 수 있다. Rev(X)를 X의 모든 자리수를 역순으로 만드는 함수라고 하자. 예를 들어, X=123일 때, Rev(X) = 321이다. 그리고, X=100일 때, Rev(X) = 1이다.
# 두 양의 정수 X와 Y가 주어졌을 때, Rev(Rev(X) + Rev(Y))를 구하는 프로그램을 작성하시오

# 함수를 사용하여 내가 작성한 코드
def Rev(n):
    n = str(n)
    num = n[::-1]
    num = int(num)
    return num

X, Y = map(int, input().split())
print(Rev(Rev(X) + Rev(Y)))

# 함수를 사용하지않고 내가 작성한 코드
X, Y = map(str, input().split())

x = int(X[::-1])
y = int(Y[::-1])
result = x + y
result = str(result)

print(int(result[::-1]))
