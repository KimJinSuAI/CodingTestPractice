def solution(words, queries):
    answer = []
    fTree = [{}for _ in range(10001)]
    eTree = [{}for _ in range(10001)]
    for word in words:
        key = ""
        l = len(word)
        fTree[l][key] = fTree[l].get(key,0)+1
        for i in range(l-1):
            key += word[i]
            fTree[l][key] = fTree[l].get(key,0)+1
        key +=word[-1]
        fTree[l][key] = fTree[l].get(key,0)+1
        
        word = word[::-1]
        key = ""
        eTree[l][key] = eTree[l].get(key,0)+1
        for i in range(l-1):
            key += word[i]
            eTree[l][key] = eTree[l].get(key,0)+1
        key += word[-1]
        eTree[l][key] = eTree[l].get(key,0)+1

    for query in queries:
        if query[0]!="?":
            index = query.index("?")
            key = query[:index]
            count = fTree[len(query)].get(key,0)
        else:
            query = query[::-1]
            index = query.index("?")
            key = query[:index]
            count = eTree[len(query)].get(key,0)
        answer.append(count)

    return answer

print(solution(	["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?","?????"]))