#준희는 자기가 팀에서 귀여움을 담당하고 있다고 생각한다. 하지만 연수가 볼 때 그 의견은 뭔가 좀 잘못된 것 같았다. 그렇기에 설문조사를 하여 준희가 귀여운지 아닌지 알아보기로 했다.

#참고 코드
N = int(input())

count = 0
for _ in range(N):
    a = int(input())
    if a == 0:
        count += 1

if (N / 2) > count:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")

#다른 방법으로 작성한 코드
N = int(input())

cute = 0
not_cute = 0
for _ in range(N):
    a = int(input())
    if a == 0:
        not_cute += 1
    elif a == 1:
        cute += 1

if cute > not_cute:
    print("Junhee is cute!")
elif cute < not_cute:
    print("Junhee is not cute!")