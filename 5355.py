# 겨울 방학에 달에 다녀온 상근이는 여름 방학 때는 화성에 갔다 올 예정이다. (3996번) 화성에서는 지구와는 조금 다른 연산자 @, %, #을 사용한다. @는 3을 곱하고, %는 5를 더하며, #는 7을 빼는 연산자이다. 따라서, 화성에서는 수학 식의 가장 앞에 수가 하나 있고, 그 다음에는 연산자가 있다.

T = int(input())

for _ in range(T):
    a = list(input().split())
    num = float(a.pop(0))   #a.pop(0) > a리스트의 0번째에 위치한 값을 내놓고 리턴
    for i in range(len(a)):
        if a[i] == "@":
            num *= 3
        elif a[i] == "%":
            num += 5
        elif a[i] == "#":
            num -= 7

    print("%0.2f" % num)
