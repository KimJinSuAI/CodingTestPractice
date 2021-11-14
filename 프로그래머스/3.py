def solution(n, m, x, y, queries):
    l,r,u,d = y,y,x,x
    for idx in range(len(queries)-1,-1,-1):
        i,dis = queries[idx]
        if i==0:    #좌
            r = min(m-1,r+dis)
            if l!=0:
                l+=dis
                
        elif i==1:  #우
            l = max(0,l-dis)
            if r!=m-1:
                r-=dis
                
        elif i==2:  #상
            d = min(n-1,d+dis)
            if u!=0:
                u+=dis
        else:       #하
            u = max(0,u-dis)
            if d!=n-1:
                d-=dis
        
    if l>r or u>d:
        return 0

    return (d-u+1)*(r-l+1)

    



        

print(solution(2, 2, 0, 0, [[2, 1], [0, 1], [1, 1], [0, 1], [2, 1]]), 4)
print(solution(2, 5, 0, 1, [[3, 1], [2, 2], [1, 1], [2, 3], [0, 1], [2, 1]]), 2)
print(solution(1000,1000,1,1,[[0,100001],[2,100001]]))