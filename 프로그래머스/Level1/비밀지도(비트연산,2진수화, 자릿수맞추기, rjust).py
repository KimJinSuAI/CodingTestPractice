def solution(n, arr1, arr2):
    answer = [[' ']*n for _ in range(n)]
    arr1 = [bin(i|j).zfill(n+2) for i,j in zip(arr1,arr2)]
    for i in range(n):
        for j in range(2,n+2):
            if arr1[i][j]=='1':
                answer[i][j-2]='#'
        else:
            arr1[i] = ''.join(answer[i])
    return arr1

def solution(n, arr1, arr2):    #다른사람, rjust
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer

# print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]), ["#####","# # #", "### #", "# ##", "#####"])
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))