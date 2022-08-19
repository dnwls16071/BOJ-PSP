#두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 

A, B = map(int, input().split())

print(A+B)
print(A-B)
print(A*B)
print(A//B) #몫을 자연수 형태로 출력하는 //과 몫을 실수 형태로 출력하는 /은 다르다.
print(A%B)