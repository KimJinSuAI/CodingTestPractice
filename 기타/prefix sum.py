class prefixSum:
    def __init__(self, data):
        self.data = [0]
        sum = 0
        for i in range(len(data)):
            sum+=data[i]
            self.data.append(sum)
            
    def query(self, start, end):
        if not self.data:
            return 0
        else:
            return self.data[end]-self.data[start-1]
    # 원래는 end - (start-1)임..
            
def test(data, start, end):
    tmp = prefixSum(data)
    return tmp.query(start, end)


print(test([1,4,3,4,5,6,7,8,9], 1, 1))