# 문자열 S가 주어졌을 때, SHA-256 해시값을 구하는 프로그램을 작성하시오.

from hashlib import sha256

S = str(input()) 

print(sha256(S.encode()).hexdigest())