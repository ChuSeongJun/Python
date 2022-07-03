n=int(input())
result=0


coin = [500, 100, 50, 10]

for i in coin:
    result += n // i 
    n %= i

print(result)
# 