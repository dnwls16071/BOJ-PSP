# 고창영은 맨날 오타를 낸다. 창영이가 오타를 낸 문장과 오타를 낸 위치가 주어졌을 때, 오타를 지운 문자열을 출력하는 프로그램을 작성하시오.

# 창영이는 오타를 반드시 1개만 낸다.

T = int(input())

for i in range(T):
    num, string = input().split()
    num = int(num)
    print(string[:num-1], string[num:], sep = "")