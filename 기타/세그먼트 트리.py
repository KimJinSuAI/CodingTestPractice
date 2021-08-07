import math
class segmentTree:
    def __init__(self, data):
        self.data = data
        self.last = len(data)-1
        self.height = math.ceil(math.log(len(data),2))
        self.tree = [0]*(1<<self.height+1)
        self.lazy = [0]*(1<<self.height+1)                  #lazy = b
        self.init(data, 0, len(data)-1,1)

    def lazyReflect(self, node, start, end):
        self.tree[node] += self.lazy[node]*(end-start+1)
        if start!=end:
            self.lazy[node*2] += self.lazy[node]
            self.lazy[node*2+1] += self.lazy[node]
        self.lazy[node] = 0

    def init(self, data, start, end, node):
        if start==end:
            self.tree[node] = data[start]
            return self.tree[node]
        else:   #좌측은 처음~중간까지. node//2, 우측은 중간~끝까지. node//2+1 
            mid = (start+end)//2
            self.tree[node] = (self.init(data,  start, mid, node*2) + self.init(data, mid+1, end, node*2+1))
            return self.tree[node]

    def query(self, left, right):
        return self.__qO__(1,left,right,0, self.last)

    def __qO__(self, node, left, right, start, end):
        if self.lazy[node]!=0:  #lazy reflect
            self.lazyReflect(node,start,end)

        if (left > end or right < start) :  #범위가 노드를 벗어남
            return 0
        elif (left <= start and end <= right):  #범위가 노드를 포함
            return self.tree[node]
        else:                               #범위가 노드를 걸침
            mid = (start+end)//2
            self.tree[node] = self.__qO__(node*2, left,right, start, mid) + self.__qO__(node*2+1, left, right, mid+1, end)
            return self.tree[node]

    def update(self, index, val):
        diff = val-self.data[index]
        self.data[index] = val
        return self.__uO__(1, 0, self.last, index, diff)

    def __uO__(self, node, start, end, index, diff):
        if self.lazy[node]!=0:  #lazy reflect
            self.lazyReflect(node,start,end)
        if index < start or index > end : return
        
        self.tree[node] += diff
        if start != end:
            mid = (start+end)//2
            self.__uO__(node*2, start, mid, index, diff)
            self.__uO__(node*2+1, mid+1, end, index, diff)

    def updatelazy(self, left, right, diff):
        self.data[left:right+1] = [x + diff for x in self.data[left:right+1]]
        return self.__ulO__(1, left, right, diff, 0, self.last)
    
    def __ulO__(self, node, left, right, diff, start, end):
        if self.lazy[node]!=0:  #lazy reflect
            self.lazyReflect(node,start,end)
            
        if (left > end or right < start) :  #범위가 노드를 벗어남
            return
        elif (left <= start and end <= right):  #범위가 노드를 포함
            self.tree[node] += diff*(end-start+1)
            if start!=end:
                self.lazy[node*2] += diff
                self.lazy[node*2+1] += diff
        else:                                   #범위가 노드를 걸침
            mid = (start+end)//2
            self.__ulO__(node*2, left, right, diff, start, mid)
            self.__ulO__(node*2+1, left, right, diff, mid+1, end)
            self.tree[node] = self.tree[node*2]+self.tree[node*2+1]

def solution(data):
    tmp = segmentTree(data)
    tmp.updatelazy(1,3,1)
    tmp.update(3,10)
    return tmp.query(0,9)

print(solution([0,1,2,3,4,5,6,7,8,9]))