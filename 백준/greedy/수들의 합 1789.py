S=int(input())

N=0
result=0
for i in range(1,S+1):
    result+=i
    N+=1
    if result>S:
        N=N-1
        break;
print(N)


# S=int(input())

# n=1
# while n*(n+1)/2<=S:
#     n=n+1
# print(n-1)