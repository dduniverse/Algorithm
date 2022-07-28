import sys

n,k=map(int,sys.stdin.readline().split())
people=[i for i in range(1,n+1)]
result=[]
index=0

while len(people)>0:
    index += k-1 # k번째 수 = 리스트에서 k-1번 인덱스

    if index >= len(people): # ㅔpeople 길이보다 index 번호가 크면 index 번호 조정
        index %= len(people) 

    result.append(str(people.pop(index))) # people에서 삭제한 글자는 result에 추가

print('<', ', '.join(result),'>',sep="")