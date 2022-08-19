# 오늘은 2007년 1월 1일 월요일이다. 그렇다면 2007년 x월 y일은 무슨 요일일까? 이를 알아내는 프로그램을 작성하시오.

# x월 y일의 x, y를 입력받는다.
x, y = map(int, input().split())
# 각 달의 마지막 날을 저장해놓은 리스트
final_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 요일 출력
day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

Day = 0
for i in range(x-1):
    Day += final_day[i]

Day = (Day + y) % 7

print(day[Day])