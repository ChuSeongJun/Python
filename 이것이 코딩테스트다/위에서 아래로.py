n=int(input())

array=[]
for i in range(n):
    array.append(int(input()))

array=sorted(array, reverse=True)

for i in array:
    print(i,end=' ')
    
    
# n=int(input())

# array=[]
# for i in range(n):
#     array.append(int(input()))
    
# count = [0]*(max(array)+1)

# for i in range(len(array)):
#     count[array[i]]+=1
    
# for i in range(len(count)):
#     for j in range((count[i])):
#         print(i,end=' ')
# 계수정렬