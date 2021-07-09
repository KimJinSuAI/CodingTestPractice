def dfs(begin, target, words):
    if begin == target:
        return 0
    elif len(words)==0:
        return 9999
    else:    
        minimum = []
        for word in words:
            tmp =0
            for b,w in zip(begin,word):
                if b!=w:
                    tmp+=1
            if tmp==1:
                tmpWords = words.copy()
                tmpWords.remove(word)
                minimum.append(1+dfs(''.join(list(word)),target,tmpWords))
            else:
                minimum.append(9999)
                 
        return min(minimum)

def solution(begin, target, words):
    answer = dfs(begin,target,words)
    if answer>=9999:
        return 0
    else:
        return answer

        
print(solution("hit","cog",["hot", "dot", "dog", "lot", "log"]))
print(solution("hit","cog",["hot", "dot", "dog", "lot", "log","cog"]))



from collections import deque


def get_adjacent(current, words):
    for word in words:
        if len(current) != len(word):
            continue

        count = 0
        for c, w in zip(current, word):
            if c != w:
                count += 1

        if count == 1:
            yield word


def solution2(begin, target, words):
    dist = {begin: 0}
    queue = deque([begin])

    while queue:
        current = queue.popleft()

        for next_word in get_adjacent(current, words):
            if next_word not in dist:
                dist[next_word] = dist[current] + 1
                queue.append(next_word)

    return dist.get(target, 0)