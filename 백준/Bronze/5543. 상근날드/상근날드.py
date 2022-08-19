high=int(input())
middle=int(input())
low=int(input())
coke=int(input())
cider=int(input())

burger=[high,middle,low]
drink=[coke,cider]

set=[]
for i in burger:
    for j in drink:
        set.append(i+j-50)
        
print(min(set))