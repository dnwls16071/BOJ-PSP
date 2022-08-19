# 다음과 같은 규칙에 따라 수들을 만들려고 한다.
#
# 첫 번째 수로 양의 정수가 주어진다.
# 두 번째 수는 양의 정수 중에서 하나를 선택한다.
# 세 번째부터 이후에 나오는 모든 수는 앞의 앞의 수에서 앞의 수를 빼서 만든다. 예를 들어, 세 번째 수는 첫 번째 수에서 두 번째 수를 뺀 것이고, 네 번째 수는 두 번째 수에서 세 번째 수를 뺀 것이다.
# 음의 정수가 만들어지면, 이 음의 정수를 버리고 더 이상 수를 만들지 않는다.
# 첫 번째 수로 100이 주어질 때, 두 번째 수로 60을 선택하여 위의 규칙으로 수들을 만들면 7개의 수들 100, 60, 40, 20, 20 , 0, 20이 만들어진다. 그리고 두 번째 수로 62를 선택하여 위의 규칙으로 수들을 만들면 8개의 수들 100, 62, 38, 24, 14, 10, 4, 6이 만들어진다. 위의 예에서 알 수 있듯이, 첫 번째 수가 같더라도 두 번째 수에 따라서 만들어지는 수들의 개수가 다를 수 있다.
#
# 입력으로 첫 번째 수가 주어질 때, 이 수에서 시작하여 위의 규칙으로 만들어지는 최대 개수의 수들을 구하는 프로그램을 작성하시오. 최대 개수의 수들이 여러 개일 때, 그중 하나의 수들만 출력하면 된다.

first_number = int(input())
result = []

max_cnt = 0
for i in range(first_number+1):
    lst = [first_number, i]
    j = 0
    while True:
        last_number = lst[j] - lst[j+1] # j번째 항과 j+1번째 항의 차이
        j += 1
        if last_number < 0: # 만약 마지막 수가 음수라면
            break   # 더 이상 만들지않고 그대로 스탑
        lst.append(last_number) # 마지막 숫자를 리스트에 저장
        if max_cnt < len(lst):  # 만약 최대 개수보다 크다면?
            max_cnt = len(lst)  # 최대 개수 값을 갱신
            result = lst # 리스트도 갱신

print(max_cnt)
for i in range(len(result)):
    print(result[i], end = " ")

# 브루트포스의 정석대로 0부터 하나하나 증가시켜 조건을 판단하여 리스트에 저장하였다.

# 리스트 슬라이싱
# lst[:3] => 리스트 맨 앞부터 3번째 원소값까지
# lst[3:] => 리스트 4번째 원소값부터 끝까지
# lst[:] => 리스트의 모든 원소값
