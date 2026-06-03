correct_username = 'Admin'
correct_password = 'password'
username = input("Enter a username:")
password = input("Enter a password:")
if username == correct_username and password == correct_password:
    print("Login successfull")
else:
    print("Invalid username and password")
