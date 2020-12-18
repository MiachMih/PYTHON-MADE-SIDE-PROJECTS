# calculates e^x
from factorial import fact

# calculating natural number using infinite series
# a - order of infinite sum
# b - decimal place rounding
def e(a=13, b=9):
    e = 0
    for x in range(a):
        try:
            e += 1/fact(x)
        except RecursionError:
            print('fact Error: the value for n was too great.')
    return round(e, b)