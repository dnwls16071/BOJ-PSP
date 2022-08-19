# 당신은 FCFS(First-Come, First-Served)의 규칙에 따라 요청된 일을 처리하는 서버를 담당하게 되었다. 매일, 당신은 일을 처리하기 위해 최대 T분 동안 서버에 시간을 할당할 수 있다. 당신은 오늘 주어진 시간동안 몇개의 일이 완료될 수 있는지 알고싶다.

# 예시를 들어보겠다. T = 180이고, 요청된 일들의 수행시간이 요청된 순으로 각각 45, 30, 55, 20, 80, 20분이다. 그러면, 단 4개의 일만이 완료될 수 있다. 처음 4개의 일의 수행시간은 150분으로 주어진 시간 내에 완료될 수 있지만, 처음 5개의 일의 수행시간은 230분으로 주어진 시간 180분보다 크기 때문에 완료될 수 없다. 처음 4개의 일을 수행한 뒤 6번째의 일을 수행해도 T를 초과하지 않지만 5번째 일을 수행할 수 없기 때문에 6번째 일을 수행할 수 없음을 참고해라.

# 1차 작성한 코드(런타임에러)
n, T = map(int, input().split())
work_time = list(map(int, input().split()))

res = 0 
cnt = 0
for i in work_time:
    res += i
    cnt += 1
    if res > T:
        ans = cnt - 1
        break
print(ans)

# 2차 작성한 코드(런타임에러)
n, T = map(int, input().split())
work_time = list(map(int, input().split()))

res = 0
cnt = 0
for i in work_time:
    res += i
    cnt += 1
    if res <= T:
        ans = cnt
print(ans)

# 3차 작성한 코드(런타임에러)
n, T = map(int, input().split())
work_time = list(map(int, input().split()))
res = 0
cnt = 0
for i in work_time:
    res += i
    cnt += 1
    if res <= T:
        ans = cnt
    else:
        break
print(ans)

# 4차 작성한 코드(정상처리 통과 코드)
n, T = map(int,input().split())
FCFS = list(map(int,input().split()))
r = 0
for i in FCFS:
    T -= i
    if T >= 0:
        r+=1
    else:
        break
print(r)