class Trie:
    def __init__(self):
        self.root = Node(None, 0)

    def insert(self, word):
        self.root.count += 1
        cur = self.root

        for char in word:
            if cur.next.get(char) is not None:
                cur = cur.next[char]
                cur.count += 1
            else:
                cur.next[char] = Node(char, 1)
                cur = cur.next[char]


class Node:
    def __init__(self, ch, count):
        self.ch = ch
        self.count = count
        self.next = {}


def get_match_nums(query):
    global forward_tries, reversed_tries

    if query[0] == '?':
        if reversed_tries.get(len(query)) is not None:
            trie = reversed_tries[len(query)].root
            query = query[::-1]
        else:
            return 0

    else:
        if forward_tries.get(len(query)) is not None:
            trie = forward_tries[len(query)].root
        else:
            return 0

    for char in query:
        if char == '?':
            return trie.count
        elif trie.next.get(char) is None:
                return 0

        trie = trie.next[char]


def pre_processing(words):
    global forward_tries, reversed_tries

    forward_tries, reversed_tries = dict(), dict()

    for word in words:
        if forward_tries.get(len(word)) is None:
            forward_tries[len(word)] = Trie()
        forward_tries[len(word)].insert(word)

        reversed_word = word[::-1]
        if reversed_tries.get(len(reversed_word)) is None:
            reversed_tries[len(reversed_word)] = Trie()
        reversed_tries[len(word)].insert(reversed_word)


def solution(words, queries):
    global forward_tries, reversed_tries

    pre_processing(words)
    return [get_match_nums(query) for query in queries]
