# 경근이는 수업 과제의 일환으로 연세대학교의 역사를 조사하고 있었다. 케케묵은 도서관 구석에서 경근이가 발견한 것은 역대 연고전의 야구경기 실황 기록문서였다.
# 하지만 문서를 가지고 있음에도 불구하고 한 눈에 당시의 경기 승패를 파악하기에는 어려움이 많았는데, 문서에는 회차별 양 팀 획득 점수만이 적혀져 있기 때문이었다.

# 경근이는 주어진 방대한 자료를 해석하는것이 귀찮았기 때문에 절친한 프로그래머 친구인 당신에게 도움을 요청했다.

# 주어진 실황 기록문서에서 어떤 팀이 이겼는지를 알아내 경근이를 도와주자!

T = int(input())    #테스트 케이스의 숫자 입력
for _ in range(T):  
    yonsei_score = 0
    korea_score = 0
    for _ in range(9):  #9줄에 나눠 출력
        Y, K = map(int, input().split())    #매회 득점한 점수들을 공백을 두고 입력
        yonsei_score += Y  
        korea_score += K
    if yonsei_score > korea_score:
        print("Yonsei")
    elif yonsei_score < korea_score:
        print("korea")
    else:
        print("Draw")