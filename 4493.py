# 가위 바위 보는 두 명이서 하는 게임이다. 보통 미리 정해놓은 수 만큼 게임을 하고, 많은 게임을 이긴 사람이 최종 승자가 된다.

# 가위 바위 보를 한 횟수와 매번 두 명이 무엇을 냈는지가 주어졌을 때, 최종 승자를 출력하는 프로그램을 작성하시오.

# 바위는 가위를 이긴다.
# 가위는 보를 이긴다.
# 보는 바위를 이긴다.

# 1차 작성한 코드
t = int(input())
for i in range(t):
    n = int(input())
    a_cnt = 0
    b_cnt = 0
    for i in range(n):
        a, b = input().split()
        
        if (a == "R" and b == "S") or (a == "P" and b == "R") or (a == "S" and b == "P"):
            a_cnt += 1
        elif (a == "R" and b == "P") or (a == "S" and b == "R") or (a == "P" and b == "S"):
            b_cnt += 1
        else:
            a_cnt += 1
            b_cnt += 1
        
    if a_cnt > b_cnt:
        print("Player 1")
    elif a_cnt < b_cnt:
        print("Player 2")
    else:
        print("TIE")

# 2차 작성한 코드
t = int(input())
for i in range(t):
    n = int(input())
    a_cnt = 0
    b_cnt = 0
    for i in range(n):
        a, b = input().split()
        
        if a == b:
            continue
        elif (a == "R" and b == "S") or (a == "P" and b == "R") or (a == "S" and b == "P"):
            a_cnt += 1
        else:
            b_cnt += 1
        
    if a_cnt > b_cnt:
        print("Player 1")
    elif a_cnt < b_cnt:
        print("Player 2")
    else:
        print("TIE")