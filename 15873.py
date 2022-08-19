# 자연수 A, B가 주어지면 A+B를 구하는 프로그램을 작성하시오.

N = input()

if len(N) == 2:
    print(int(N[0]) + int(N[1]))
elif len(N) == 4:
    print(20)
else:   # len(N) == 3인 경우에 해당
    if N[1] == "0":     # ex >> 302인 경우
        print(int(N[0]) * 10 + int(N[2]))
    elif N[-1] == "0":  # ex >> 320인 경우
        print(int(N[0]) + int(N[1]) * 10) 