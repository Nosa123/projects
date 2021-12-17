x= 5
y= 9

py_operators= {
    "add": "+",
    "substract": "-",
    "multiply": "*",
    "division": "/"
    }

#print(type(py_operators))


def add(i, j):
    return i + j
    
def substract(i, j):
    return i - j
    
def multiply(i, j):
    return i * j

def division(i, j):
    return i / j



#print(py_operators["add"])
user_input= input("Please, type your operation to perform: ").lower()
result= 0
for op in py_operators:
    if op == user_input:
        result= add(x,y)
        print(f"The result of {x} {py_operators[op]} {y} = {result}")
    elif op == user_input:
        result= substract(x,y)
        print(f"The result of {x} {py_operators[op]} {y} = {result}")
    else:
        print(f"In this part of the universal, we do not accept such operation {user_input}")
        break
        
        
  #  print(op)

#result= add(x,y)
#print(f"The result of {x} {py_operators} {y} = {result}")



