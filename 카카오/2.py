import math
n_dic = {
    0: '0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'A'
}
def _10toN(num, n):

    result = ''
    q, r = divmod(num, n)

    while q > 0:
        result = n_dic[r] + result
        q, r = divmod(q,n)
    return n_dic[r]+result

def solution(n, k):
    n = _10toN(n,k)
    answer = 0

    #P
    if n.find("0")==-1:
        n = int(n)
        for k in range(2, int(math.sqrt(n))+1): #소수인지 검사
            if n%k==0:
                return 0
        return 1

    start = 0
    for end in range(len(n)):
        if n[end]=="0":
            now = int(n[start:end])
            if now>1:
                for k in range(2,int(math.sqrt(now))+1): #소수인지 검사
                    if int(now)%k==0:
                        break
                else:
                    answer+=1
            start = end

    now = int(n[start:])
    if now>1:
        for k in range(2,int(math.sqrt(now))+1): #소수인지 검사
            if int(now)%k==0:
                break
        else:
            answer+=1
    return answer

# print(solution(437674,3))
# print(solution(110011,10))
print(solution(16,9))