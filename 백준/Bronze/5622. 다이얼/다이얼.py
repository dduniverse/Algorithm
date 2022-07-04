text=input()
dial=['','1','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ','0']
time=0
count=0

for d in dial:
    count=count+1
    
    for t in text:
        if t in d:
            time=time+count

print(time)