# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 1차 작성 코드(시간초과)
# 시간초과가 발생한 원인 : 브루트 포스(Brute Force)로 인한 너무 많은 탐색이 시간 초과를 불러왔다고 판단했다.
import sys
input = sys.stdin.readline
M, N = map(int, input().split())
cnt = 0
prime_number = []
for i in range(M, N+1):
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
        
    if cnt == 2:
        prime_number.append(i)
        cnt = 0
    else:
        cnt = 0

for k in prime_number:
    print(k)
    
# 탐색의 범위를 좁히는 방법을 고민해보다가 제곱근의 개념을 이용하게되었다.

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    M, N = map(int, input().split())
    prime_number = []
    for i in range(M, N+1):
        if i == 1:
            continue
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                break
        else:
            prime_number.append(i)
    
    for k in prime_number:
        print(k)