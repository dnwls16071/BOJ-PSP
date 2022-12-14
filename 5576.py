# 최근 온라인에서의 프로그래밍 콘테스트가 열렸다. W 대학과 K 대학의 컴퓨터 클럽은 이전부터 라이벌 관계에있어,이 콘테스트를 이용하여 양자의 우열을 정하자라는 것이되었다.
# 이번이 두 대학에서 모두 10 명씩이 콘테스트에 참여했다. 긴 논의 끝에 참가한 10 명 중 득점이 높은 사람에서 3 명의 점수를 합산하여 대학의 득점으로하기로 했다.
# W 대학 및 K 대학 참가자의 점수 데이터가 주어진다. 이때, 각각의 대학의 점수를 계산하는 프로그램을 작성하라.

# sorted, reversed 등을 사용하여 정렬의 새로운 리스트를 반환할 수 있다.
# sort, reverse 등을 사용해서 기존의 리스트를 정렬된 상태로 변경할 수 있다.
# 기존과 새로운 것에 차이가 있다는 것에 초점을 맞출것
score_W = sorted([int(input()) for _ in range(10)])[7:]
score_K = sorted([int(input()) for _ in range(10)])[7:]
print(sum(score_W), sum(score_K))

# 리스트 내포(list comprehension)
# list 이름 = [표현식 for 변수 in 반복 가능한 대상 (조건문)]
# ※참고로 조건문은 필수가 아니어서 () 표시해놓은것