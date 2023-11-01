s, p = map(int, input().split()) # DNA 문자열 길이, 비밀번호 부분 문자열 길이
dna = input() # DNA 문자열
a, c, g, t = map(int, input().split()) # 'A', 'C', 'G', 'T'의 최소 개수
password = 0 # 만들 수 있는 비밀번호의 개수

count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

for i in range(s-p+1):
    # 초기 길이 p의 문자열의 acgt 개수 파악
    if i == 0:
        for j in range(p):
            count[dna[j]] += 1
    # 한 칸 씩 이동하며 왼쪽 값 -1(제거), 오른쪽 값 +1(추가)
    else:
        count[dna[i-1]] -= 1
        count[dna[i-1+p]] += 1

    # 조건에 맞는 지 확인 후 개수 +1
    if count['A'] >= a and count['C'] >= c and count['G'] >= g and count['T'] >= t:
        password += 1

print(password)