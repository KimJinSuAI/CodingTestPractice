class prefixSum:
    def __init__(self, data):
        self.data = [[0] * (len(data[0])+1) for _ in range(len(data)+1)]
        for y in range(1,len(self.data)):
            for x in range(1,len(self.data[0])):
                self.data[y][x] = self.data[y-1][x]+self.data[y][x-1]-self.data[y-1][x-1]+data[y-1][x-1]

    def query(self,sy,sx,ey,ex):
        return self.data[ey][ex]-self.data[ey][sx-1]-self.data[sy-1][ex]+self.data[sy-1][sx-1]
def test():
    tmp = prefixSum([[1,2,3],[4,5,6],[7,8,9]])
    return tmp.query(2,2,3,3)

print(test())