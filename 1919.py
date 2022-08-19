# 두 영어 단어가 철자의 순서를 뒤바꾸어 같아질 수 있을 때, 그러한 두 단어를 서로 애너그램 관계에 있다고 한다. 예를 들면 occurs 라는 영어 단어와 succor 는 서로 애너그램 관계에 있는데, occurs의 각 문자들의 순서를 잘 바꾸면 succor이 되기 때문이다.

# 한 편, dared와 bread는 서로 애너그램 관계에 있지 않다. 하지만 dared에서 맨 앞의 d를 제거하고, bread에서 제일 앞의 b를 제거하면, ared와 read라는 서로 애너그램 관계에 있는 단어가 남게 된다.

# 두 개의 영어 단어가 주어졌을 때, 두 단어가 서로 애너그램 관계에 있도록 만들기 위해서 제거해야 하는 최소 개수의 문자 수를 구하는 프로그램을 작성하시오. 문자를 제거할 때에는 아무 위치에 있는 문자든지 제거할 수 있다.

if __name__ == "__main__":
    from collections import Counter
    a = Counter(input())
    b = Counter(input())
    print(sum((a-b).values()) + sum((b-a).values()))

# 처음 작성한 코드
if __name__ == "__main__":
    first_word = list(input())
    second_word = list(input())

    cnt = 0
    for i in first_word:
        if i not in second_word:
            cnt += 1

    for j in second_word:
        if j not in first_word:
            cnt += 1
    print(cnt)

# Counter 함수는 문자열 내 각 문자의 개수를 세어 딕셔너리로 itertable한 형태로 반환해주는 함수로 디폴트 정렬 형식은 내림차순이다.
# collections 라이브러리의 Counter함수에 대해서 공부할 수 있었던 문제였다.

# collections 라이브러리
from collections import Counter

a = Counter(input())    # ex. aabbcc
b = Counter(input())    # ex. xxyybb
print(a-b)  # a집합에서 a와 b의 교집합 부분을 제외한 부분   >   Counter({'a': 2, 'c': 2})   
print(b-a)  # b집합에서 a와 b의 교집합 부분을 제외한 부분   >   Counter({'x': 2, 'y': 2})
print(a+b)  # a와 b를 더한 형태    >     Counter({'b': 4, 'a': 2, 'c': 2, 'x': 2, 'y': 2})