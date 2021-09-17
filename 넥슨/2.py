def paperCuttings(textLength, starting, ending):
    # Write your code here
    count = 0
    nodes = list(set(zip(starting,ending)))
    nodes.sort(key = lambda x: (x[0],x[1]))
    N = len(nodes)
    for i in range(N):
        end = nodes[i][1]
        n = N-i-1
        for j in range(i+1,N):
            if nodes[j][0]<=end:
                n-=1
            else:
                break
        count+=n
            
    return count
            


# print(paperCuttings(10,[1,1,6,7],[5,3,6,10]))
print(paperCuttings(10,[3,1,2,8,8],[5,3,7,10,10]))