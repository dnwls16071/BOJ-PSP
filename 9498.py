# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

test_score = int(input())

if test_score >= 90 and test_score <= 100:
    print("A") 
elif test_score >= 80 and test_score <= 89:
    print("B")
elif test_score >= 70 and test_score <= 79:
    print("C")
elif test_score >= 60 and test_score <= 69:
    print("D")
else:
    print("F") 