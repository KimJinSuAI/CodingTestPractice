class Node(object):
    def __init__(self, value = None, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next


class doubleLinkedList(object):
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None, self.head)
        self.head.next = self.tail

    def append(self, Node):
        tmpnode = self.head
        while tmpnode.next!=self.tail:
            tmpnode = tmpnode.next
        Node.prev = self.tail.prev
        Node.next = self.tail
        Node.prev.next = Node
        self.tail.prev = Node

    def insert(self, node):
        node.prev.next = node
        node.next.prev = node
        
    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        if node.next==self.tail:
            return node.prev
        else:
            return node.next
        
        
        
def solution(n, k, cmd):
    dl = doubleLinkedList()
    for i in range(n):
        dl.append(Node(i))
    stck = []

    nowNode = dl.head.next
    for i in range(k):
        nowNode = nowNode.next

    for c in cmd:
        if c[0]=="U":#prev
            for u in range(int(c[2:])):
                nowNode = nowNode.prev
        elif c[0]=="D":#next
            for d in range(int(c[2:])):
                nowNode = nowNode.next
        elif c=="C":#remove
            stck.append(nowNode)
            nowNode = dl.remove(nowNode)
        else:#c=="Z"    #insert
            tmpNode = stck.pop()
            dl.insert(tmpNode)

    answer = ["X"]*n
    nowNode = dl.head.next
    while nowNode!=dl.tail:
        answer[nowNode.value] = "O"
        nowNode = nowNode.next
        
    return ''.join(answer)

print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(	8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
# print(solution(8,0,["C","C","C","C","C","C","C","C","Z"]))