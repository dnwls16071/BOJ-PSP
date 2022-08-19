# 텍스트에서 줄을 입력받은 뒤, 줄 번호를 출력하는 프로그램을 작성하시오.

N = int(input())

for i in range(1, N+1):
    sentence_lst = input()

    print(str(i) + ". " + sentence_lst)
    