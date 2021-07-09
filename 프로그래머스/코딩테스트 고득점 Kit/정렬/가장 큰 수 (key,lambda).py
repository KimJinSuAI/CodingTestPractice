def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return ''.join(numbers)
# def solution(numbers):
#     answer = ""
#     number = list(map(lambda x:str(x), numbers))
#     for i in range(len(numbers)):
#         max = number[0]
#         for j in range(1,len(number)):
#             l=-1
#             for k in range(len(number[j])):
#                 l+=1
#                 if number[j][k]>max[l]:
#                     max = number[j]
#                     break
#                 elif number[j][k]<max[l]:
#                     break
#                 else:
#                     if k==len(number[j])-1 and l==len(max)-1:
#                         if k<l:
#                             max = number[j]
#                         break
#                     elif k==len(number[j])-1:
#                         k=-1
#                     elif l==len(max)-1:
#                         l=-1
#         answer +=max
#         number.remove(max)

#     return answer
def solution2(numbers):    
    numbers = sorted(list(map(str,numbers)), reverse=True, key=lambda x:x*3)
    return str(int(''.join(numbers)))
    
print(solution2([0,0]))