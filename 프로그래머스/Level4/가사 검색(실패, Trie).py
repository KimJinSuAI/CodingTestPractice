class Trie:
    def __init__(self):
        self.root = Node(None, 0)

    def insert(self, word):
        cur = self.root
        cur.count +=1
        for char in word:
            if cur.next.get(char) is not None:
                cur = cur.next[char]
                cur.count+=1
            else:
                cur.next[char] = Node(char, 1)
                cur = cur.next[char]

class Node:
    def __init__(self, ch, count):
        self.ch = ch
        self.count = count
        self.next = {}

def solution(words, queries):
    answer = []
    fTries, rTries = dict(), dict()
    for word in words:
        if not fTries.get(len(word),False):
            fTries[len(word)] = Trie()
        fTries[len(word)].insert(word)

        if not rTries.get(len(word),False):
            rTries[len(word)] = Trie()
        rTries[len(word)].insert(word[::-1])
    
    for query in queries:
        if not fTries.get(len(query),False):
            answer.append(0)
        else:
            if query[0]!="?":
                cur = fTries[len(query)].root
                for q in query:
                    if q=="?":
                        answer.append(cur.count)
                        break
                    elif not cur.next.get(q,False):
                        answer.append(0)
                        break
                    else:
                        cur = cur.next[q]
            else:
                query = query[::-1]
                cur = rTries[len(query)].root
                for q in query:
                    if q=="?":
                        answer.append(cur.count)
                        break
                    elif not cur.next.get(q,False):
                        answer.append(0)
                        break
                    else:
                        cur = cur.next[q]

    return answer

print(solution(	["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?","?????"]))