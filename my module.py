def add(num1 : int, num2 : int):
    return num1 + num2
print(add(4,7))

def avg(*numbers): # * is used when you are not sure the lenght of inputs to be taken. it puts parameters into a tuple
    return sum(numbers)/ len(numbers)