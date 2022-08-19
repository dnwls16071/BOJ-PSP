# 2018 SCAL-MOOKJA에 출전하기로 한 무근이와 인서는 대회 준비를 위해 같이 모여 문제를 풀기로 했다.

# 그런데 어느 날, 일어나서 날짜를 확인해 보니 무근이와 인서의 시계가 서로 다른 날짜를 가리키고 있었다. 두 사람이 정확한 날짜에 모일 수 있도록 문제를 푸는 지금 시각이 UTC+0(세계 표준시)을 기준으로 무슨 날짜인지 출력해 주는 프로그램을 작성하자.

# 만약 서울에서 확인한 시각이 2018년 9월 29일 오후 2시 정각이라면 UTC+0 기준의 시각은 2018년 9월 29일 오전 5시 정각이다.

import datetime
now = datetime.datetime.now() + datetime.timedelta(hours=9) #한국시간으로 나오니 수정해준다

print(now.year)
print(now.month)
print(now.day)