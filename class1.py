def hello():
    name=input('What is your name?:')
    return 'Hello {}'.format(name)
print(hello())

def old():
    age=int(input('\nWhat year were you born?:'))
    return 'Your {} years old'.format(2019-age)
print(old())

def around():
    ar=input('\nWhat city(Taraz,Almaty,Shymkent,Kyzylorda) do you live in?')
    if ar=='Taraz':
        print('Zhambyl oblysynansyn')
    if ar=='Almaty':
        print('Almaty kalasynansyn')
    if ar=='Shymkent':
        print('Shymkent kalasynansyn')
    if ar=='Kyzylorda':
        print('Kyzylorda oblysynansyn')
around()