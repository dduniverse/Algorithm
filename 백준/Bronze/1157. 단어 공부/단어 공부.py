word=input().upper() # 대문자로 바꿔줌
s_word=list(set(word)) # set을 이용해 중복된 알파벳 제거
cnt=[]

for s in s_word:
    cnt.append(word.count(s)) # count() 함수:문자열에서 's'의 개수

if cnt.count(max(cnt))>1: # cnt 리스트의 최댓값 개수가 1개 보다 많으면
    print('?')
else:
    print(s_word[cnt.index(max(cnt))]) # index 함수: 몇번째 인덱스인지
    # s_word에서 한글자씩 순서대로 가져와 개수를 cnt에 저장하므로 
    # cnt의 인덱스번호 = s_word의 인덱스 번호 