import string
tmp = string.digits+string.ascii_lowercase
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]

def solution(n, t, m, p):
    tmp = ""
    i = 0
    answer = ""
    while len(answer)!=t:
        while len(tmp)<m:
            tmp += str(convert(i,n))
            i+=1
        answer += tmp[p-1]
        tmp = tmp[m:]
    return answer.upper()

print(solution(2,4,2,1))
print(solution(16,16,2,1))