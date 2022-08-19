# 상근이는 이진수 곱셈에 어려움을 겪는 여자친구를 위한 프로그램을 만들려고 한다.

# 상근이의 여자친구는 항상 이진수에 17을 곱한다. 즉, 이진수 N이 입력으로 들어오면 17을 곱한 다음 이진수로 출력하는 프로그램을 작성하시오.

# # 1차 작성한 코드(내장함수 이용)
N = int(input(), 2)
print(bin(N*17)[2:])

# 진법 변환 코드(함수)
def converter(a, b):
    answer = " "
    temp = list("0123456789ABCDEF")
    if a == 0:
        answer = "0"
    else:
        while a != 0:
            answer += temp[a % b]
            a //= b
    return answer[::-1]
