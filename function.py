def hello():
    print("Hello World!")

hello()

def sum(num1=0, num2=0):
    if (type(num1) != int or type(num2) != int):
        return 0
    return num1 + num2

total = sum()
print (total)

def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("Dave", "John", "Sara")

def mult_named_items(**kwargs):
    print (kwargs)
    print(type(kwargs))

mult_named_items(first = "dave", last = "Gray")