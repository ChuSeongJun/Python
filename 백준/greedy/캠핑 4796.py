i=1
while True:
    L, P, V=map(int,input().split())
    if L+P+V==0:
        break;
    result=(V//P)*L
    result=result+min((V%P),L)
    print('Case %d: %d' %(i,result))
    i+=1