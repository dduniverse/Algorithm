def isPrime(x):
    count = [0] * (x+1)
    for i in range(1, x+1):
        for j in range(1, int(i**0.5)+1):
            if i % j == 0:
                if i / j == j:
                    count[i] += 1
                else:
                    count[i] += 2
    return count

def solution(number, limit, power):
    return sum([power if i > limit else i for i in isPrime(number)])