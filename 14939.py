# 세준이는 도서관에서 일한다. 도서관의 개방시간이 끝나서 세준이는 사람들이 마구 놓은 책을 다시 가져다 놓아야 한다. 세준이는 현재 0에 있고, 사람들이 마구 놓은 책도 전부 0에 있다. 각 책들의 원래 위치가 주어질 때, 책을 모두 제자리에 놔둘 때 드는 최소 걸음 수를 계산하는 프로그램을 작성하시오. 세준이는 한 걸음에 좌표 1칸씩 가며, 책의 원래 위치는 정수 좌표이다. 책을 모두 제자리에 놔둔 후에는 다시 0으로 돌아올 필요는 없다. 그리고 세준이는 한 번에 최대 M권의 책을 들 수 있다.

N, M = map(int, input().split())
book = list(map(int, input().split()))

positive = []
negative = []
for i in book:
    if i > 0:
        positive.append(i)
    elif i < 0:
        negative.append(i)
positive.sort(reverse=True)
negative.sort()
distance = []
for i in range(len(negative)//M):
    distance.append(abs(negative[i*M]))
if len(negative) % M > 0:
    distance.append(abs(negative[(len(negative)//M)*M]))

for i in range(len(positive)//M):
    distance.append(positive[i*M])
if len(positive) % M > 0:
    distance.append(positive[(len(positive)//M)*M])

distance.sort()
walking = 0
for i in range(len(distance)-1):
    walking += (distance[i] * 2)
print(walking + max(distance))

# 절대값을 기준으로 가장 멀리 있는 값부터 M개씩 묶어서 묶은 값의 최댓값을 저장해준다.
# 위의 과정을 반복하고나서 최소 걸음수를 구하는 방법은 리스트의 최댓값을 제외한 나머지 값들을 *2 처리하여 더해주고 최댓값은 편도로 처리하여 그냥 더해준다.
# 묶는 과정에서 포함되지않는 경우 역시 왕복으로 처리해줘야하므로 나머지 연산은 별도로 수행해줘야한다.

# 이 문제의 테스트케이스 출력이 어떻게 도출되는지 그려보면서 이해하려고 했지만 잘 이해가 되지 않아 다른 코드들을 참고했었다.
# 그리디 알고리즘 문제를 많이 접해보면서 최적의 해를 구하는 방법을 많이 생각해봐야겠다.
