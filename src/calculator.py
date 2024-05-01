def func1(x, y):
    return (x+y)

def func2(x,y):
    return (x-y)

def func3(x,y):
    return (x*y)

def func4(x,y):
    
    result_func4 = func1(x,y) + func2(x,y) + func3(x,y)
    
    return result_func4

if __name__ == "__main__":
    x = 5
    y = 3;
    
    print("func1:", func1(x, y))
    print("func2:", func2(x, y))
    print("func3:", func3(x, y))
    print("func4:", func4(x, y))