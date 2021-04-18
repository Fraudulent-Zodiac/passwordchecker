
password = input ('Enter your password:  ')
passwordConf = input ('Re-enter your password:  ')

if len (password) < 8:
    print ('Your password should have at least 8 characters')

if not any(char.isdigit() for char in password):
    print ('Your password should have at least 1 number')

if not any(char.isupper() for char in password):
    print ('Your password should have at least 1 capital letter')

if not any(char.islower() for char in password):
    print ('Your password should have at least 1 lower case letter')

if password != passwordConf:
    print ('Your passwords should match')


