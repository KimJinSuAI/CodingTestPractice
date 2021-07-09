from collections import Counter
def quad(arr):
    first = arr[0][0]
    for i in range(len(arr)):
        for j in range(0,len(arr)):
            if i==0 and j==0:
                continue
            if arr[i][j] != first:
                x = len(arr)//2
                if x==1:
                    return Counter({'0':arr[0].count(0)+arr[1].count(0), 
                    '1':arr[0].count(1)+arr[1].count(1)})
                else:
                    a = quad([arr[i][:x] for i in range(x)])
                    b =  quad([arr[i][x:] for i in range(x)])
                    c =  quad([arr[i][:x] for i in range(x,len(arr))])
                    d =  quad([arr[i][x:] for i in range(x,len(arr))])
                    
                    return a+b+c+d
    else:
        return Counter({str(first):1})

def solution(arr):
    x = quad(arr)
    return [x['0'],x['1']]

# print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]), [4,9])
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))