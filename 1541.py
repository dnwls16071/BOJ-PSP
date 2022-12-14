# 세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.

# 그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

# 괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

# 문제 해결을 위한 계획 : '-' 부호 뒤에 붙는 수가 최대가 되게끔 괄호를 표시한다.

# 입력 문장을 '-' 부호를 기준으로 분할하여 리스트에 저장한다.
# 입력 문장의 첫 번째 값 다음에 '-' 부호가 안 나올수도 있으므로 '+' 부호 기준으로 분할하여 리스트에 저장한다.

expression = input().split("-")
result = 0
# 입력 문장의 첫 번째 값을 정수화시켜 합계에 더해놓는다.
for i in expression[0].split("+"):
    result += int(i)

# 입력 문장의 첫 번째 요소부터 하나하나를 반복문으로 받아온다.
for i in expression[1:]:
    # 하나하나 받아온 요소들은 전부 '+' 부호를 가지고 있으므로 그것 역시 분할하여 받아온다. 
    for j in i.split("+"):
        # 받아온 인수들을 전부 정수화시켜 빼준다.
        result -= int(j)
print(result)