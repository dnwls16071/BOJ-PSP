# 한 줄로 된 간단한 에디터를 구현하려고 한다. 이 편집기는 영어 소문자만을 기록할 수 있는 편집기로, 최대 600,000글자까지 입력할 수 있다.

# 이 편집기에는 '커서'라는 것이 있는데, 커서는 문장의 맨 앞(첫 번째 문자의 왼쪽), 문장의 맨 뒤(마지막 문자의 오른쪽), 또는 문장 중간 임의의 곳(모든 연속된 두 문자 사이)에 위치할 수 있다. 즉 길이가 L인 문자열이 현재 편집기에 입력되어 있으면, 커서가 위치할 수 있는 곳은 L+1가지 경우가 있다.

# 이 편집기가 지원하는 명령어는 다음과 같다.

# L	커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
# D	커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
# B	커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
# 삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
# P $	$라는 문자를 커서 왼쪽에 추가함

# 1차(시간초과)
# string_list = list(input())
# cursor = len(string_list)

# for _ in range(int(input())):
#     command = list(input().split())
#     if command[0] == "P":
#         string_list.insert(cursor, command[1])
#         cursor += 1
#     elif command[0] == "L":
#         if cursor > 0:
#            cursor -= 1
#     elif command[0] == "D":
#         if cursor < len(string_list):
#             cursor += 1
#     elif command[0] == "B":
#         if cursor > 0:
#             string_list.remove(string_list[cursor])

# print(''.join(string_list))

import sys

st1 = list(sys.stdin.readline().strip())    # 입력한 문자열
st2 = []    
n = int(sys.stdin.readline())   # 반복 횟수
for _ in range(n):
    command = sys.stdin.readline().strip()  # 공백을 포함해서 그냥 입력
    if command[0] == "P":
        st1.append(command[2])  # 공백이 command[1]이므로 command[2] 값이 문자에 해당
    elif command[0] == "L" and st1 != []:
        st2.append(st1.pop())
    elif command[0] == "D" and st2 != []:
        st1.append(st2.pop())
    elif command[0] == "B" and st1 != []:
        st1.pop()
        
print(''.join(st1+list(reversed(st2))))
        