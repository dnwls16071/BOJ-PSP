# 동혁이는 나무 조각을 5개 가지고 있다. 나무 조각에는 1부터 5까지 숫자 중 하나가 쓰여져 있다. 또, 모든 숫자는 다섯 조각 중 하나에만 쓰여 있다.

# 동혁이는 나무 조각을 다음과 같은 과정을 거쳐서 1, 2, 3, 4, 5 순서로 만들려고 한다.

# 첫 번째 조각의 수가 두 번째 수보다 크다면, 둘의 위치를 서로 바꾼다.
# 두 번째 조각의 수가 세 번째 수보다 크다면, 둘의 위치를 서로 바꾼다.
# 세 번째 조각의 수가 네 번째 수보다 크다면, 둘의 위치를 서로 바꾼다.
# 네 번째 조각의 수가 다섯 번째 수보다 크다면, 둘의 위치를 서로 바꾼다.
# 만약 순서가 1, 2, 3, 4, 5 순서가 아니라면 1 단계로 다시 간다.
# 처음 조각의 순서가 주어졌을 때, 위치를 바꿀 때 마다 조각의 순서를 출력하는 프로그램을 작성하시오.

# map함수의 사용 방법을 알아낸 아주 좋은 문제였다.
# 문자열 배열의 경우 사용하는 방법 : print(''.join(arr))
# 문자열 배열뿐만 아니라 숫자 배열을 map함수로 나타내는 방법 : print(''.join(map(str, arr)))

# 1차 작성한 코드
arr = list(map(int, input().split()))
answer = [1, 2, 3, 4, 5]


while True:
    for i in range(0, len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            print(' '.join(map(str, arr)))
    
    if arr == answer:
        break

# 2차 작성한 코드
arr = list(map(int, input().split()))

while True:
    if arr == [1, 2, 3, 4, 5]:
        break

    for i in range(0, len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            print(' '.join(map(str, arr)))