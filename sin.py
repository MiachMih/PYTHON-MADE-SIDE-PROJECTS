from factorial import fact
# x is in radians
def TaylorSeries(x, n=0):
    sin = 0
    n=n
    if n < 0 or type(n) != int:
        return "n must be a non-negative integer"
    
    while n >= 0:
        sin += pow(-1,n)*pow(x,2*n+1)/fact(2*n+1)
        n -=1
    return sin