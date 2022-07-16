n=int(input())

for i in range(1,n+1): # 1에서 n까지의 수 중 하나 i
    result=sum(map(int,str(i)))+i 
    # i를 문자열로 바꾼 후, 각 자리를 다시 정수로 바꿔 합을 구한다. 
    # 그 합과 i를 더한 값을 result라고 할 때

    if result==n: # result가 n과 같으면
        print(i) # i는 n의 생성자이다.
        break

    if i==n: # i가 n까지 진행되었으면 생성자가 없는 것이므로 0 출력
        print(0)