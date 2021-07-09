def solution(array, commands):
    return list( map( lambda x:sorted( array[x[0]-1:x[1]] )[x[2]-1], commands ) )

    # answer = []
    # for i in range(len(commands)):
    #     ans = array[commands[i][0]-1:commands[i][1]]
    #     ans.sort()
    #     answer.append(ans[commands[i][2]-1])
    # return answer

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))