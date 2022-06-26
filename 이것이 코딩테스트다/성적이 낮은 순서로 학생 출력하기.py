

n=int(input())

array=[]

for i in range(n):
    a,b=input().split()
    array.append((a,int(b)))

array= sorted(array, key=lambda x : int(x[1]))

for i in array:
    print(i[0],end=' ')