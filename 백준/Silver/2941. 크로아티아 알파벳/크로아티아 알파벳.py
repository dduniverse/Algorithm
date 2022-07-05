word=input()
c_alp=['c=','c-','dz=','d-','lj','nj','s=','z=']

for c in c_alp:
    if c in word:
        word=word.replace(c,'*') # replace(바꾸고자 하는 문자, 새로 바꿀 문자)

print(len(word))