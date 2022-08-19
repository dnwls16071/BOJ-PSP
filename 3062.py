# 수 124를 뒤집으면 421이 되고 이 두 수를 합하면 545가 된다. 124와 같이 원래 수와 뒤집은 수를 합한 수가 좌우 대칭이 되는지 테스트 하는 프로그램을 작성하시오.

T = int(input())

for i in range(T):
    N = input()
    res = int(N) + int(N[::-1])
    if str(res) == str(res)[::-1]:    
        print("YES")
    else:
        print("NO")