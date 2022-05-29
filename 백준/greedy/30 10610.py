a=input()
a=sorted(a,reverse=True)
sum=0
#30의 배수 조건 뒷자리가 0이면서 각자리 합이 3으로 나누어진다
if '0' not in a:
    print(-1)
else:
    for i in a:
        sum=sum+int(i)
    if sum%3 !=0:
        print(-1)
    else:
        print("".join(a))