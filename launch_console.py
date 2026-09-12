name = input('Welcome to the launch console! What is your name?: ')
 
run = True
while run == True:
    print('1. Aboout me')
    print('2. My goals')
    print('3. My favorite juice')
    print('4. Exit')
    num = input('Hello ' + name + '! Choose a number between 1-4 based on what you would like to know? ')

    if num == '1':
        print('My name is Jeslyn and I am 17 years old.')
    elif num == '2':
        print('I hope to become an electrical engineer')
    elif num == '4':
        print('goodbye!')
        run = False
    elif num == '3':
        print('I like raspberry lemonade!')
    else:
        print('choose a number 1-3')
