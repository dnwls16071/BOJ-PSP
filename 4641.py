# 2~15개의 서로 다른 자연수로 이루어진 리스트가 있을 때, 이들 중 리스트 안에 자신의 정확히 2배인 수가 있는 수의 개수를 구하여라.

# 예를 들어, 리스트가 "1 4 3 2 9 7 18 22"라면 2가 1의 2배, 4가 2의 2배, 18이 9의 2배이므로 답은 3이다.

if __name__ == "__main__":
    while True:
        lst = list(map(int, input().split()))
        if lst[0] == -1:
            break
        lst.pop()   # 마지막 0은 리스트에 포함되어있지 않기 때문에 pop()을 사용하여 빼낸다.
        cnt = 0
        for i in lst:
            res = (i / 2)
            if res in lst:
                cnt += 1
        print(cnt)