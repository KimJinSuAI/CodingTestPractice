from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    board2 = [[0]*101 for _ in range(101)]
    rectangle.sort(key = lambda x:x[0])
    for x1,y1,x2,y2 in rectangle:
        x1*=2;y1*=2;x2*=2;y2*=2
        for x in range(x1,x2+1):
            board2[y1][x]+=1
            board2[y2][x]+=1
        for y in range(y1+1,y2):
            board2[y][x1]+=1
            board2[y][x2]+=1
        for y in range(y1+1,y2):
            for x in range(x1+1,x2):
                board2[y][x]=6



    d = [[1,0],[-1,0],[0,1],[0,-1]]
    Q = deque([[0,characterY*2,characterX*2]])
    visited = [[False]*101 for _ in range(101)]
    itemY*=2;itemX*=2
    ans = 1e9
    while Q:
        dis,y,x = Q.popleft()
        if [y,x]==[itemY,itemX]:
            ans = min(ans,dis)
        elif not visited[y][x]:
            visited[y][x] = True
            for dy,dx in d:
                ny,nx = y+dy,x+dx
                if -1<ny<101 and -1<nx<101 and 0<board2[ny][nx]<3 and not visited[ny][nx]:
                    Q.append([dis+1,ny,nx])
    # for i in range(20):
    #     print(board2[i][:20])
    return ans//2
print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]],1,3,7,8))
# print(solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]],9,7,6,1))
# print(solution([[1,1,3,7],[2,2,7,4],[4,3,6,6]] , 1 , 2, 6, 6))