a=int(input())
coin_list=list()
quarter=0
dime=0
nickel=0
penny=0
for i in range(a):
    coin_list.append(int(input()))

for i in range(a):
    z=int(coin_list[i])
    quarter=z//25
    dime=(z%25)//10
    nickel=((z%25)%10)//5
    penny=(((z%25)%10)%5)//1
    print(quarter,dime,nickel,penny)
    
# 내 풀이

T = int(input())

for _ in range(int(input())):
    C = int(input())
    d = [25, 10, 5, 1]
    li = []
    for n in d:
        li.append(C//n)
        C = C%n
print(*li)

# 구글 풀이