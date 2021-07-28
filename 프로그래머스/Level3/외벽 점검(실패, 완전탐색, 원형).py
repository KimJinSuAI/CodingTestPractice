from itertools import permutations
def solution(n, weak, dist):
    dist = sorted(dist) #오름차순으로 주어지는건가?
    weak += list(map(lambda x: x+n, weak))
    dist_list = list(map(list,permutations(dist,len(dist))))
    answer = []
    for d in dist_list:
        for i in range(len(weak)//2):      #시작지점==weak[i]
            dCopy = d[:]
            weakCopy = weak[i:i+len(weak)//2]
            count = 0
            while weakCopy:                #모든 weak제거해야함
                start = weakCopy[0]
                if not dCopy:
                    break
                crew = dCopy.pop()
                count+=1
                while weakCopy and start<=weakCopy[0]<=start+crew:
                    weakCopy.pop(0)
            else:
                answer.append(count)
    if not answer:
        return -1
    else:
        return min(answer)
# print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
# print(solution(12,[10,0],[1,2]))