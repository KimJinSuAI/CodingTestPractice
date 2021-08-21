import heapq
def solution(strs, t):
    strs.sort(key = lambda x: len(x), reverse = True)
    visited = {}
    Q = []
    heapq.heappush(Q,[0,'',0])    #비용, 방문문자, 인덱스
    min = -1
    while Q:
        cost, strg, index = heapq.heappop(Q)
        if visited.get(strg,False):
            continue
        visited[strg] = True
        if index == len(t):
            if min==-1 or min>cost:
                min = cost

        for str in strs:
            if str == t[index:index+len(str)]:
                heapq.heappush(Q,[cost+1,strg+str,index+len(str)])
    return min

from collections import deque
def solution(strs, t):
    distance = [float("inf")]*(len(t)+1)
    Q = deque([])
    for str in strs:
        if t.startswith(str):
            distance[len(str)] = 1
            Q.append(len(str))
    while Q:
        idx = Q.popleft()
        target = t[idx:]
        for str in strs:
            if target.startswith(str):
                tmp = idx+len(str)
                if distance[tmp]>distance[idx]+1:
                    distance[tmp] = distance[idx]+1
                    Q.append(tmp)
    return distance[-1] if distance[-1]!=float("inf") else -1


# print(solution(["ba","na","n","a"],"banana"))
print(solution(["app","ap","p","l","e","ple","pp"],"apple"))
# print(solution(["ba","an","nan","ban","n"],"banana"))

# print(solution(["a","aa","aab","aac"]*10,"a"*20000))