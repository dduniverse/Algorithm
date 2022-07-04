s=input()
c='abcdefghijklmnopqrstuvwxyz'

for i in c:
    print(s.find(i), end=' ') # c에서 한 글자씩 가져와 s에서 찾기
    # find() 함수
    # 어떤 찾는 문자가 문자열 안에서 첫 번째에 위치한 순서를 숫자로 출력
    # 찾는 문자가 문자열 안에 없는 경우에는 -1을 출력하는 함수