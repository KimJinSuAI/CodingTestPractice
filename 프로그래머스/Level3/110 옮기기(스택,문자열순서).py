def found110(number):#110삭제
    count = 0
    stck = []
    for chr in number:
        if chr=="0" and len(stck)>1:
            if stck[-1]=="1" and stck[-2]=="1":
                count+=1
                stck.pop()
                stck.pop()
            else: stck.append(chr)
        else:
            stck.append(chr)
    return ''.join(stck), count

def insert110(string, count):      #110삽입
    count110 = "110"*count
    try:
        k = string.index("11")
        return string[:k]+count110+string[k:]
    except:
        if len(string)>0:
            if string[-1] =="1":
                return string[:-1]+count110+"1"
            else:
                return string+count110
        else:
            return count110

def solution(s):
    answer = []
    for number in s:
        number, count = found110(number)        
        answer.append(insert110(number,count))
    return answer


    # return stck
# print(solution(["1011110"]))
print(solution(["1110","100111100","0111111010"])==["1101","100110110","0110110111"])
print(solution(["1011110","01110","101101111010"])== ["1011011","01101","101101101101"])
# print(solution(["1011110","01110","101101111010"]))
print (solution(["110"]))