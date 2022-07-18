n=int(input())
word=[]

for _ in range(n):
    word.append(input())

word=list(set(word))
word.sort() # 먼저 알파벳순으로
word.sort(key=lambda x:len(x)) # 그 다음에 길이순으로

for i in range(len(word)):
    print(word[i])