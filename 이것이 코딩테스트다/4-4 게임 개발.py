

n, m = map(int, input().split())
a, b, direction = map(int, input().split())

d = [[0]*m for _ in range(n)]
# 방문한 위치 저장하기 위한 맵 생성해 0으로 초기화
d[a][b] = 1
# 현재 좌표 방문 처리

# 0 북쪽 1 동쪽 2 남쪽 3 서쪽

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

result = 0
turn = 0


def turn_left():
    global direction
    direction -= 1
    if direction == 0:
        direction = 3


while 1:
    turn_left()
    na = a+dx[direction]
    nb = b+dx[direction]
    if d[na][nb] == 0 and array[na][nb] == 0:
        d[na][nb] = 1
        a = na
        b = nb
        result += 1
        turn = 0
        continue
    else:
        turn += 1

    if turn == 4:
        na = a-dx[direction]
        nb = b-dy[direction]
        if array[na][nb] == 0:
            a = na
            b = nb
        else:
            break
        turn = 0

print(result)
