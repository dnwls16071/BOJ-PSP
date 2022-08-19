# 첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

import sys
input = sys.stdin.readline
text = list(sys.stdin.readline())
alphabet_lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(len(alphabet_lst)):  # 알파벳리스트 길이만큼 반복
    print(text.count(alphabet_lst[i]), end=" ") # 알파벳리스트의 i번째 값에 해당하는 것을 카운트하여 나열하기
