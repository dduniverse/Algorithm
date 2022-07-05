n=int(input())
count=n # 모든 단어가 그룹단어라고 가정.

for i in range(n):
    word=input()

    for j in range(0,len(word)-1): # 인덱스는 0부터 시작, len(word)까지 하면 j+1이 단어의 index 범위를 넘어버리기 때문에 len(word)-1 까지
        if word[j]==word[j+1]:
            pass # pass : 실행할 것이 없을 때 사용, 빈 껍데기 if문이 필요할 때
        elif word[j] in word[j+1:]: # j번째 알파벳이 j+1부터 끝까지의 단어에 존재하면 그룹단어가 아니다.
            count=count-1
            break # 알파벳 하나만 조건을 만족하지 못해도 그 단어는 그룹단어가 아니므로 count-1를 한번만 진행하기 위해 break 작성

print(count)