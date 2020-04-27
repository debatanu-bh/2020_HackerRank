def switch_cases(operator,x,y):
    return{

        "add": lambda: x+y,
        "sub": lambda: x-y
    }.get(operator,lambda:None)()

switch_cases(add,2,3)