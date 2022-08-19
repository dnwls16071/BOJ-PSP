# 입력으로 주어지는 문자열에서 연속으로 3개의 문자가 JOI 또는 IOI인 곳이 각각 몇 개 있는지 구하는 프로그램을 작성하시오. 문자열은 알파벳 대문자로만 이루어져 있다. 예를 들어, 아래와 같이 "JOIOIOI"에는 JOI가 1개, IOI가 2개 있다.


string = input()

JOI_cnt = 0
IOI_cnt = 0

for i in range(len(string)-2):
    answer = ""
    answer += string[i] + string[i+1] + string[i+2]

    if answer == "JOI":
        JOI_cnt += 1
    if answer == "IOI":
        IOI_cnt += 1

print(JOI_cnt)
print(IOI_cnt)