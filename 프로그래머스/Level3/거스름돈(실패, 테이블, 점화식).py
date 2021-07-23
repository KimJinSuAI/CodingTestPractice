#n이 만들어야할 돈, ijk는 오름차순 정렬된 돈일 때 
#arr(n,"ijk") = arr(n, "ij") + arr(n-k, "ijk")

def solution(total, coin):
    arr = [1] + [0]*total
    for c in coin:
        for i in range(c, total+1):
            arr[i] += arr[i-c]
    return arr.pop()

print(solution(11,[1,2,5]), 11)
# def dp(n, money):
#     global memo
#     if len(money)==1:
#         if n%int(money[0])!=0:
#             return 0
#         else:
#             return 1
#     else:
#         key = (n, ''.join(money))       #n
#         x = memo.get(key,-1)
#         if x!=-1:
#             return x
#         else:
#             maximum = int(money.pop())
#             if maximum%int(money[-1])==0:
#                 memo[key] = n//maximum+1
#             elif maximum > n:
#                 memo[key] = dp(n,money)
#             else:
#                 sum = 0
#                 tmp = ''.join(money)
#                 for i in range(n//maximum+1):
#                     tmp2 = n-maximum*i
#                     memo[(tmp2,tmp)] = dp(tmp2, money[:])
#                     sum += memo[(tmp2,tmp)]
#                 memo[key] = sum
#         return memo[key]

# def solution(n, money):
#     global memo
#     money.sort()
#     money = list(map(str, money))
#     memo = {}
#     tmp = dp(n,money)
#     return tmp

# print(solution(5, [1,2,5]))
# print(solution(1111,[1,10,100]))