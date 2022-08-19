# 친구로부터 노트북을 중고로 산 스브러스는 노트북을 켜자마자 경악할 수밖에 없었다. 바탕화면에 온갖 파일들이 정리도 안 된 채 가득했기 때문이다. 그리고 화면의 구석에서 친구의 메시지를 확인할 수 있었다.

# 바탕화면의 파일들에는 값진 보물에 대한 정보가 들어 있어. 하나라도 지우게 된다면 보물은 물론이고 다시는 노트북을 쓸 수 없게 될 거야. 파일들을 잘 분석해서 보물의 주인공이 될 수 있길 바랄게. 힌트는 “확장자”야.

# 화가 났던 스브러스는 보물 이야기에 금세 화가 풀렸고 보물의 정보를 알아내려고 애썼다. 하지만 파일이 너무 많은 탓에 이내 포기했고 보물의 절반을 보상으로 파일의 정리를 요청해왔다. 스브러스의 요청은 다음과 같다.

# 파일을 확장자 별로 정리해서 몇 개씩 있는지 알려줘
# 보기 편하게 확장자들을 사전 순으로 정렬해 줘
# 그럼 보물의 절반을 얻어내기 위해 얼른 스브러스의 노트북 파일 정리를 해줄 프로그램을 만들자!

N = int(input())
file = {}
for _ in range(N):
    file_name, extender_name = input().split(".")
    if extender_name not in file:
        file[extender_name] = 1
    else:
        file[extender_name] += 1
new_file = sorted(file.items())

for key, value in new_file:
    print(key, value)

# 처음엔 이 문제의 본질을 이해하지 못해서 WA를 받았다.
# 결론을 먼저 말하자면 이 문제는 딕셔너리를 제대로 이용할 수 있느냐 없느냐 문제이다.

# 리스트는 sort(), sort(reverse=True)를 통해서 간단하게 정렬할 수 있지만 딕셔너리는 다르다.
# 딕셔너리의 정렬법을 공부해서 정리해보았다.

# 딕셔너리의 Key를 기준으로 오름차순 정렬하는 방법
# dict = {'A' :1,'D' :4,'C' :3,'B' :2}
# sdict= sorted(dict.items())

# 딕셔너리의 value를 기준으로 오름차순 정렬하는 방법
# dicts = {'A' :4,'D' :1,'C' :2,'B' :3}
# sdicts= sorted(dicts.items(), key=lambda x: x[1])

# 딕셔너리의 Key를 기준으로 오름차순 정렬하는 방법
# dict = {'A' :1,'D' :4,'C' :3,'B' :2}
# sdict= sorted(dict.items(), reverse = True)

# 딕셔너리의 value를 기준으로 오름차순 정렬하는 방법
# dicts = {'A' :4,'D' :1,'C' :2,'B' :3}
# sdicts= sorted(dicts.items(), key=lambda x: -x[1])
