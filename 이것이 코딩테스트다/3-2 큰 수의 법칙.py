n,m,k=map(int,input().split())
# a는 a개의 자연수 b는 몇번 더하는지 c는 특정 인덱스 연속해서 몇번더할수있는지
list=list(map(int,input().split()))

list.sort()


a=list[n-1]
b=list[n-2]

result=0
while 1:
    for i in range(k):
        if m==0:
            break
        result+=a
        m-=1
    if m==0:
        break
    result+=b
    m-=1

print(result)