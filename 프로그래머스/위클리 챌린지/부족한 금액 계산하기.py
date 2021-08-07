def solution(price, money, count):
    return price*count*(count+1)/2-money

print(solution(2500,1000000000,2500))