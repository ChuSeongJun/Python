i=input()
i=int(i)

if i%10 !=0:
    print(-1)
else:
    a=0
    b=0
    c=0
    a=i//300
    b=(i%300)//60
    c=((i%300)%60)//10
    print(a,b,c)
    