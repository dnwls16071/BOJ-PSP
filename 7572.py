# 예로부터 동아시아에서는 십간(十干)과 십이지(十二支)를 사용하여 연도를 표시하였다. 십간은 "갑을병정무기경신임계"를 말하며 십이지는 "자축인묘진사오미신유술해"를 말한다. 십간과 십이지로 구성된 간지를 사용하여 60년을 주기로 각 연도에 다음과 같이 이름을 부여한다: 최초 1년째는 "갑자"이고, 2년째는 "을축", 3년째는 "병인" 과 같이 올해의 간지에서 십간과 십이지의 다음 문자를 이듬해의 간지로 사용한다. 십간은 10년을 주기로, 십이지는 12년을 주기로 순환된다. 이런 순서로 하여 마지막 "계해"는 60년째를 나타내고, 61년째는 다시 "갑자"가 된다.

# 60갑자를 서양식으로 나타내기 위해 

# 십간을 0부터 9까지의 정수로 표현하고 
# 십이지를 "ABCDEFGHIJKL"로 표현하고
# 십간과 십이지의 순서를 바꾼다고 하자.
# 이를 서양식 간지 표현법이라고 부르자. 예를 들면, "갑자"는 "A0"로 "을축"은 "B1", "계해"는 "L9"으로 표현된다. 2013년은 계사년이므로 "F9"으로 표현되고, 2014년은 갑오년으로 "G0" 로 표현된다.

# 입력으로 주어진 연도를 서양식 간지 표현법으로 나타낸 것을 출력하는 프로그램을 작성하시오.

if __name__ == "__main__":
    N = int(input())
    a = "JKLABCDEFGHI"
    b = "7890123456"
    print(a[(N-1) % 12] + b[(N-1) % 10])

# 문제에서의 힌트에 주목해야한다.
# 예를 들어 입력한 값인 2060년은 E6이고, 2013년은 F9로 표현되어야한다.
# 십간은 0~9까지이므로 10으로 나눈 나머지가 되고, 십이지는 A~L까지이므로 12로 나눈 나머지가 된다.