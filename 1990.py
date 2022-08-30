# 151은 소수이면서 동시에 팰린드롬이기 때문에 소수인 팰린드롬이다. 팰린드롬이란 앞으로 읽어나 뒤로 읽으나 같은 수를 말한다. 예를 들어 1234는 앞으로 읽으면 1234지만, 뒤로 읽으면 4321이 되고 이 두 수가 다르기 때문에 팰린드롬이 아니다. 두 정수 a, b가 주어졌을 때, a이상 b이하인 소수인 팰린드롬을 모두 구하는 프로그램을 작성하시오.

# Code1
import sys
input = sys.stdin.readline

def isPalindrome(x):
    x = str(x)
    if x == x[::-1]:
        return True
    else:
        return False

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

# 10000000을 넘는 수 중에는 팰린드롬 넘버가 존재하지않는다.
# 따라서 10000000을 넘는 수는 10000000으로 초기화해주면 된다.
def check(a, b):
    if b > 10000000:
        b = 10000000
    Palindrome = [i for i in range(a, b+1) if isPalindrome(i)]
    Prime = [i for i in Palindrome if isPrime(i)]
    for i in Prime:
        print(i)
    print(-1)

a, b = map(int, input().split())
check(a, b)

# 처음에 Palindrome과 Prime_number를 판별하는 함수를 작성할때 for문과 if문을 활용했었는데 시간 초과가 발생했다.
# 다른 코드를 참고했는데 대부분 리스트 내포(list comprehension)를 사용해서 코드를 작성했다.
# List Comprehension을 사용하면 반복문의 속도가 훨씬 빠르고 간결해진다.
