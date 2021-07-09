# import pandas as pd
# def solution(clothes):
#     dataFrame = pd.DataFrame(clothes)
#     x = {}
#     answer=1
#     for i in dataFrame[1]:
#         if i not in x:
#             x[i] = 1
#         else:
#             x[i] = x[i]+1
#     for j in x:
#         answer = answer*(x[j]+1)
#     answer = answer-1
    
#     return answer

def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes]) #Counter는 반복가능한 객체의 원소개수를 세기위함. 딕셔너리와 매우 유사함. a:9, b:10,..이런식
                                                    #kind for name은 열추출하는방식임..  익명name데이터 속의 kind 익명데이터
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1 #x는 저장용 익명변수, y는 데이터가 들어갈 익명변수, cnt.values는 카운터의 
    return answer                                              #value리스트, 1은 초기값

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))