# 지훈이는 Sort 마스터다. 그래서 어떠한 N개의 원소를 가진 배열이 들어오더라도 암산으로 오름차순 정렬을 할 수 있다고 한다. 의심 많은 보성이는 지훈이를 테스트해 보기로 마음먹었다. 하지만 모든 원소를 일일이 다 확인하는 것은 너무 귀찮은 일이라 생각한 보성이는 정렬된 배열의 마지막 원소만 맞는지 확인해 보기로 했다.

# 보성이를 위하여 마지막 원소를 알려주는 프로그램을 만들어주자.

N = int(input())
arr = sorted(list(map(int, input().split())))
print(arr[N-1])