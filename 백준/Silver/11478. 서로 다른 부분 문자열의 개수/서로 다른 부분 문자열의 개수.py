from itertools import combinations

s=input() # 문자열
s_substring=[] # s의 부분문자열을 저장할 리스트

for i in range(len(s)): # 문자열 s의 모든 인덱스를 순차적으로 방문하여 슬라이싱하는 과정
    for j in range(i+1, len(s)+1): # 슬라이싱을 위해 i+1부터 len(s)+1까지 방문(i=len(s)이면, j=len(s)+1이어야 len(s)의 슬라이싱 가능)
        s_substring.append(s[i:j])

print(len(set(s_substring))) # 중복을 제거한 문자열 s의 부분문자열의 개수 출력