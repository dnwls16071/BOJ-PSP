# 2와 e는 발음이 비슷해, 둘을 섞어서 말하면 듣는 사람을 짜증나게 만들 수 있다.

# 지민이는 이 점을 이용해 은수를 미치게 하고 있다. 은수를 위해 지민이가 말한 문자열 s가 주어질때, 2의 등장 횟수가 더 많은지, e의 등장 횟수가 더 많은지 도와주자

len_s = int(input())
s = input()

count1 = s.count("2")
count2 = s.count("e")

if count1 > count2:
    print("2")
elif count1 < count2:
    print("e")
elif count1 == count2:
    print("yee")