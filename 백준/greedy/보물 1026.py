N=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
result=0
for i in range(N):
    result=result+max(a)*min(b)
    a.remove(max(a))
    b.remove(min(b))
print(result)