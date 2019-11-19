def ask(name='AzatAI'):
    print(name)
    
my_func = ask()
my_func2 = ask # assign the function to a variable.
my_func2('Hello')

def decorator_func():
    print('dec start')
    return ask

my_ask = decorator_func()
my_ask('Tom')

