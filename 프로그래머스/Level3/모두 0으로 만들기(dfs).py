import sys
sys.setrecursionlimit(10**8)
def dfs(node):
    global answer
    visited[node] = True
    if len(tree[node])==1:
        answer+=abs(a[node])
        a[tree[node][0]] += a[node]
        a[node] = 0
        if not visited[tree[node][0]]:
            dfs(tree[node][0])
        return
    else:
        for n in tree[node]:
            if not visited[n]:
                dfs(n)
                if a[n]!=0:
                    answer+= abs(a[n])
                    a[node]+=a[n]
                    a[n] = 0
        return
            



def solution(A, edges):
    global tree,a, visited, answer
    a=A
    answer = 0
    if sum(a)!=0:
        return -1
    tree = [[] for _ in range(len(a))]
    visited = [False  for _ in range(len(a))]
    for i in edges:
        tree[i[0]].append(i[1])
        tree[i[1]].append(i[0])
    dfs(0)
    return answer

print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]]), 9)
print(solution([0,1,0], [[0,1],[1,2]]), -1)