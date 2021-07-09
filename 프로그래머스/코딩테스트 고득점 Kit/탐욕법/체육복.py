def solution(n, lost, reserve):
    delList = []
    for i in reserve:
        if i in lost:
            lost.remove(i)
            delList.append(i)
    for i in delList:
        reserve.remove(i)

    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)
        
    return n-len(lost)

def solution2(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)
print(solution(5,[2,3,4],[1,2,3]))