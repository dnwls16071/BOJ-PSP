# 테스트케이스(TestCase)'란 사용자가 제출한 코드가 옳은 답을 출력하는지 판단하기 위한 데이터다. 한 문제는 여러 개의 테스트케이스를 가지며, 문제를 '맞았다'는 것은 해당 문제의 모든 테스트케이스를 통과했다는 것을 의미한다. 즉, 하나의 테스트케이스라도 틀린다면 해당 문제는 틀린 것이 된다.

# 그림1. 실제 대회 시스템의 채점 방식을 나타내는 그림

# 테스트케이스 중 일부는 유저에게 공개되며, 일부는 공개되지 않는다. '샘플 테스트케이스'란 문제의 이해를 돕기 위해 유저에게 제공된 데이터다. 시스템이 코드를 채점할 때에는 이 외에도 공개되지 않은 '시스템 테스트케이스'를 통해 추가로 답을 검증한다. 따라서 유저는 코드를 작성할 때 제한 내의 모든 데이터를 고려해야 한다.

# 만영이는 샘플 테스트케이스만 맞으면 답을 제출하는 나쁜 버릇이 있다. 때문에 만영이의 정답률은 30%도 채 되지 않는다. 한 사이트의 아주대학교 유저 평균 정답률이 45%인 것을 감안하면 만영이는 학교 정답률에 엄청난 기여를 하고 있는 셈이다. 

# 무엇보다 준표를 힘들게 하는 건 아래와 같은 만영이의 말버릇이다.

# "맞았는데 왜 틀리죠?"
# 일명 '맞왜틀'이라고 불리는 이 현상은 문제풀이에 익숙하지 않거나, 자신의 코드에 자부심이 넘치는 사람들에게 종종 발생하며, "제가 만든 데이터는 되는데 왜 틀리죠?", "맞왜틀 맞왜틀 신나는 노래~~ 헤이! 나도 한 번 불러보자~~~" 등의 다양한 응용이 있다.

# 매번 만영이의 '맞왜틀'을 소스코드를 보거나 테스트케이스를 만들어 디버깅해주던 준표는 점점 지쳐갔다. 더 이상 만영이의 코드를 읽기 싫었던 준표는 문제의 테스트케이스를 빼내어 만영이에게 주었다. 모든 테스트케이스의 정답과 만영이의 코드가 생성한 답이 주어질 때 만영이의 결과를 예측해보자.

# 1차 작성한 코드(참고)
S1, S2 = map(int, input().split())
lst1 = [list(map(int, input().split())) for _ in range(S1)]
lst2 = [list(map(int, input().split())) for _ in range(S2)]
for i in range(S1):
    if lst1[i][0] != lst1[i][1]:
        print("Wrong Answer")
        # exit > 프로그램을 종료하는 데 사용할 수 있는 파이썬 내장함수
        exit()
for i in range(S2):
    if lst2[i][0] == lst2[i][1]:
        print("Why Wrong!!!")
        exit()
print("Accepted")

# 2차 작성한 코드
S1, S2 = map(int, input().split())
for i in range(S1):
    a, b = map(int, input().split())

    if a != b:
        print("Wrong Answer")
        exit()

for i in range(S2):
    c, d = map(int, input().split())
    if c != d:
        print("Why Wrong!!!")
        exit()

print("Accepted")