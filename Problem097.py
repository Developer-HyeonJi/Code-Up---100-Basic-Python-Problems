#다 0으로 세팅
h, w = map(int, input().split())

#격자판 생성
pan = []

for i in range(h+1):
    pan.append([])
    for j in range(w+1):
        pan[i].append(0)

#막대의 개수 입력
n = int(input())

for k in range(n):
    #막대의 길이(l), 방향(d), 좌표(x, y) 입력 받기
    l, d, x, y = map(int, input().split())
    
    if d == 0:
        for m in range (l):
            pan[x][y+m] = 1

    else:
        for n in range(l):
            pan[x+n][y] = 1

#격자판 모두 출력
for i in range(1, h+1):
    for j in range(1, w+1):
        print(pan[i][j], end=' ')
    print()
