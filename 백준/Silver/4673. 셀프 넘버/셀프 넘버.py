number=list(range(1,10000)) # 1에서 10000까지의 수
non_self=[] # 셀프 넘버가 아닌 수 = 생성자가 있는 수

for num in number: # ex. num=33
    for n in str(num): # num을 string으로 바꿔 한 자리씩 가져와
        num=num+int(n) # num에 각 자리를 더해줌 ex. 33+3+3
    if num<=10000: # 10000까지의 수이므로 10000보다 작을 떄만 리스트에 추가
        non_self.append(num)

non_self=set(non_self) # set으로 바꿔 중복값을 제거
self_number=set(number)-non_self # 10000까지의 수에서 셀프 넘버가 아닌 수 제거

for i in sorted(self_number): #set은 순서가 없으므로 정렬을 해주어야 함
    print(i) #셀프 넘버만 출력