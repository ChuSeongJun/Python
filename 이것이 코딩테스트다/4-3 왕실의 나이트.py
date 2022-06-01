# 나이트는 앞으로 두칸이동후 수직으로 한칸 이동가능
# 8*8좌표평면이 있을때 나이트가 n에 있을때 이동가능한 경우의 수는?
# 행과 열로 구성된 좌표 평면
# 갈수있는 경우의 수 2,1  2,-1  -2,1  -2,-1  -1,-2  1,-2  -1,2  1,2  총 8개  행, 열
# 아스키코드 반환 ord("A")   숫자에 맞는 아스키코드 반환  chr(65)

n=input()

row=int(ord(n[0]))-int(ord("a"))+1
column=int(n[1])

result=0

dx=[2,2,-2,-2,-1,1,-1,1]
dy=[1,-1,1,-1,-2,-2,2,2]

for i in range(len(dx)):
    nx=row+dx[i]
    ny=column+dy[i]
    if nx>=1 and nx<=8 and ny<=8 and ny>=1:
        result+=1

print(result)