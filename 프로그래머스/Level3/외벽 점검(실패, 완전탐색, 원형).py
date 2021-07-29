#완전탐색인지 판단하려면 제한사항의 변수범위가 크지않아야함
#완전탐색은 가능한 변수들을 모두 찾아야함
#1. 시작지점어디? -> 모든 지점시작 후 삭제안된 지점부터..
#2. 어떤친구로 결함찾을까? -> 모든 친구순열에서 구함
#3. 시계방향? 반시계방향? -> ****원형을 직선으로 만듦. 기존 배열*2****
#ex) n==12일 때, 1(13)->10 == 10->1(13)

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
print(solution(12, [1, 5, 6, 10], [1, 4]))
# print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
# print(solution(12,[10,0],[1,2]))