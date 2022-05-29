# 6개의 패키지
# a 끊어진 기타줄, b기타줄 브랜드 개수
# 각 브랜드 6개의 가격, 개당 가격

a,b=map(int, input().split())


multi_list=list()
single_list=list()

for i in range(b):
    z,y=(map(int, input().split()))
    multi_list.append(z)
    single_list.append(y)
    
c=min(multi_list)
d=min(single_list)

result=0

if c>d*6:
    result=d*6

elif c<(a%6)*d:
    result=c*(a//6)+c
    
else:
    result=c*(a//6)+d*(a%6)
    
print(result)




# 권오현 코드
# n, m = map(int, input().split())
# p6 = []
# p1 = []
# for i in range(m):
#     a, b = map(int, input().split())
#     p6.append(a)
#     p1.append(b)
# p6.sort()
# p1.sort()

# if(n>=6):
#     price1 = p6[0] * (n//6)
#     price2 = price1
#     price1 += p6[0]
#     price3 = p1[0] * n
    
#     n %= 6
#     if(n > 0):
#         price2 += p1[0] * n
#     print(min(price1, price2, price3))
# else:
#     s1 = p1[0] * n
#     s6 = p6[0]
#     price = min(s1, s6)
#     print(price)