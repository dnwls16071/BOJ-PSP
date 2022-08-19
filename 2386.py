# 꿍은 도비의 자유를 위해 영어를 가르치기로 결심했다. 하지만 도비는 바보라 ABC부터 배워야 한다.
#
# 그래서 꿍은 영어 문장과 알파벳 하나가 주어지면 그 알파벳이 문장에서 몇 번 나타나는지를 세는 문제들을 내주었다. 하지만 도비는 마법사고 컴공도 마법사다.
#
# 여러분은 도비를 위해 문제의 답을 알려주는 프로그램을 만들수 있을것이다!

while True:
    lst = input()
    if lst == "#":
        break
    alphabet = lst[0]
    sentence = lst[2:].lower()
    cnt = 0
    for i in sentence:
        if i == alphabet:
            cnt += 1
    print(alphabet, cnt)

# 입력값을 읽어오는 방법에는 여러가지 감각이 필요하다.
# 이 문제처럼 알파벳을 제외한 오른쪽 값들을 하나의 문장으로 인식하려면 리스트 슬라이싱 기능을 이용하면 된다.
# 하지만 이 문제가 아니라 공백을 기준으로 입력값을 받아온다면 lst[0], lst[1] 이런 식으로 받아오면 된다.