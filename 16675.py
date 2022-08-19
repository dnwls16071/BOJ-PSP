# 민성이와 태경이는 고려대학교에서 알아주는 가위바위보의 최고수들이다. 이들은 기존의 가위바위보에 질린 나머지, 2개의 손을 모두 이용하여 가위바위보를 즐기는 경지에 이르렀다.

# 먼저, 둘이 동시에 “가위, 바위, 보”를 외치며 두 개의 손을 각각 가위, 바위, 보 중 하나로 설정하여 공개한다. 그 자리에서 서로 3초간 호흡을 가다듬은 후, 동시에 왼손을 낼지 오른손을 낼지를 결정한다. 민성이와 태경이는 최고수들끼리의 대결이라는 압박감에 의해 가끔 판단력이 흐려질 때가 있어서, 실수로 왼손과 오른손에 같은 동작을 취할 수도 있다.

# 당신은 민성이와 태경이의 왼손과 오른손의 상태가 주어졌을 때, 민성이 또는 태경이가 적절히 왼손 또는 오른손을 선택하여 가위바위보에서 무조건 이기는 방법이 있는지 없는지를 알려고 한다.

# # 잘못 작성한 코드
# case = list(map(str, input().split()))
# # S, R, P 중 하나이며 각각 가위, 바위, 보를 의미한다.

# Minsung = []
# Taekyung = []
# for i in range(len(case) // 2):
#     Minsung.append(case[i])

# for j in range(len(case)//2, len(case)):
#     Taekyung.append(case[j])

# Minsung_score = 0
# Taekyung_score = 0
# draw = 0 # 승부가 나지 않았을 경우
# for a in Minsung:
#     for b in Taekyung:
#         if (a == "R" and b == "S"):
#             Minsung_score += 1
#         elif(a == "S" and b == "R"):
#             Taekyung_score += 1
#         elif (a == "S" and b == "P"):
#             Minsung_score += 1 
#         elif (a == "P" and b == "S"):
#             Taekyung_score += 1
#         elif (a == "P" and b == "R"):
#             Minsung_score += 1
#         elif (a == "R" and b == "P"):
#             Taekyung_score += 1
#         elif (a == "R" and b == "R") or (a == "S" and b == "S") or (a == "P" and b == "P"):
#             draw += 1

# # 민성이가 태경이한테 완벽하게 이긴다는 전제하에서
# if Minsung_score == 4 and Taekyung_score == 0:
#     print("MS")
# # 태경이가 민성이한테 완벽하게 이긴다는 전제하에서
# elif Minsung_score == 0 and Taekyung_score == 4:
#     print("TK")
# # 둘이 무조건 비겨서 draw변수값이 0보다 큰 경우
# elif draw > 0:
#     print("?")

# 다시 재작성한 코드
ML, MR, TL, TR = input().split()

# 각 사람이 낸 두 수가 다를 경우
if ML != MR and TL != TR:
    print("?")
    
# 민성이가 같은 수를 낸 경우
elif ML == MR and TL != TR:
    if ML == 'S' and (TL == 'R' or TR == 'R'):
        print("TK")
    elif ML == 'P' and (TL == 'S' or TR == 'S'):
        print("TK")
    elif ML == 'R' and (TL == 'P' or TR == 'P'):
        print("TK")
    else:
        print("?")

# 태경이가 같은 수를 낸 경우
elif ML != MR and TL == TR:
    if TL == 'S' and (ML == 'R' or MR == 'R'):
        print("MS")
    elif TL == 'P' and (ML == 'S' or MR == 'S'):
        print("MS")
    elif TL == 'R' and (ML == 'P' or MR == 'P'):
        print("MS")
    else:
        print("?")

# 각 사람이 낸 두 수가 같은 경우
else:
    if ML == 'S':
        if TL == 'P':
            print("MS")
        if TL == 'S':
            print("?")
        if TL == 'R':
            print("TK")
    if ML == 'R':
        if TL == 'P':
            print("TK")
        if TL == 'S':
            print("MS")
        if TL == 'R':
            print("?")
    if ML == 'P':
        if TL == 'P':
            print("?")
        if TL == 'S':
            print("TK")
        if TL == 'R':
            print("MS")