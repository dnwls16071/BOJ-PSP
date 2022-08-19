# A와 B가 한 오디션 프로의 결승전에 진출했다. 결승전의 승자는 심사위원의 투표로 결정된다.
# 심사위원의 투표 결과가 주어졌을 때, 어떤 사람이 우승하는지 구하는 프로그램을 작성하시오.

V = int(input()) #심사위원의 수
vote = input()

if vote.count("A") > vote.count("B"):
    print("A")
elif vote.count("A") < vote.count("B"):
    print("B")
elif vote.count("A") == vote.count("B"):
    print("Tie")