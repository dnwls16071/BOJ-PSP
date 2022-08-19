# 앨버타의 자동차 번호판은 ABC-0123 (세 글자, 네 숫자)와 같이 두 부분으로 나누어져 있다.

# 좋은 번호판은 첫 번째 부분의 가치와 두 번째 부분의 가치의 차이가 100을 넘지 않는 번호판이다.

# 글자로 이루어진 첫 번째 부분의 가치는 글자를 26진법 수처럼 계산한다. (각 자리가 [A..Z]) 예를 들어, "ABC"의 가치는 28 (0×262 + 1×261 + 2×260)이 된다. "ABC-0123"은  |28 - 123| ≤ 100 이기 때문에, 좋은 번호판이다.

# 자동차 번호판이 주어졌을 때, 좋은 번호판인지 아닌지를 구하는 프로그램을 작성하시오.

N = int(input())
for _ in range(N):
    string, num = input().split("-")
    num = int(num)

    string_num = 0
    for i in range(3):
        string_num += (ord(string[i])-65) * 26**(2-i)
    
    if abs(string_num - num) <= 100:
        print("nice")
    else:
        print("not nice")