# 입력 받은 대로 출력하는 프로그램을 작성하시오.

# 계속 진행되는 반복문을 만들고 그 안에서 try~except를 사용하여 예외를 처리한다.
# 입력이 있을 땐 계속 입력을 받아와서 연산을 진행하고, EOFError가 발생하면 반복문을 빠져나오도록한다.
# 입력 도중에 파일의 끝을 만나면 EOFerror가 발생합니다.

while True:
    try:
        print(input())
    except EOFError:
        break