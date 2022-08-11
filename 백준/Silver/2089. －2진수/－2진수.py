n=int(input())

if n==0:
    print(0)
else:
    ans=''
    while n: # n값이 존재하면
        ans+=str(n%2) # n을 2로 나눈 나머지를 문자열로 ans에 추가
        n=n//2 # n을 2로 나눈 몫을 n에 저장
        n*=(-1) # n에 -1을 곱해줌(위에서 2로 나누었기 때문에 -2로 나눈 몫은 -1를 곱해주어야 함)
    print(ans[::-1]) # ans를 뒤에서부터 거꾸로 출력함