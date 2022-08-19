# 아래 예제 출력과 같은 J박스를 출력하는 프로그램을 작성하시오.

for _ in range(int(input())):
    number = int(input())
    for i in range(number):
        if i == 0:
            print("#"*number)
        elif i != 0 and i != number-1:
            print("#" + "J"*(number-2) + "#")
        else:
            print("#"*number)
    print()
