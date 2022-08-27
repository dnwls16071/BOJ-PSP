# 어떤 수를 왼쪽부터 읽어도, 오른쪽부터 읽어도 같을 때 이 수를 회문인 수라고 한다. 예를 들어, 747은 회문인 수이다. 255도 회문인 수인데, 16진수로 표현하면 FF이기 때문이다. 양의 정수를 입력받았을 때, 이 수가 어떤 B진법 (2 ≤ B ≤ 64)으로 표현하면 회문이 되는 경우가 있는지 알려주는 프로그램을 작성하시오. B진법이란, 한 자리에서 수를 표현할 때 쓸 수 있는 수의 가짓수가 B라는 뜻이다. 예를 들어, 십진법에서 B는 10이다.

def conv(a, b):
    ans = []
    while a != 0:
        ans.append(a % b)
        a //= b
    ans = ans[::-1]
    return ans

def isPalindrome(x):
    for i in range(len(x)//2):
        if x[i] != x[len(x)-i-1]:
            return False
    return True

T = int(input())
for _ in range(T):
    flag = False    # 회문이 될 수 있는지 없는지를 판단하는 Bool값
    N = int(input())
    for B in range(2, 65):
        if isPalindrome(conv(N, B)):
            flag = True
            break
    if flag:
        print(1)
    else:
        print(0)


