# 두 단어 A와 B가 주어졌을 때, A에 속하는 알파벳의 순서를 바꾸어서 B를 만들 수 있다면, A와 B를 애너그램이라고 한다.

# 두 단어가 애너그램인지 아닌지 구하는 프로그램을 작성하시오.

T = int(input())

for i in range(T):
    A, B = map(str, input().split())

    lst_A = sorted(list(A))
    lst_B = sorted(list(B))

    if lst_A == lst_B:
        print(A + " & " + B + " are anagrams.")
    else:
        print(A + " & " + B + " are NOT anagrams.")
        