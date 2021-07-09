# Bottom-up은 for문, Top-down은 재귀.   
# 재귀는 Stack Overflow 가능.. 모든면에서 Bottom-up이 우세
memo1 = []
memo2 = []
def dp(money):                                                  #Bottom-up
    memo1[len(money)-1]=money[len(money)-1]
    memo1[len(money)-2]=money[len(money)-2]
    memo2[len(money)-2]=money[len(money)-2]
    for i in range(len(money)-3,-1,-1):
        if i+3>len(memo1)-1:
            memo1[i] = money[i] + memo1[i+2]
            memo2[i] = money[i]
        else:
            memo1[i] = money[i] + max(memo1[i+2],memo1[i+3])
            memo2[i] = money[i] + max(memo2[i+2],memo2[i+3])
    memo1[0]-=money[0]
    return(max(memo2[0],memo1[1],memo1[2]))
        
def dp2(now, start, money):                                     #Top-down
    if now>len(money)-1:
        return 0
    elif memo1[now]!=0:
        return memo1[now]
    elif (now+1)%len(money) == start:
        memo1[now] = 0
    else:
        memo1[now] = money[now] + max(dp(now+2, start,  money), dp(now+3, start,  money))
    return memo1[now]

def solution(money):
    global memo1,memo2
    memo1 = [0]*len(money)
    memo2 = [0]*len(money)
    return dp(money)
    # x=[]
    # for i in range(3):
    #     memo1 = [0]*len(money)
    #     x.append(dp(i,i,money))
    # return max(x)
    
def solution2(a):                                                   #Bottom-up, 내꺼 거꾸로
    x1, y1, z1 = a[0], a[1], a[0]+a[2]
    x2, y2, z2 = 0, a[1], a[2]
    for i in a[3:]:
        x1, y1, z1 = y1, z1, max(x1, y1)+i
        x2, y2, z2 = y2, z2, max(x2, y2)+i
    return max(x1, y1, z2)

print(solution([1,2,3,1]), 4)
print(solution([1,1,4,1,4]), 8)
print(solution([1000,0,0,1000,0,0,1000,0,0,1000]), 3000)
print(solution([1000,1,0,1,2,1000,0]), 2001)
print(solution([1000,0,0,0,0,1000,0,0,0,0,0,1000]), 2000)
print(solution([1,2,3,4,5,6,7,8,9,10]), 30)
print(solution([0,0,0,0,100,0,0,100,0,0,1,1]), 201)
print(solution([11,0,2,5,100,100,85,1]), 198)
print(solution([1,2,3]), 3)
print(solution([91,90,5,7,5,7]), 104)
print(solution([90,0,0,95,1,1]), 185)
