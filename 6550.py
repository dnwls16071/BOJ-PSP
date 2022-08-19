# 2개의 문자열 s와 t가 주어졌을 때 s가 t의 부분 문자열인지 판단하는 프로그램을 작성하라. 부분 문자열을 가지고 있는지 판단하는 방법은 t에서 몇 개의 문자를 제거하고 이를 순서를 바꾸지 않고 합쳤을 경우 s가 되는 경우를 이야기 한다.

# 1차 작성코드
while True:
    try:
        s, t = input().split()
        value = 0
        flag = 0
        for i in range(len(t)):    
            if t[i] == s[value]:
                value += 1
                if value == len(s):
                    flag = 1
                    break
        if flag == 1:
            print("Yes")
        else:
            print("No")
    except:
        break

# 2차 작성코드
def solution(s, t):
    value = 0
    for i in range(len(t)):
        if t[i] == s[value]:
            value += 1
            if value == len(s):
                return "Yes"
    return "No"

while True:
    try:
        s, t = input().split()
        answer = solution(s, t)
        print(answer)
    except:
        break

    