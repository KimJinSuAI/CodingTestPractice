from collections import Counter
import re
def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    S1=[]
    S2=[]
    for i in range(len(str1)-1):
        tmp = str1[i:i+2]
        if re.match("[a-z][a-z]",tmp):
            S1.append(tmp)
    for j in range(len(str2)-1):
        tmp = str2[j:j+2]
        if re.match("[a-z][a-z]",tmp):
            S2.append(tmp)
    if S1==[] and S2==[]:
        return 65536
    S1 = Counter(S1)
    S2 = Counter(S2)
    intersection = (S1&S2)
    union = (S1+(S2-S1))
    return int((sum(intersection.values())/sum(union.values()))*65536)

# print(solution("FRANCE","french"), 16384)
# print(solution("handshake","shake hands"), 65536)
# print(solution(	"aa1+aa2", "AAAA12"), 43690)
print(solution(	"E=M*C^2", "e=m*c^2"))