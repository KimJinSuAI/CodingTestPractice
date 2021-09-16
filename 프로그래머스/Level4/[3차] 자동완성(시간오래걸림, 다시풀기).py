from collections import deque
def solution(words):
    words.sort()
    visited = {}
    for word in words:
        visited[word] = False
    Q = deque([("",words)])
    while Q:
        node,candidates = Q.popleft()
        count = []
        first = ""
        prefix = True
        newCandidates = []
        for word in candidates:
            if visited[word]:
                continue
            
            if word.startswith(node):
                if node==word:
                    visited[word] = len(node)
                    prefix = False
                    continue
                
                tmp = node+word[len(node)]
                count.append(tmp)
                newCandidates.append(word)
                if first=="":
                    first = word

        if len(count)==1 and node and prefix:
            visited[first] = len(node)
        else:
            count = set(count)
            for c in count:
                Q.append((c,newCandidates))
            
    answer = sum(visited.values())
    return answer

print(solution(["word","war","warrior","world","go","gone","guild"]	),15)
print(solution(["go","gone","guild"]),7)
print(solution(["abc","def","ghi","jklm"]),4)