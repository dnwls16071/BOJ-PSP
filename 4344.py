# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

C = int(input())

for i in range(C):
    lst = list(map(int, input().split()))
    average = sum(lst[1:]) / lst[0]

    cnt = 0
    for j in lst[1:]:
        if j > average:
            cnt += 1
       
    rate = (cnt / lst[0]) * 100
    print('%0.3f' % rate + "%")