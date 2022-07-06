x=int(input()) # x번째 분수
line=1 #몇번째 줄인지. 초기값은 1 -> 1/1은 1번째 줄이므로. line값=해당 line에 있는 분수의 개수

while x>line:
    x=x-line # x가 존재하는 line에서 x가 몇 번째에 존재하는지 알기위해 x에서 앞 line을 빼준다.
    line=line+1 # 다음 line으로 가기 위해 line+1

if line%2==0: #짝수번째 line이면 
    s=x # 분자는 1,2,3,4.. 순으로 진행되므로, x값(분수가 몇번 째에 존재하는지)이 곧 분자값이 된다.
    m=line-x+1 # 분모는 ..3,2,1순으로 진행되어 line-분자+1 이라는 규칙을 알 수 있다.
else: # 홀수번째 line이면
    s=line-x+1 # 분자는 ..3,2,1순으로 진행되어 line-분모+1 이라는 규칙
    m=x # 분모가 1,2,3,4.. 순으로 진행되므로, x값이 분모값이다.

print('{}/{}'.format(s,m))