from itertools import combinations
def distinctMoves(s, n, x, y):
    # Write your code here
    answer = set()
    rs = []
    ls = []
    needR = 0
    needL = 0
    for i,S in enumerate(s):
        if S=="r":
            rs.append(i)
        else:
            ls.append(i)
    lenr = len(rs)
    lenl = len(ls)
    
    tmp = y-x
    if tmp>0:
        needR = tmp
    else:
        needL = -tmp
    
    while needR<=lenr and needL <= lenl:
        combr = list(combinations(rs,needR))
        combl = list(combinations(ls,needL))

        for r in combr:
            for l in combl:
                tmp = sorted(list(r)+list(l))
                st = ""
                for t in tmp:
                    st+=str(s[t])

                tmp = x
                for i in range(len(st)):
                    if st[i]=="r":
                        tmp+=1
                    else:
                        tmp-=1
                        if tmp<0:
                            break
                else:
                    answer.add(st)


        needR+=1
        needL+=1
    return len(answer)

# print(distinctMoves("rrlrlr",6,1,2))
print(distinctMoves("rrrlrr",7,0,0))
