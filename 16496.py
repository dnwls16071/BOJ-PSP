# N과 L이 주어질 때, 합이 N이면서, 길이가 적어도 L인 가장 짧은 연속된 음이 아닌 정수 리스트를 구하는 프로그램을 작성하시오.

N = int(input())
lst = list(map(str, input().split()))

new_lst = []
for i in lst:
    s = str(i)
    new_s = s
    while len(new_s) < 10:
        new_s += s
    new_lst.append((new_s, s))

new_lst.sort(key = lambda x : x[0], reverse = True)
ans = ""
for j in new_lst:
    ans += j[-1]

if int(ans) == 0:
    print(0)
else:
    print(ans)


# 이 문제의 아이디어가 정말 참신했다.. 문제 푸는 스킬(PS) 경험치가 매우 높아야 나오는 방법이었다.
# 처음엔 0을 연달아서 붙여 비교를 하려고 했는데 매번 틀렸다는 결과가 나와서 머리를 쥐어 뜯었다.
# 구글링을 활용한 두 번째 방법은 숫자를 문자형으로 바꿔 계속 반복해주는 것이다.
# 리스트의 값은 1000000000보다 작거나 같은 음이 아닌 정수이므로 최대 10자리가 된다.
# 리스트를 정렬할때는 최대 10자리까지 늘린 수를 기준으로 내림차순 정렬을 한 후에 원래 값들로 수를 만들어 답을 도출하면 된다.
