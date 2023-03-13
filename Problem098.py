#격자판 생성
d=[]

#10*10의 격자판 틀 
for i in range(11) :
  d.append([])
  for j in range(11) : 
    d[i].append(0)

#입력받은 좌표 입력 
for i in range(10) :
  a = input().split()
  for j in range(10) :
    d[i+1][j+1] = a[j]

#(2,2) 좌표에서 시작
i=2
j=2

#개미집이 있는 곳까지 이동
while(d[i][j]!='2'):
    d[i][j]='9'
    #만약 오른쪽에 길이 있다면
    if(d[i][j+1]=='0'):
        #오른쪽으로 이동
        j=j+1

    #만약 옆이 벽이라면
    #아래로 이동한다
    else:
        #아래로 이동
        i=i+1

#모든 좌표 출력
for i in range(1, 11) :
  for j in range(1, 11) : 
    print(d[i][j], end=' ')
  print()
