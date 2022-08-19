# 2016년 5월 28일 제 2회 인하대학교 프로그래밍 경시대회(IUPC)가 개최된다. 이 대회는 다른 프로그래밍 경시대회와 다르게  손코딩으로 문제를 풀어야한다. CTP회장인 정은이는 모든 대회 참가자들에게 펜을 지급하기 위하여 펜을 구하기로 하였다. 대회 개최를 위한 예산을 아끼기 위하여 펜을 구매하지 않고 CTP회원들에게 펜을 빌리기로 하였다.

# CTP에는 N명의 회원들이 존재하며 각각의 회원들의 필통에 들어있는 펜의 개수는 모두 다르다. 정은이는 여러명의 회원에게 펜을 빌릴경우 펜을 돌려주기에 번거롭다고 생각하여 최소한의 회원들에게 펜을 빌려 참가자들에게 나누어 주려고 한다.

# 대회에 참가하는 참가자들은 팀을 구성해서 참가하는데 모든 팀원에게 펜을 지급해야한다. 한 팀이 k명의 팀원으로 구성되어 있을때 몇 명의 회원들에게 펜을 빌려야하는지 출력하시오.

# 1차 작성한 코드
N = int(input())
M, K = map(int, input().split())

pen = []
for _ in range(N):
    pen.append(int(input()))
pen.sort(reverse=True)

count = 0
for i in range(1, len(pen)):
    if M*K - sum(pen[0:i+1]) < 0:
        count += i
        break
print(count)

# 2차 작성한 코드
N = int(input())
M, K = map(int, input().split())
pen = list(map(int, input().split()))

count = 0
for i in range(1, len(pen)):
    if M*K - sum(pen[0:i+1]) < 0:
        count += i
        break
print(count)

# 참고한 코드
# n=int(input())
# m,k=map(int, input().split())
# cntPencil=m*k
# ctpList=sorted( list(map(int,input().split())) ,reverse=True)
# start=0
# currentPencil=0
# flag=0
# for i in ctpList:
#     currentPencil+=i
#     start+=1
#     if currentPencil>= cntPencil:
#         print(start)
#         flag=1
#         break
# if flag==0: print("STRESS")
