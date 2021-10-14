class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, word):
        cur = self.root

        for char in word:
            if cur.next.get(char) is not None:
                cur = cur.next[char]
            else:
                cur.next[char] = Node(char)
                cur = cur.next[char]


class Node:
    def __init__(self, ch):
        self.ch = ch
        self.next = {}

def solution(strList):
    trie = Trie()
    for str in strList:
        trie.insert(str)
    return trie.root.next["a"].next

print(solution(["aa","bb","ab"]))
