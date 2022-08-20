# 경북대 특산품 호반우는 품질에 따라 등급이 숫자로 매겨진다. 호반우 상인들은 N개의 호반우를 파려고 한다. 호반우는 개별적으로 팔 수도 있지만 묶음으로 팔 수도 있다. 이 때 묶음이라 함은 호반우들의 어떤 부분집합을 말한다.

# 하나의 호반우를 팔 때 기존의 계산법으로는 품질만큼의 가격으로 팔리게 된다.

# 따라서 묶어파나 개별적으로 파나 상인이 벌 수 있는 총 금액은 차이가 없었다.

# 하지만 호반우 상인들은 욕심쟁이여서 돈을 더 많이 받을 방법을 놓고 회의를 열게 된다. 그러던 와중 호반우 상인들은 새로운 품질 계산법을 개발해냈다!

# 호반우를 묶음으로 팔 때는 모든 호반우의 품질을 묶음의 '중앙값'으로 결정하게 된다. 이 때 묶음이 짝수인 경우 묶음 안에 있는 호반우를 품질을 기준으로 정렬했을 때 (묶음 개수/2+1)번째 호반우를 중앙값으로 정의하고 홀수인 경우 ((묶음 개수+1)/2)번째 호반우를 중간값으로 정의한다.

# 계산법을 새로 만드는 데는 성공했지만 호반우가 너무 많아 어떻게 묶어야 할 지 혼란이 오기 시작한 호반우 상인들은 장사에서 최대의 이익을 얻지 못 하고 있었다. 호반우 상인들을 위해 호반우들을 팔아서 얻을 수 있는 최대 이익을 계산하는 프로그램을 만들어주자!

N = int(input())
quality = sorted(list(map(int, input().split())))

lst = []
start = 0
end = len(quality)-1
while start < end:
    lst.append((quality.pop(0), quality.pop()))
    start += 1
    end -= 1

total = 0
for i in lst:
    if len(i) % 2 == 0:  # 묶음 개수가 짝수개인 경우
        mid = (len(i)//2)+1
        total += i[mid-1] * 2
    else:
        mid = (len(i)+1)//2
        total += i[mid-1] * 2

if len(quality) % 2 != 0:   # 만약 홀수개(1개)가 남는다면?
    total += sum(quality)
    print(total)
else:   # 만약 짝수개(0개)가 남는다면?
    print(total)

# 문제에 주어진 노트를 보고 오히려 헷갈려서 헤맸던 문제였다...
# 다시 주어진 노트를 보니 계속 헛짓거리를 했던 시간이 많이 아깝게 느껴졌다.
# 이 문제의 핵심은 정렬과 그리디 알고리즘이었다.

# 최대 수익이 나오게끔 하는 방법은 (가장 싼 호반우, 가장 비싼 호반우)를 묶어 (가장 비싼 호반우) * 2를 반복하면 된다.
# 이 때 호반우의 개수가 홀수라면, 무조건 하나가 남을 수 밖에 없다. 따라서 위의 과정을 반복한 다음 나머지 값을 그대로 더해주기만 하면 된다.
# 호반우의 개수가 짝수라면, 쌍을 이뤄서 그대로 반복해주면 된다.