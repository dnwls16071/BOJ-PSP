# 입학 OT때 누구보다도 남다르게 놀았던 당신은 자연스럽게 1학년 과대를 역임하게 되었다.
# 타교와의 조인트 엠티를 기획하려는 당신은 근처에 있는 학교 중 어느 학교가 술을 가장 많이 먹는지 궁금해졌다.
# 학교별로 한 해동안 술 소비량이 주어질 때, 가장 술 소비가 많은 학교 이름을 출력하여라.

#1번 코드
T = int(input())    # 테스트 케이스의 숫자 T가 주어진다.


for i in range(T):
    N = int(input())
    
    max = 0
    mname = ""  # 최댓값을 가지는 학교를 초기화할때 문자열이므로 큰따옴표로 초기화
    for i in range(N):
        S, L = input().split()
        L = int(L)
        if L > max:
            max = L # 최댓값 변수에 L저장
            mname = S # 최댓값 학교에 S저장
    print(mname)

#2번 참고 코드
#2번 코드 아이디어 : 각각의 리스트를 만들고 그대로 리스트에 저장한다.
#2번 코드 아이디어 : 그대로 저장하면 변하지않으므로 술 소비량의 최댓값이 위치한 인덱스를 변수에 저장한다.
#2번 코드 아이디어 : 변수를 학교 리스트의 인덱스 위치값을 구하는데 사용하면 원하는 값을 구할 수 있다.
T = int(input())

for i in range(T):
    N = int(input())

    s_list = []
    l_list = []
    for i in range(N):
        S, L = input().split()
        L = int(L)
        s_list.append(S)
        l_list.append(L)
        a = l_list.index(max(l_list))
    print(s_list[a])