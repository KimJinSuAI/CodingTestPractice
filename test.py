import sys
class PSum:
    def __init__(self, data):
        self.data = [[0]*(len(data[0])+1) for _ in range(len(data)+1)]
        for y in range (1,len(data)+1):
            for x in range (1,len(data[0])+1):
                self.data[y][x] = self.data[y-1][x]+self.data[y][x-1]-self.data[y-1][x-1]+data[y-1][x-1]

    def query(self, sy,sx, ey, ex):
        return self.data[ey][ex]-self.data[sy-1][ex]-self.data[ey][sx-1]+self.data[sy-1][sx-1]

N = int(sys.stdin.readline())
data = []
for i in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))
data = PSum(data)
print(data.data)
print()
print(data.query(3,3,5,5))
