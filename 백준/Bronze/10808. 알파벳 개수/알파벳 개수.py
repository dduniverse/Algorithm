s=input()

alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alp_count=[0]*26 # alp 개수만큼 미리 개수에 대한 리스트를 만들어 둠

for a in alp:
    alp_count[alp.index(a)]=s.count(a)
    # alp에서 a의 인덱스를 번호를 찾아 alp_count리스트의 해당하는 인덱스에 s에서 a의 개수를 세어 저장

print(*alp_count)