def solution(n, k, cmd):
    process = ["O" for _ in range(n)]
    stck = []
    for c in cmd:
        if c[0]=="U":
            x = 0
            tmp = int(c[2:])
            flag = False
            for a in sorted(stck, reverse=True):
                if k-tmp<=a<k:
                    if not flag:
                        flag = True
                    tmp+=1
                else:
                    if flag:
                        break
            k-=tmp
        elif c[0]=="D":
            x = 0
            tmp = int(c[2:])
            flag = False
            for a in sorted(stck):
                if k<a<=k+tmp:
                    if not flag:
                        flag = True
                    tmp+=1
                else:
                    if flag:
                        break
            
            k+=tmp

        elif c=="C":
            tmp = k
            stck.append(k)
            process[k]="X"
            while process[k]=="X":
                k +=1
                if k==n:
                    k = tmp-1
                    while process[k]=="X":
                        k-=1
        else:
            process[stck.pop()] = "O"

    return ''.join(process)

print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(	8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
print(solution(8,2,["C","C","C","C","U 1"]))