def sayGoodbye():
    print('Goodbye!')

sayGoodbye()

fizz = '''Dear Alic,
I will return to Carol's house at the end of the month.
You friend,
Bob'''

print(fizz)

def bacon():
    spam = 99 # creates a local variables named spam
 #   print(spam) # prints 99
    return spam 

spam = 42 # creates a gobal variable named spam
print(spam) # prints 42
bacon() # Calls the bacon() function

print(spam) # prints 42

lettuce = bacon() # assigns the value of bacon() to lettuce; must have a return statement to store a number
print(lettuce) # prints 99

bread = lettuce + 3 # assigns bread as 99 + 3
print(bread) # prints 102

def sayHello(name):
    print('Hello, ' + name + '. Your name has ' + str(len(name)) + ' letters.')

sayHello('Alice')
sayHello('Bob')
spam = 'Carol'
sayHello(spam)