while True:
    try:
        s=input()
    except EOFError:
        break
    
    s_low, s_upp, s_num, s_space=0,0,0,0

    for i in s:
        if i.islower(): # 소문자인지
            s_low+=1
        if i.isupper(): # 대문자인지
            s_upp+=1
        if i.isdigit(): # 숫자인지
            s_num+=1
        if i.isspace(): # 공백인지
            s_space+=1    
    print(s_low, s_upp, s_num, s_space)