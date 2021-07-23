def dp(sticker):
    dq = {}
    dq[0] = sticker[-1]
    dq[1] = sticker[-2]
    dq[2] = dq[0]+sticker[-3]
    for i in range(3,len(sticker)):
            dq[i] = sticker[-i-1]+max(dq[i-2],dq[i-3])
    return max(dq.values())
def solution(sticker):
    if len(sticker)<=3:
        return max(sticker)
    return max(dp(sticker[:-1]), dp(sticker[1:]))

print(solution([14, 6, 3]))