import re
from collections import Counter
from itertools import combinations
def solution(orders, course):
    answer = []
    dic = {}
    for i in range(len(orders)-1):
        for j in range(i+1,len(orders)):
            intersection = ''.join(sorted((Counter(orders[i]) & Counter(orders[j])).keys()))        #교집합은 "ABC..."
            for k in course:
                if k>len(intersection):
                    break
                else:
                    keys = list(map(lambda x: ''.join(x),combinations(intersection, k)))                                      #
                    for l in keys:
                        if l not in dic.keys():
                            for m in orders:
                                for n in l:
                                    if not re.search("["+n+"]",m):
                                        break
                                else:
                                    dic[l] = dic.get(l,0)+1

    for c in course:
        max=0
        stck = []
        for key in dic.keys():
            if len(key)==c and dic[key]>=2:
                if dic[key]>max:
                    stck = []
                    stck.append(key)
                    max = dic[key]
                elif dic[key]== max:
                    stck.append(key)
        for s in stck:
            answer.append(s)

    return sorted(answer)








import collections
import itertools

def solution(orders, course):                                                       #다른사람 풀이
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))