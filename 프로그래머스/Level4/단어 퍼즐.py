from collections import deque
def solution(strs, t):
    strs.sort(key = lambda x: len(x), reverse = True)
    visited = {}
    Q = deque([])
    Q.append([0,'',0])    #비용, 방문문자, 인덱스
    min = -1
    while Q:
        cost, strg, index = Q.popleft()
        if visited.get(strg,False):
            continue
        visited[strg] = True
        if index == len(t):
            return cost

        target = t[index:]
        for str in strs:
            if target.startswith(str):
                Q.append([cost+1,strg+str,index+len(str)])
    return min

from collections import deque
def solution(strs, t):
    distance = [float("inf")]*(len(t)+1)            #dijkstra
    Q = deque([0])
    distance[0] = 0
    while Q:
        idx = Q.popleft()                           #노드는 길이다..
        target = t[idx:]
        for str in strs:
            if target.startswith(str):              #갈 수 있다.. 간선이 있다.
                tmp = idx+len(str)
                if distance[tmp]>distance[idx]+1:
                    distance[tmp] = distance[idx]+1
                    Q.append(tmp)
    return distance[-1] if distance[-1]!=float("inf") else -1


print(solution(["ba","na","n","a"],"banana"))
print(solution(["app","ap","p","l","e","ple","pp"],"apple"))
# print(solution(["ba","an","nan","ban","n"],"banana"))

# print(solution(["a","aa","aab","aac"]*10,"a"*20000))