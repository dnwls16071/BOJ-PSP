# 5명의 요원 중 FBI 요원을 찾는 프로그램을 작성하시오.

# FBI요원은 요원의 첩보원명에 FBI가 들어있다. 

li = []
for i in range(1, 6):
    name = input()
    if "FBI" in name:
        li.append(i)

if li:
    print(*li)
else:
    print("HE GOT AWAY!")