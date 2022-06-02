n,m=map(int,input().split())
a,b,d=map(int,input().split())
# 0 북쪽 1동쪽 2남쪽 3서쪽

array=[]
for i in range(n):
    array.append(list(map(int,input().split())))

dx=[-1,0,1,0]
dy=[0,1,0,-1]


    