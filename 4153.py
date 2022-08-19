# 과거 이집트인들은 각 변들의 길이가 3, 4, 5인 삼각형이 직각 삼각형인것을 알아냈다. 주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.

# 1차 작성 코드
T = int(input())

for i in range(T):
    x, y, z = map(int, input().split())
    if x == 0 and y == 0 and z == 0:
        print("wrong")
    else:
        if (x**2 + y**2) == z**2:
            print("right")
        else:
            print("wrong")

# 2차 작성 코드
while True:
    nums = list(map(int, input().split()))
    if sum(nums) == 0:
        break
    max_num = max(nums) # nums 리스트중에서 가장 긴 값(빗변)을 max_num에 저장
    nums.remove(max_num) # nums값에서 최대값인 max_num을 뺀다 
    if nums[0]**2 + nums[1]**2 == max_num**2:   
        print("right")
    else:
        print("wrong")