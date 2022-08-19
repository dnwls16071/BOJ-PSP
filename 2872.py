# 국민대학교에서는 매 학기 시작 전 종합정보시스템에서 수강신청을 한다. 매 수강신청마다 아주 많은 학생들이 몰려 서버에 많은 부하가 가기 때문에, 국민대학교에서는 수강신청 부하 관리 시스템을 도입하기로 결정하였다. 새로운 관리 시스템은 다음과 같은 방식으로 동작한다.

# 수강신청 버튼이 활성화 된 후, 수강신청 버튼을 조금이라도 빨리 누른 학생이 대기목록에 먼저 들어간다.
# 이미 대기열에 들어가 있는 상태에서 다시 수강신청 버튼을 누를 경우 대기목록의 맨 뒤로 밀려난다.
# 잠시 후 수강신청 버튼이 비활성화 되면, 대기목록에서 가장 앞에 있는 학생부터 자동으로 수강신청이 완료되며, 수강 가능 인원이 꽉 찰 경우 나머지 대기목록은 무시하고 수강신청을 종료한다.


# 위의 표는 최대 수강 가능 인원이 3명인 알고리즘 수업에 대해 6명의 학생이 수강신청을 진행한 모습이다. 버튼이 비활성화 된 후, 먼저 규칙 1을 적용하여 클릭을 2번 이상 한 학생의 중복된 대기목록을 삭제한다. 중복된 목록을 제거한 후, 맨 앞에서부터 최대 수강 가능 인원인 3명을 선정한다. 표의 맨 오른쪽에는 그 최종결과를 나타낸 모습이다. 이와 같은 방법을 이용하여 최종적으로 수강신청에 성공한 인원을 출력하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline
K, L = map(int, input().split())

sugang = []
for i in range(L):
    sugang.append(input())

update_sugang = []
for k in sugang:
    if k not in update_sugang:
        update_sugang.append(k)
    else:
        continue

for j in range(K):
    print(update_sugang[j])