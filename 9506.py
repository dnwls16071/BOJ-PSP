# 어떤 숫자 n이 자신을 제외한 모든 약수들의 합과 같으면, 그 수를 완전수라고 한다. 
# 예를 들어 6은 6 = 1 + 2 + 3 으로 완전수이다.
# n이 완전수인지 아닌지 판단해주는 프로그램을 작성하라.
#join메소드 사용 + 리스트 내포 : "+".join(str(i) for i in lst)
while True:
    n = int(input())
    if n == -1:
        break
    
    lst = []
    for i in range(1, n):
        if n % i == 0:
            lst.append(i)
    if sum(lst) == n:
        print(n, "=", " + ".join(str(i) for i in lst))
    else:
        print(str(n) + " is NOT perfect.")

