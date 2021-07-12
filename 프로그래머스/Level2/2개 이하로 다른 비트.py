def solution(numbers):
    answer = []
    for number in numbers:
        tmp = number+1
        tmpbin = bin(tmp)[2:]
        numbin = bin(number)[2:].zfill(len(tmpbin))
        count = 0
        for bit in range(len(numbin)-1,-1,-1):
            if tmpbin[bit]!=numbin[bit]:
                count+=1
                if count>2:
                    break
        else:
            answer.append(tmp)
        if count>2:
            for bit2 in range(len(numbin)-1,-1,-1):
                if numbin[bit2]=="0":
                    answer.append(int("0b"+numbin[:bit2]+"10"+numbin[bit2+2:],2))
                    break
                    
                    
        
    return answer

print(solution([2,7]))