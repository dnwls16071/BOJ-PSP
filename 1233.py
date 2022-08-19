# 지민이는 주사위 던지기 게임을 좋아하여 어느 날 옆에 있는 동호를 설득하여 주사위 던지기 게임을 하자고 하였다. 총 3개의 주사위가 있다. 그리고 이 주사위는 각각 S1(2 ≤ S1 ≤ 20), S2(2 ≤ S2 ≤ 20), S3(2 ≤ S3 ≤ 40)개의 면이 있다. (실제로는 주사위가 6개의 면이 있는 것이 정상이지만 특별한 주사위라 생각하자.)

# 문제는 세 개의 주사위를 동시에 던졌을 때 가장 높은 빈도로 나오는 세 주사위의 합을 구하는 것이다.

# 예를 들어, S1 = 3, S2 = 2, S3 = 3으로 주어질 때, 주사위1은 S1(3)개의 면이 있으므로 1, 2, 3의 눈을 가지고, 주사위2는 S2(2)개의 면이 있으므로 1, 2의 눈을 가지며, 주사위3은 S3(3)개의 면이 있으므로 1, 2, 3의 눈을 가진다. 이 때, 이 3개의 주사위를 던져서 눈의 합을 구하면, (1, 1, 1) = 3, (1, 1, 2) = 4, (1, 1, 3) = 5, ... , (3, 2, 1) = 6, (3, 2, 2) = 7, (3, 2, 3) = 8과 같은 합들을 얻을 수 있다. 이 때, 가장 많이 발생하는 합을 구하는 것이다.

# 1차 작성한 코드
S1, S2, S3 = map(int, input().split())

S1_lst = []
for i in range(1, S1+1):
    S1_lst.append(i)
S2_lst = []
for i in range(1, S2+1):
    S2_lst.append(i)
S3_lst = []
for i in range(1, S3+1):
    S3_lst.append(i)

result = []
for a in S1_lst:
    for b in S2_lst:
        for c in S3_lst:
            result.append(a+b+c)

ans = []
for i in result:
    ans.append(result.count(i))
ans = set(ans)

print(max(ans))

# 2차 작성한 코드
S1, S2, S3 = map(int, input().split())
tmp = [0] * 81  #왜 81만큼의 배열을 생성했느냐 > 최댓값이 20+20+40=80이므로
for i in range(1, S1+1):
    for j in range(1, S2+1):
        for k in range(1, S3+1):
            tmp[i+j+k] += 1

for i in range(1, 81):
    if tmp[i] == max(tmp):  # 만약  tmp[i]가 tmp 값 중에서 가장 최댓값이라면?
        print(i)    # 그 i 값이 인덱스 값이므로 출력한다.
        break