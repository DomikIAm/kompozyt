def composite_fun(f,g):
    return lambda x: f(g(x))

def add(x):
    return x+2

def multiply(x):
    return x*2

def substract(x):
    return x-1

add_substract_multiply = composite_fun(composite_fun (multiply,substract),add)
print("Dodawanie 2 do 5 odejmowanie 1 i mnozenie przez 2: ", add_substract_multiply(5))