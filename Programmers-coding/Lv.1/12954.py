#https://school.programmers.co.kr/learn/courses/30/lessons/12954
#x만큼 간격이 있는 n개의 숫자

def solution(x, n):
    
    if x > 0:
        return [i for i in range(x,x*n+1,x)]
    elif x == 0:
        return [x] * n
    else:
        return [i for i in range(x,x*n-1,x)]
    
    
