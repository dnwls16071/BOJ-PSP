# 은민이는 4와 7을 좋아하고, 나머지 숫자는 싫어한다. 금민수는 어떤 수가 4와 7로만 이루어진 수를 말한다.

# N이 주어졌을 때, N보다 작거나 같은 금민수 중 가장 큰 것을 출력하는 프로그램을 작성하시오.

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    N = int(input())
    while True:
        flag = True
        for i in str(N):
            if i != "4" and i != "7":
                flag = False
                N -= 1
        if flag == True:
            print(N)
            break

# 4와 7로만 이루어진 숫자 : 44 47 74 77
# 입력값을 문자형으로 받아서 하나하나 조건문을 돌려야한다. 

# if __name__ == "__main__":
#     # Execute when the module is not initialized from an import statement.
#     main()

# __name__
# 모듈의 이름을 담고 있는 파이썬 내장 변수입니다.
# python.py 라는 파일이 있다면 __name__는 .py 확장자를 제외한 python이 됩니다.

# __main__
# __main__은 최상위 코드가 실행되는 환경의 이름입니다. "최상위 코드"는 프로그램 실행 시 첫 번째로 실행되는 Python 모듈입니다. 프로그램 구동에 필요한 다른 모듈들을 가져오기(import) 때문에 "최상위"라고 합니다.
# "최상위 코드"를 애플리케이션의 진입점(entry point)이라고도 합니다.
# 모듈은 __name__을 확인하여 최상위 환경에서 실행 중인지의 여부를 확인할 수 있습니다
# 모듈이 최상위 코드 환경에서 실행되면 해당 __name__은 '__main__' 문자열로 설정됩니다.
# Python 모듈 또는 패키지를 imort하면 __name__은 모듈 이름으로 설정됩니다. 일반적으로 .py 확장자가 없는 파일 이름입니다.