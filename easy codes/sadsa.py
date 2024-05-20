def bye():
    print('bye!')


def greet2(name):
    print(f'How are you, {name}?')


def greet(name):
    print(f'Hello, {name}!')
    greet2(name)
    print('getting ready to say bye')
    bye()


greet('Michael')
