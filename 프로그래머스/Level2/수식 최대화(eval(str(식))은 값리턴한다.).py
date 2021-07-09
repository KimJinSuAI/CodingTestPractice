import re
def solution(expression):
    num = re.findall("[0-9]+",expression)
    opr = re.findall("[-+*]", expression)
    expression = []
    stck = []
    for i in range(len(opr)):                                   #연산자와 숫자 구분짓기. ["500","+","300","-","200"....]
        expression.append(num[i])
        expression.append(opr[i])
    expression.append(num[-1])

    op = 0
    expressionTmp = expression
    currentOpr = ["-*+","-+*","+-*","+*-","*-+","*+-"]          #6개 연산우선순위
    oprIndex = 0
    maxResult = 0
    for x in currentOpr:                                        #6개 연산우선순위별 max값 찾기
        while len(expressionTmp)!=1:                            #스택사용
            for i in range(len(expressionTmp)):
                if op!=0:   #0 은 안해야할것.
                    if op=="-":
                        stck.append(int(stck.pop())-int(expressionTmp[i]))
                    elif op=="+":
                        stck.append(int(stck.pop())+int(expressionTmp[i]))
                    else:
                        stck.append(int(stck.pop())*int(expressionTmp[i]))
                    op = 0
                elif expressionTmp[i]==x[oprIndex]:
                    op= x[oprIndex]
                else:
                    stck.append(expressionTmp[i])                    
            expressionTmp = stck
            stck = []
            oprIndex+=1
        maxResult = max(maxResult, abs(int(expressionTmp[0])))
        expressionTmp = expression
        oprIndex = 0   
    return maxResult

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))