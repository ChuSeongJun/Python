n=int(input())
a=input().split()

x,y=1,1

# L왼쪽 R오른쪽 U 위로 D 아래로

dx=[0,0,-1,1]
dy=[-1,1,0,0]

moving=['L','R','U','D']

for i in a:
    for j in range (len(moving)):
        if i==moving[j]:
            nx=x+dx[j]
            ny=y+dy[j]
    
    if nx<1 or ny<1 or nx>n or ny>n:
        continue
    x,y=nx,ny
    
print(x,y)