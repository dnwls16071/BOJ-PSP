# 원룡이는 한 컴퓨터 보안 회사에서 일을 하고 있다. 그러던 도중, 원룡이는 YESWOA.COM 으로부터 홈페이지 유저들의 비밀키를 만들라는 지시를 받았다. 원룡이는 비밀 키를 다음과 같은 방법으로 만들었다.
#
# 개인마다 어떤 특정한 소수 p와 q를 주어 두 소수의 곱 pq를 비밀 키로 두었다. 이렇게 해 주면 두 소수 p,q를 알지 못하는 이상, 비밀 키를 알 수 없다는 장점을 가지고 있다.
#
# 하지만 원룡이는 한 가지 사실을 잊고 말았다. 최근 컴퓨터 기술이 발달함에 따라, 소수가 작은 경우에는 컴퓨터로 모든 경우의 수를 돌려보아 비밀 키를 쉽게 알 수 있다는 것이다.
#
# 원룡이는 주성조교님께 비밀 키를 제출하려던 바로 직전에 이 사실을 알아냈다. 그래서 두 소수 p, q 중 하나라도 K보다 작은 암호는 좋지 않은 암호로 간주하여 제출하지 않기로 하였다. 이것을 손으로 직접 구해보는 일은 매우 힘들 것이다. 당신은 원룡이를 도와 두 소수의 곱으로 이루어진 암호와 K가 주어져 있을 때, 그 암호가 좋은 암호인지 좋지 않은 암호인지 구하는 프로그램을 작성하여야 한다.

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    P, K = map(int, input().split())

    lst = []
    for i in range(2, P):
        if P % i == 0:
            if i > P // i:
                tmp_up = i
                tmp_down = P // i
                lst.append([tmp_down, tmp_up])
                break
            else:
                tmp_up = P // i
                tmp_down = i
                lst.append([tmp_down, tmp_up])
                break
    else:
        print("GOOD")

    if len(lst) > 0:
        for i in lst:
            if i[0] < K:
                print("BAD", i[0])

# 위와 같이 작성한 코드의 채점 결과는 시간초과였다.
# 아무래도 탐색범위가 넓다보니 당연히 나올수밖에 없는 결과로 보여진다.

P, K = map(int, input().split())
flag = True
for i in range(2, K):
    if P % i == 0:
        print("BAD", i)
        flag = False
        break

if flag == True:
    print("GOOD")

# K보다 작은 암호가 나오면 좋지 못한 암호가 된다는 점에서 힌트를 얻었다.
# P를 2부터 K-1까지의 값으로 나누었을때 만약 나눠떨어진다면 좋지 못한 암호가 되므로 BAD와 해당 i값을 출력한다.
# 부울연산자를 이용한 방법을 사용하여 만약에 초기값 그대로 나온다면 좋은 암호라는 뜻이므로 GOOD를 출력한다.
