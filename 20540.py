# 졸업을 앞둔 연길이는 크리스마스가 다가올수록 외로움을 느낀다.

# 그런 연길이를 위해 동우는 소개팅을 시켜주지는 않고 연길이의 이상향을 찾는 것을 도와주고자 한다.

# MBTI 신봉자인 연길이는 자신과 정반대인 사람에게 매력을 느낀다. 즉, MBTI의 네가지 지표가 모두 자신과 반대인 사람이 연길이의 이상형이다.

# MBTI는 다음과 같은 네 가지 척도로 성격을 표시한다. 각각의 척도는 두 가지 극이 되는 성격으로 이루어져 있다.

# 지표	설명
# 외향(Extroversion)	내향(Introversion)	선호하는 세계:세상과 타인 / 내면 세계
# 감각(Sensation)	직관(iNtuition)	인식형태: 실제적인 인식/ 실제 너머로 인식
# 사고(Thinking)	감정(Feeling)	판단기준: 사실과 진실 위주 / 관계와 사람 위주
# 판단(Judging)	인식(Perceiving)	생활양식: 계획적인 생활 / 즉흥적인 생활
# 네 가지 척도마다 두 가지 경우가 존재하므로, 총 16가지의 유형이 만들어진다. 유형은 각 경우를 나타내는 알파벳 한 글자씩을 따서 네 글자로 표시한다. 다음은 MBTI의 유형들이다.

# 구분	감각/사고	감각/감정	직관/감정	직관/사고
# 내향/판단	ISTJ	ISFJ	INFJ	INTJ
# 내향/인식	ISTP	ISFP	INFP	INTP
# 외향/인식	ESTP	ESFP	ENFP	ENTP
# 외향/판단	ESTJ	ESFJ	ENFJ	ENTJ
# 연길이가 자신의 이상향을 무사히 찾을 수 있도록 도와주자!

MBTI = list(input())

for i in MBTI:
    if i == "E":
        print("I", end = "")
    elif i == "S":
        print("N", end = "")
    elif i == "T":
        print("F", end = "")
    elif i == "J":
        print("P", end = "")
    elif i == "I":
        print("E", end = "")
    elif i == "N":
        print("S", end = "")
    elif i == "F":
        print("T", end = "")
    elif i == "P":
        print("J", end = "")
    