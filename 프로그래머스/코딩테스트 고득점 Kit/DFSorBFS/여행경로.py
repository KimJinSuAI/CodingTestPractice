def dfs(start, tickets, route):
    route.append(start)
    if len(tickets)==0: #다돌았다
        return route
    else:               #다못돌았다
        tmp = []
        for i,j in tickets:
            if i == start:
                tmp.append(j)
        if len(tmp)==0: #갈수없다.
            return None
        tmp.sort()

        for i in tmp:
            ticketsCopy = tickets.copy()
            ticketsCopy.remove([start,i])
            a = dfs(i,ticketsCopy, route.copy())
            if a!=None:
                return a
def solution(tickets):
    return dfs("ICN",tickets, [])
    
# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
print(solution([["ICN","B"],["ICN","A"],["B","C"],["C","ICN"]]))