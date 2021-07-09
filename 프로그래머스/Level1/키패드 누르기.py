def solution(numbers, hand):
    left = [3,0]
    right = [3,2]
    number = [[3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    answer=""
    for i in numbers:
        if i in [1,4,7]:
            left = number[i]
            answer+="L"
        elif i in [3,6,9]:
            right = number[i]
            answer+="R"
        else:
            lDst=abs(number[i][0]-left[0])+abs(number[i][1]-left[1])
            rDst=abs(number[i][0]-right[0])+abs(number[i][1]-right[1])
            if lDst==rDst:
                answer+=hand[0].upper()
                if hand=="left":
                    left = number[i]
                else:
                    right = number[i]
            elif lDst<rDst:
                answer+="L"
                left = number[i]
            else:
                answer+="R"
                right = number[i]
    return answer
                
        
# print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))
print(solution(	[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))