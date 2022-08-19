# 준하는 유치원에서 단어 퍼즐게임을 즐겨한다.

# 단어 퍼즐게임이란, 주어진 알파벳들을 섞어서 단어를 만드는 게임이다.

# 천재 준하는 알파벳을 임의로 조합하여, 사전과 매칭된 단어를 만드는 프로그램을 만들어 단어를 완성시켰다.

# 그러나 완성된 단어를 원장님에게 가져가려는 순간, 지나가던 강민이와 부딫혀서 단어조각을 땅에 떨어뜨리고 말았다.

# 준하는 어찌어찌 조각을 회수했지만, 순서는 뒤죽박죽이 되었고, 알파벳이 부족하거나 다른 알파벳이 섞였을 수도 있다.

# 준하가 처음에 완성한 단어와 나중에 회수한 알파벳들이 주어질 때,

# 준하가 알파벳을 제대로 회수했는지 안했는지 판단하는 프로그램을 만들어주자.

# 1차 작성한 코드(거의 참고한 코드임)
# cnt = 1
# while True:
#     a = input()
#     b = input()
#     if a == "END" and b == "END":
#         break
    
#     # 알파벳 수에 해당하는만큼의 배열을 생성하고 해당 문자를 숫자로 변환하면 그 숫자에 해당하는 위치값을 1로 변화
#     tmpa, tmpb = [0]*26, [0]*26
#     for i in a:
#         tmpa[ord(i)-97] += 1
#     for i in b:
#         tmpa[ord(i)-97] += 1

#     if tmpa == tmpb:
#         print("Case %d: same" %cnt)
#     else:
#         print("Case %d: different" %cnt)
#     cnt += 1

# 2차 작성한 코드
cnt = 1
while True:
    a = str(input())
    b = str(input())
    if a == "END" and b == "END":
        break

    a_score = 0
    for i in a:
        a_score += ord(i)
    
    b_score = 0
    for i in b:
        b_score += ord(i)
    
    if a_score == b_score:
        print("Case %d: same" %cnt)
    else:
        print("Case %d: different" %cnt)
    cnt += 1
    