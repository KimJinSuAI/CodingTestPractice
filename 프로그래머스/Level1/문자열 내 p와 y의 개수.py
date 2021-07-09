from collections import Counter
def solution(s):
    c=Counter(s)

    return (c['p']+c['P'])==(c['y']+c['Y'])

print(solution("pPoooyY"))
print(solution("Pyy"))