a=int(input())
coin=[500,100,50,10,5,1]
result=0
rest=1000-a
for i in coin:
    result=result+rest//i
    rest=rest%i
print(result)



# a = 1000 - int(input())
# b = [500, 100, 50, 10, 5, 1]
# count = 0
# for i in b:
#     count += a // i
#     a %= i
# print(count)


# 구글 풀이
