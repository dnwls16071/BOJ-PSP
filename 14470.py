# JOI 군은 식사 준비를 위해 A℃의 고기를 전자레인지로 B℃까지 데우려고 한다. 고기는 온도가 0℃보다 낮을 때 얼어 있고, 0℃보다 높을 때는 얼어 있지 않다. 온도가 정확히 0℃일 때 고기는 얼어 있을 수도, 얼어 있지 않을 수도 있다.

# JOI 군은 가열할 때 고기가 아래의 규칙을 따라 데워진다고 가정하고, 고기를 데우는 데 걸리는 시간을 어림하기로 했다.

# 고기가 얼어 있고 온도가 0℃ 미만일 때 : 온도가 C초에 1℃씩 오른다.
# 고기가 얼어 있고 온도가 정확히 0℃일 때 : 얼어 있지 않은 상태로 만드는(해동하는) 데 D초가 걸린다.
# 고기가 얼어 있지 않을 때 : 온도가 E초에 1℃씩 오른다.
# 이 규칙을 토대로, 고기가 B℃까지 데워지는 데 몇 초가 걸리는지 구하라.

# 1차 작성한 코드
A = int(input())    # 원래의 고기의 온도
B = int(input())    # 목표 온도
C = int(input())    # 얼어 있는 고기를 1도 데우는데 걸리는 시간
D = int(input())    # 얼어 있는 고기를 해동하는데 걸리는 시간
E = int(input())    # 얼어 있지 않은 고기를 1도 데우는데 걸리는 시간

if A < 0:
    time = -A*C+D+B*E
else:
    time = (B - A) * E
print(time)

# 2차 작성한 코드
A = int(input())    # 원래의 고기의 온도
B = int(input())    # 목표 온도
C = int(input())    # 얼어 있는 고기를 1도 데우는데 걸리는 시간
D = int(input())    # 얼어 있는 고기를 해동하는데 걸리는 시간
E = int(input())    # 얼어 있지 않은 고기를 1도 데우는데 걸리는 시간

time = 0
if A < 0:
    time += abs(A*C)
    time += D
    time += B * E
else:
    time += (B - A) * E

print(time)