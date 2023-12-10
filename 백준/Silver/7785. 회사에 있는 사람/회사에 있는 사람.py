n = int(input())
company = {}
for _ in range(n):
    name, record = input().split() # 출입기록
    if record == 'enter':
        company[name] = 1
    else:
        company[name] = 0

# 현재 회사에 있는 사람의 이름을 사전 순의 역순으로 출력
for key, value in sorted(company.items(), reverse=True):
    if value == 1:
        print(key)