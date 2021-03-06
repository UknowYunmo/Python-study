"""
스타트링크에서 판매하는 어린이용 장난감 중에서 가장 인기가 많은 제품은 구슬 탈출이다.
구슬 탈출은 직사각형 보드에 빨간 구슬과 파란 구슬을 하나씩 넣은 다음, 빨간 구슬을 구멍을 통해 빼내는 게임이다.
보드의 세로 크기는 N, 가로 크기는 M이고, 편의상 1×1크기의 칸으로 나누어져 있다.
가장 바깥 행과 열은 모두 막혀져 있고, 보드에는 구멍이 하나 있다.
빨간 구슬과 파란 구슬의 크기는 보드에서 1×1크기의 칸을 가득 채우는 사이즈이고, 각각 하나씩 들어가 있다.
게임의 목표는 빨간 구슬을 구멍을 통해서 빼내는 것이다. 이때, 파란 구슬이 구멍에 들어가면 안 된다.
이때, 구슬을 손으로 건드릴 수는 없고, 중력을 이용해서 이리 저리 굴려야 한다.
왼쪽으로 기울이기, 오른쪽으로 기울이기, 위쪽으로 기울이기, 아래쪽으로 기울이기와 같은 네 가지 동작이 가능하다.
각각의 동작에서 공은 동시에 움직인다. 빨간 구슬이 구멍에 빠지면 성공이지만, 파란 구슬이 구멍에 빠지면 실패이다.
빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패이다. 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다.
또, 빨간 구슬과 파란 구슬의 크기는 한 칸을 모두 차지한다.
기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지이다.
보드의 상태가 주어졌을 때, 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 구하는 프로그램을 작성하시오.
첫 번째 줄에는 보드의 세로, 가로 크기를 의미하는 두 정수 N, M (3 ≤ N, M ≤ 10)이 주어진다.
다음 N개의 줄에 보드의 모양을 나타내는 길이 M의 문자열이 주어진다.
이 문자열은 '.', '#', 'O', 'R', 'B' 로 이루어져 있다. '.'은 빈 칸을 의미하고,
'#'은 공이 이동할 수 없는 장애물 또는 벽을 의미하며, 'O'는 구멍의 위치를 의미한다.
'R'은 빨간 구슬의 위치, 'B'는 파란 구슬의 위치이다.
입력되는 모든 보드의 가장자리에는 모두 '#'이 있다.
구멍의 개수는 한 개 이며, 빨간 구슬과 파란 구슬은 항상 1개가 주어진다.
최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 출력한다.
만약, 10번 이하로 움직여서 빨간 구슬을 구멍을 통해 빼낼 수 없으면 -1을 출력한다.
"""
N,M=map(int,input().split())
game=[]
where_R=[0,0]
where_B=[0,0]
for i in range(0,N):
    game.append(input())
def find():
    for i in range(0,N):
        for j in range(0,M):
            if game[i][j]=='R':
                where_R[0]=i
                where_R[1]=j
    for i in range(0,N):
        for j in range(0,M):
            if game[i][j]=='B':
                where_B[0]=i
                where_B[1]=j
    return
def down():
    find()
    a=where_R[0]
    b=where_R[1]
    c=where_B[0]
    d=where_B[1]
    for i in range(a+1,N):
        if game[i][b]=="#":
            game[a]=game[a][0:b]+"."+game[a][b+1:]
            game[i-1]=game[i-1][0:b]+"R"+game[i-1][b+1:]
            break
    for i in range(c+1,N):
        if game[i][d]=="#":
            game[c]=game[c][0:d]+"."+game[c][d+1:]
            game[i-1]=game[i-1][0:d]+"B"+game[i-1][d+1:]
            break
    return
def right():
    find()
    a=where_R[0]
    b=where_R[1]
    c=where_B[0]
    d=where_B[1]
    for i in range(b+1,M):
        if game[a][b+1]=="#":
            break
        if game[a][i]=="#":
            game[a]=game[a][0:b]+"."+game[a][b+1:i-1]+"R"+game[a][i:]
            break
    for i in range(d+1,M):
        if game[c][d+1]=="#":
            break
        if game[c][i]=="#":
            game[c]=game[c][0:d]+"."+game[c][d+1:i-1]+"B"+game[c][i:]
    return

def left():
    find()
    a=where_R[0]
    b=where_R[1]
    c=where_B[0]
    d=where_B[1]
    for i in range(b-1,-1,-1):
        if game[a][b-1]=="#":
            break
        if game[a][i]=="#":
            game[a]=game[a][0:i+1]+"R"+game[a][i+2:b]+"."+game[a][b+1:]
            break
    for i in range(d-1,-1,-1):
        if game[c][d-1]=="#":
            break
        if game[c][i]=="#":
            game[c]=game[c][0:i+1]+"B"+game[c][i+2:d]+"."+game[c][d+1:]
            break
    return
def up():
    find()
    a=where_R[0]
    b=where_R[1]
    c=where_B[0]
    d=where_B[1]
    for i in range(a-1,-1,-1):
        if game[i][b]=="#":
            game[a]=game[a][0:b]+"."+game[a][b+1:]
            game[i+1]=game[i+1][0:b]+"R"+game[i+1][b+1:]
            break
    for i in range(a-1,-1,-1):
        if game[i][d]=="#":
            game[c]=game[c][0:d]+"."+game[c][d+1:]
            game[i+1]=game[i+1][0:d]+"B"+game[i+1][d+1:]
            break
    return
down()
down()
print("------내려--------")
for i in range(0,N):
    print(game[i])
print("------오른쪽--------")
right()
right()
for i in range(0,N):
    print(game[i])
print("------왼쪽--------")
left()
left()
for i in range(0,N):
    print(game[i])
print("------올려--------")
up()
up()
for i in range(0,N):
    print(game[i])
"""
왼쪽, 오른쪽, 아래, 위로 기울이는 함수를 만들었다!
이제 남은 가지 문제는 R과 B가 같은 라인에 있을 때 하나는 사라져버린다는 점
이걸 먼저 해결하고
마지막으로 최선의 수를 구하는 방법을 구상하면 될 거 같다 
"""