a=int(input())
seat=input()
number=seat.count('LL')

if number==1 or number==0:
    print(a)

else:
    b=a-(number-1)
    print(b)

# 내풀이

N = int(input())

member = input()

count = member.count('LL')

if (count <= 1): 
    print(len(member)) 

else: 
    print(len(member) - count + 1)

# 구글 풀이