import sys

def mazeFind(x , y):
    if(x < 0 or y < 0 | x >= N or y >= N): # 미로 외부인가?
        return False
    elif(maze[x][y] != PATHWAY_COLOR): # 벽(1)인가? 혹은 막히거나 방문(2 ,3)한 곳인가? > 길이아닌가?
        return False
    elif(x == N-1 & y == N-1): # 출구인가?
        maze[x][y] = PATH_COLOR # 최종목적지는 가능한 길이므로 가능하다고 변경
        return True
    else: # x, y값이 미로 내부다... 
        maze[x][y] = PATH_COLOR # maze가 아직 확실한 판단전에 방문여부만 체크
        if(mazeFind(x-1,y) | mazeFind(x,y+1) | mazeFind(x+1,y) | mazeFind(x,y-1)): # 현재 위치에서 4방향이 가능한지
            return True
        maze[x][y] = BLOCKED_COLOR # 위의 if를 통과 못한 것은 이 위치가 출구로 가는 길목이 아니다라는 것을 의미하므로 dead end
        return False

N = 8
maze = [[0, 0, 0, 0, 0, 0, 0, 1],
        [0, 1, 1, 0, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 1, 1, 0, 0],
        [0, 1, 1, 1, 0, 0, 1, 1],
        [0, 1, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 1],
        [0, 1, 1, 1, 0, 1, 0, 0]]

PATHWAY_COLOR = 0 # 원래 길
WALL_COLOR = 1 # 벽
BLOCKED_COLOR = 2 # 이 길로 계속 가면 가다 도중에 막히는 길
PATH_COLOR = 3 # 이 길로 계속 가면 끝까지 갈 수 있는 길

mazeFind(0,0)

for i in range(0,N):
    print(maze[i])