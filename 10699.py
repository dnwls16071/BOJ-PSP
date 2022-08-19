# 서울의 오늘 날짜를 출력하는 프로그램을 작성하시오.

import datetime # 날짜 모듈을 사용해야하는 경우 datetime을 사용
now = datetime.datetime.now() # 현재의 시간을 가지는 객체인 now를 생성

#특정 형식으로 입력하고자 한다면 객체.strftime과 출력형식 %Y, %m, %d, %H, %M, %S 사용
nowDate = now.strftime("%Y-%m-%d") # 특정한 형식으로 입력하고자 한다면 strftime
print(nowDate)