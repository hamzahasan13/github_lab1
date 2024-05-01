def fun1(x, y):
    return (x+y)

def fun2(x,y):
    return (x-y)

def fun3(x,y):
    return (x*y)

def fun4(x,y,z):
    
    result_fun4 = x+y+z
    
    return result_fun4

if __name__ == "__main__":
    x = 5
    y = 3;
    
    print("fun1:", fun1(x, y))
    print("fun2:", fun2(x, y))
    print("fun3:", fun3(x, y))
    print("fun4:", fun4(x, y))