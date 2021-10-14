class penwickTree:
    def __init__(self, data):
        self.tree = [0]*(len(data)+1)    #공간복잡도:O(n)
        for i in range(1,len(data)+1):
            self.update(i, data[i-1])   #구축: O(nlogn)

    def prefix_sum(self, i):    #누적 합. index가 0이될떄까지 LSB를 계속 뺌 (log n)
        result = 0
        while i > 0:
            result += self.tree[i]
            i -= (i & -i)
        return result

    def update(self, i,dif):    #index<n 까지 index에 LSB를 계속 더함 (log n)
        while i <= len(self.tree)-1:
            self.tree[i] += dif
            i += (i & -i)

    def interval_sum(self,start, end):#Query : O(2log n)
        return self.prefix_sum(end) - self.prefix_sum(start - 1)

    
def test(data):
    tmp = penwickTree(data)
    # tmp.update(3,2)
    # return tmp.tree
    # return tmp.interval_sum(1,16)
    return tmp.tree

print(test([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]))