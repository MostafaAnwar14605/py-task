'''
def numbers(x,y):
    print(x+y)

numbers(10,25)
numbers(15,20)
'''

'''
def numbers(x,y):
    print(x+y)
numbers(x =5,y =15 )    
'''

'''

def numbers(x=0,y=0):
    print(x,y)
numbers()
'''


'''
def print_sum(*args):
    total_sum = sum (args)
    print("sum of the arguments:",total_sum)
    
print_sum(1,2,3,4,5,6)
'''


'''
def lamda(*args):
    total_sum = sum (args)
    print("sum of the arguments:",total_sum)
    
print(1,2,3,4,5,6)

'''

'''
numbers = lambda*args: sum (args)
print("Sum of the arguments:",numbers(1, 2, 3, 4, 5,6))
'''

'''
print("Sum of the arguments:", (lambda *args: sum(args))(1, 2, 3, 4, 5,6))
'''

