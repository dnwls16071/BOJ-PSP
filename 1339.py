# 민식이는 수학학원에서 단어 수학 문제를 푸는 숙제를 받았다.
#
# 단어 수학 문제는 N개의 단어로 이루어져 있으며, 각 단어는 알파벳 대문자로만 이루어져 있다. 이때, 각 알파벳 대문자를 0부터 9까지의 숫자 중 하나로 바꿔서 N개의 수를 합하는 문제이다. 같은 알파벳은 같은 숫자로 바꿔야 하며, 두 개 이상의 알파벳이 같은 숫자로 바뀌어지면 안 된다.
#
# 예를 들어, GCF + ACDEB를 계산한다고 할 때, A = 9, B = 4, C = 8, D = 6, E = 5, F = 3, G = 7로 결정한다면, 두 수의 합은 99437이 되어서 최대가 될 것이다.
#
# N개의 단어가 주어졌을 때, 그 수의 합을 최대로 만드는 프로그램을 작성하시오.

N = int(input())
alpha = []
alpha_dict = {}
new_alpha_lst = []
for i in range(N):
    alpha.append(input())

for i in range(N):
    for j in range(len(alpha[i])):
        if alpha[i][j] in alpha_dict:
            alpha_dict[alpha[i][j]] += 10 ** (len(alpha[i]) - j - 1)
        if alpha[i][j] not in alpha_dict:
            alpha_dict[alpha[i][j]] = 10 ** (len(alpha[i]) - j - 1)

for val in alpha_dict.values():
    new_alpha_lst.append(val)
new_alpha_lst.sort(reverse=True)

tot = 0
k = 9
for i in new_alpha_lst:
    tot += (i * k)
    k -= 1
print(tot)

# 어떤 방식으로 문제를 해결해나가야할지 고민을 많이 했던 문제였다.
# 방법을 찾아보니 각 알파벳의 자릿수만큼 곱해서 그 수를 딕셔너리에 저장한다.
# 그 다음 딕셔너리의 value값들을 리스트에 저장해서 내림차순 정렬한 후에 처음 값부터 9를 곱해서 하나씩 감소시켜 나가는 방법을 사용했다.
