# 어느 날, 타노스는 0과 1로 이루어진 문자열 $S$를 보았다. 신기하게도, $S$가 포함하는 0의 개수와 $S$가 포함하는 1의 개수는 모두 짝수라고 한다.
#
# 갑자기 심술이 난 타노스는 $S$를 구성하는 문자 중 절반의 0과 절반의 1을 제거하여 새로운 문자열 $S'$를 만들고자 한다. $S'$로 가능한 문자열 중 사전순으로 가장 빠른 것을 구하시오.

S = list(input())

zero = S.count("0") // 2
one = S.count("1") // 2

for i in range(zero):
    S.pop(-(S[::-1].index("0"))-1)

for i in range(one):
    S.pop(S.index("1"))
print(''.join(S))

# 사전순으로 출력하려면 오름차순으로 나와야한다.
# 따라서 0이 먼저 나와야하므로 0을 뒤에서부터 제거하고 1은 앞에서부터 제거해야한다.