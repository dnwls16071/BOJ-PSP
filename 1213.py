# 임한수와 임문빈은 서로 사랑하는 사이이다.

# 임한수는 세상에서 팰린드롬인 문자열을 너무 좋아하기 때문에, 둘의 백일을 기념해서 임문빈은 팰린드롬을 선물해주려고 한다.

# 임문빈은 임한수의 영어 이름으로 팰린드롬을 만들려고 하는데, 임한수의 영어 이름의 알파벳 순서를 적절히 바꿔서 팰린드롬을 만들려고 한다.

# 임문빈을 도와 임한수의 영어 이름을 팰린드롬으로 바꾸는 프로그램을 작성하시오.

if __name__ == "__main__":
    from itertools import combinations
    English_name = input()
    lst = combinations(English_name, 4)
    flag = True
    for i in lst:
        length = len(i)
        for j in range((length//2)+1):
            if i[j] == i[length-j]:
                continue
            else:
                flag = False
                break
        
        result = []
        if flag == True:
            result.append(i)
        if result == []:
            print("I'm Sorry Hansoo")
    print(*result)