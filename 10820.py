# 문자열 N개가 주어진다. 이때, 문자열에 포함되어 있는 소문자, 대문자, 숫자, 공백의 개수를 구하는 프로그램을 작성하시오.

# 각 문자열은 알파벳 소문자, 대문자, 숫자, 공백으로만 이루어져 있다.

# 이 문제는 입력값의 개수, 즉 T(테스트케이스)가 주어지지 않았으므로 while문으로 무한 루프를 돌린다.
# EOF Error(더 이상 입력값이 없는 상황)인 상황만 제외하고 돌아가도록 예외처리를 해야한다.

# 입력값이 주어진다면 그에 맞게끔 조건식을 세우고 코드를 작성
# 입력값이 주어지지 않는 상황이라면 while문을 최우선으로 생각하여 코드를 작성
while True:
    try:
        text_list = list(input())
        Lower = 0
        Upper = 0
        number = 0
        cnt = 0
        for i in text_list:
            for j in i:
                if j in "abcdefghijklmnopqrstuvwxyz":
                    Lower += 1
                elif j in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                    Upper += 1
                elif j in "0123456789":
                    number += 1
                elif j == " ":
                    cnt += 1
        print(Lower, Upper, number, cnt)
    except EOFError:
        break