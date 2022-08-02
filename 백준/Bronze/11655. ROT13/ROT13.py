str=input()
result=[]
for s in str:
    if s.isdigit():
        result.append(s)
    elif s.isspace():
        result.append(s)
    elif s.isupper():
        if (ord(s)+13)>90:
            s=64+((ord(s)+13)-90)
            result.append(chr(s))
        else:
            result.append(chr(ord(s)+13))
    elif s.islower():
        if (ord(s)+13)>122:
            s=96+((ord(s)+13)-122)
            result.append(chr(s))
        else:
            result.append(chr(ord(s)+13))

for i in result:
    print(i,end='')