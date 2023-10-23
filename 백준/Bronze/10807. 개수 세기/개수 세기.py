n = int(input())
nums = list(map(int, input().split()))
v = int(input())

for i in nums:
    if i != v:
        n -= 1
        
print(n)