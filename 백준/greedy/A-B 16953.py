# 2를 곱한다, 1을 수의 가장 오른쪽에 추가한다.
# A->B로 바꾸는 필요한 연산 최솟값
# 거꾸로 생각

a, b=map(int,input().split())

result=1

while 1:
    if (a==b):
        break
    elif (b%2 !=0 and b%10!=1) or (a>b):
        result=-1
        break
    else:
        if (b%10==1):
            b=b//10
            result+=1
        else:
            b=b//2
            result+=1

print(result)

# a, b=map(int,input().split())

# index=1

# while a<b:
#     if b%2==0:
#         b=b//2
#     elif str(b)[-1]=='1':
#         b=int(str(b)[:-1])
#     else:
#         break
#     index+=1
    
# if a==b:
#     print(index)
# else:
#     print(-1)