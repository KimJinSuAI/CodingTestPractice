def f(a,k):
    a = sorted(a, key = lambda x: -x)
    
    if len(a)<k:
        return "Error"
    
    tmp = 0
    for i in range(k):
        tmp+=a[i]
    
    return tmp
    

print(f([1,2,7,4,5], 3))