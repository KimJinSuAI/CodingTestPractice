import sys

def solution(wave1, wave2):
    answer = sys.maxsize
    if len(wave1)!=len(wave2):
        wave1,wave2 = min(wave1,wave2,key= lambda x: len(x)), max(wave1,wave2,key= lambda x: len(x))
    wave2+=wave2*(len(wave1))
    wave2*=2                                #Expand longer wave
    
    for i in range(len(wave1)):             #Delay
        wave1 = [wave1[-1]]+wave1[:-1]
        ll = []
        
        for j in range(len(wave2)):         #Synthesize waves
            tmp = wave1[j%len(wave1)]+wave2[j]
            ll.append(tmp)
            
        for j in range(1,len(ll)//2):       #Find pattern
            now = 0
            tmp = ll[:j]
            while now+len(tmp)<len(ll):
                if tmp==ll[now:now+j]:
                    now+=j
                else:
                    break
            else:
                if len(tmp)==1:
                    return 0
                ans = 0
                for x in tmp:
                    ans+=x**2
                answer= min(answer,ans)
                break

        

    return answer

# print(solution(	[1, 2, 2, 1, 1, 2], [-2, -1]))
# print(solution([2,-1,3],[-1,-1]))
print(solution(	[0, 1, 1, 1, 1, 1], [0, 0, 1, 0, 0, 0]))