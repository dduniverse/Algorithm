s=list(input()) # 입력받은 문자열을 리스트로 만듦. 각 글자마자 다른 인덱스에 저장됨
s.reverse() # 앞글자를 pop하기 위해 역순으로 정렬시킴 (예. b,a,e,k,j,o,o,n -< n,o,o,j,k,e,a,b)

result=[]
word=[]

for _ in range(len(s)):
    result.append(''.join(s)) # 분리된 알파벳을 join시켜 result 리스트에 저장 (예. noojkeab)
    s.pop() # 한글자씩 pop (예. noojkea)

for i in result: # result에 있는 각 객체들을 거꾸로(=원래대로) 바꿔 word 리스트에 저장 (예. aekjoon)
    word.append(i[::-1])

word.sort() # word 리스트를 알파벳순으로 정렬
for i in word:
    print(i)