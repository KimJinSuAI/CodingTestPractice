from collections import deque
def solution(a, edges):
    if sum(a)!=0:
        return -1
    answer = 0
    tree = {}
    for i in edges:
        tree[i[0]] = tree.get(i[0],set())
        tree[i[0]].add(i[1])
        tree[i[1]] = tree.get(i[1],set())
        tree[i[1]].add(i[0])
    queue = deque(sorted(tree, key=lambda x:len(tree[x])))

    while queue:
        node = queue.popleft()
        if len(tree[node])==1:
            if a[node]==0:
                tree[tree[node].pop()].remove(node)
                continue

            parent = tree[node].pop()
            tree[parent].remove(node)
            answer += abs(a[node])
            a[parent]+=a[node]
            a[node] = 0
            
        elif len(tree[node])>1:
            queue.append(node)
            
    return answer

print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]]), 9)
print(solution([0,1,0], [[0,1],[1,2]]), -1)