# 회의가 끝났고, 이제 악수를 하는 시간이다. 모든 사람은 직사각형 탁자 하나의 한 면에 앉아있다.
#
# 자리를 벗어나지 않고 악수를 하는 방법의 수는 총 몇 가지일까?
#
# 각 사람들은 자신의 왼쪽이나 오른쪽에 있는 사람들과 악수를 할 수 있다. (안 할 수도 있다)

# code1
n = int(input())

a, b = 1, 0
for i in range(n):
    a, b = a+b, a
a = str(a)
print(a[-1])

# code2
n = int(input())

a, b = 1, 0
for i in range(n):
    a, b = (a+b) % 10, a % 10
print(a)

# 이 문제는 17175번 문제와 스타일이 유사한 문제이다.
# 마지막 숫자를 구하기 위해서 해당 숫자를 문자로 바꾼 다음 [-1]을 이용해서 마지막 숫자를 출력하려고 했으나 시간초과가 나왔다.
# 마지막 숫자를 구하기 위한 가장 좋은 방법 => 10으로 나눠 계속 진행하면 결국 일의 자리 숫자가 남게 된다.
