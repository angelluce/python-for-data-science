try:
    a / 0
except ArithmeticError:
    print('arithmetic error')
except:
    print("err")