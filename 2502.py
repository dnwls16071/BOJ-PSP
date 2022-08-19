# 춘향이는 편의점 카운터에서 일한다.
#
# 손님이 2원짜리와 5원짜리로만 거스름돈을 달라고 한다. 2원짜리 동전과 5원짜리 동전은 무한정 많이 가지고 있다. 동전의 개수가 최소가 되도록 거슬러 주어야 한다. 거스름돈이 n인 경우, 최소 동전의 개수가 몇 개인지 알려주는 프로그램을 작성하시오.
#
# 예를 들어, 거스름돈이 15원이면 5원짜리 3개를, 거스름돈이 14원이면 5원짜리 2개와 2원짜리 2개로 총 4개를, 거스름돈이 13원이면 5원짜리 1개와 2원짜리 4개로 총 5개를 주어야 동전의 개수가 최소가 된다.

# 1번 코드
n = int(input())

cnt = 0
while True:
    if n % 5 == 0:
        cnt += (n // 5)
        break
    else:
        n -= 2
        cnt += 1
    if n < 0:
        break
if n < 0:
    print(-1)
else:
    print(cnt)

# 처음에는 그리디 알고리즘에서 풀었던 문제가 생각나서 거스름돈의 값이 큰 경우부터 빼줬다.
# ex.13인 경우 5개가 출력되었다.
# 만약 5원짜리 동전으로 빼면 13원 거스름돈은 출력할 수 없다.
# 만약 2원자리 동전으로 빼면 2*4 + 5*1 = 13원 거스름돈을 출력할 수 있다.
# 따라서 이번엔 2원으로 빼줘야 가능하다.

