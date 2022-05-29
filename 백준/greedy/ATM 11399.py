number=int(input())
customer_list=list(map(int,input().split()))
time=0
customer_list.sort()

for i in range(number):
    for j in range(i+1):
        time=time+customer_list[j]

print(time)
    
    
#sort sort는 리스트 오름차순 정렬을 할 때 사용한다.