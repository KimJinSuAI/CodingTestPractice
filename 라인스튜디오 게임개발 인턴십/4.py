from collections import Counter
def solution(source):
    dest = []
    source = Counter(source)
    while True:
        tmp = []
        for i in source.keys():
            if source[i]!=0:
                tmp.append(i)
                source[i]-=1
        if tmp:
            for t in sorted(tmp):
                dest.append(t)   
        else:
            break        
    return ''.join(dest)

print(solution("execute"))