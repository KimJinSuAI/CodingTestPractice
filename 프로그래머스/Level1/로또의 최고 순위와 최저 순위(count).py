def solution(lottos, win_nums):
    count = 0
    zero = 0
    for i in lottos:
        if i in win_nums:
            count+=1
            win_nums.remove(i)
        if i == 0:
            zero+=1
    return list(map(lambda x: 6 if x<2 else 7-x ,[count+zero, count]))

def solution2(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)     ##<----------------
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]

print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0],[38, 19, 20, 40, 15, 25]))