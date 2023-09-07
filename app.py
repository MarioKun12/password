name = input('Enter your name: ')
password = input('Enter Password: ')
cpass = input('Confirm Password: ')
while password != cpass:
    print('Password doesnt match')
    password = input('Enter Password: ')
    cpass = input('Confirm Password: ')
else:
    print('Name: ',name)
    print('Password: ',password)