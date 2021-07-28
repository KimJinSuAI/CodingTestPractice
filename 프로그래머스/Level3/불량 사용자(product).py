from itertools import product
def solution(user_id, banned_id):
    answer = set()
    banned_list = []
    for banned in banned_id:
        count = []
        for user in user_id:
            if len(user)==len(banned):          #조건 매칭하는지 검사
                for b,u in zip(banned,user):
                    if b=="*":
                        continue
                    elif b!=u:
                        break
                else:
                    count.append(user)          
        banned_list.append(count)               #조건에 맞는 id리스트 추가
    banned_list = list(product(*banned_list))   #모든 리스트의 조합 산출
    for b in banned_list:
        x = set(b)                              #set으로 ID같은것 제거
        if len(x)==len(banned_id):              #제거안한거면 추가
            answer.add("".join(sorted(x)))      #set에 add하기에 순서만 바뀐원소는 제거됨. tuple을 썼었는데 "".join비교가 더 빠른듯..
    return len(answer)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]), 2)
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]), 3)
# print(solution(["abcde", "accde", "adcde", "aecde"],["abcd*","*bcd","*****"]), 4)