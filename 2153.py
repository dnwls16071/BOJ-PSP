# 소수란 1과 자기 자신으로만 나누어떨어지는 수를 말한다. 예를 들면 1, 2, 3, 5, 17, 101, 10007 등이 소수이다. 이 문제에서는 편의상 1도 소수로 하자.

# 알파벳 대소문자로 이루어진 영어 단어가 하나 있을 때, a를 1로, b를 2로, …, z를 26으로, A를 27로, …, Z를 52로 하여 그 합을 구한다. 예를 들어 cyworld는 합을 구하면 100이 되고, abcd는 10이 된다.

# 이와 같이 구한 수가 소수인 경우, 그 단어를 소수 단어라고 한다. 단어가 주어졌을 때, 그 단어가 소수 단어인지 판별하는 프로그램을 작성하시오.

# Tip) chr(65) = A, chr(90) = Z, chr(97) = a, chr(122) = z

def isPrime(x):
    if x == 1:
        return True
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
             return False
    return True

word = list(input())
tot = 0
for i in word:
    if i.islower():
        tot += ord(i) - 96
    else:
        tot += ord(i) - 38

if isPrime(tot):
    print("It is a prime word.")
else:
    print("It is not a prime word.")

# 이 문제.. 진짜 어이없어서 웃음만 나온 문제였다.
# 알고보니까 내가 들여쓰기를 잘못한것을 한참동안 못봐서 틀렸던 문제였다.
# 이딴 문제에 시간 쏟은게 ㄹㅇ 아깝네...