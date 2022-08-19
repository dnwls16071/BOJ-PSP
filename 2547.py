# 사탕 박사 고창영은 사탕 공장을 그만 두고 초등학교 선생님으로 취직했다.

# 오늘은 창영이네 반 학생들과 소풍을 가는 날이다. N명의 학생은 모두 가방에 사탕을 가득 담아왔다.

# 그런데, 사탕을 많이 가져온 학생들이 사탕을 적게 가져온 학생들을 놀리기 시작했다.

# 창영이는 "얘들아~ 그러면 안되지ㅜㅜ 사탕을 모두 여기에 가져와보렴. 선생님이 공평하게 나눠줄게"

# 창영이는 모든 학생들이 같은 사탕을 가지게 하려고 한다.

# 이것이 가능한 일일까?

# 1차 작성한 코드
T = int(input())

for _ in range(T):
    temp = input()
    N = int(input())
    lst = []
    for i in range(N):
        lst.append(int(input()))
        
    if sum(lst) % N == 0:
        print("YES")
    else: 
        print("NO")
        
# 2차 작성한 코드(질문)
# 이 코드가 정답이 안되는 이유
T = int(input())

for _ in range(T):
    print()
    N = int(input())
    lst = []
    for i in range(N):
        lst.append(int(input()))
        
    if sum(lst) % N == 0:
        print("YES")
    else: 
        print("NO")