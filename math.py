def add(x,y):
    return x+y
def subtract(x,y):
    if x<y:
        return ERROR
    return x-y
def mul(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return DIVIDE_BY_0_ERROR
    return x/y

def square(x):
    return x*x
    
#changes for branch