# 한상덕은 이번에 중덕 고등학교에 새로 부임한 교장 선생님이다. 교장 선생님으로서 첫 번째 일은 각 반의 수학 시험 성적의 통계를 내는 일이다.
# 중덕 고등학교 각 반의 학생들의 수학 시험 성적이 주어졌을 때, 최대 점수, 최소 점수, 점수 차이를 구하는 프로그램을 작성하시오.

K = int(input())

for i in range(K):
    lst = list(map(int, input().split()))
    del lst[0]
    lst.sort(reverse=True)
    diff = []
    print("Class", i+1)
    for i in range(len(lst)-1):
        diff.append(lst[i] - lst[i+1])
    
    print("Max", str(max(lst))+",", "Min", str(min(lst))+"," , "Largest gap", max(diff))

