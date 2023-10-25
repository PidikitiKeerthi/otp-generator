import random
generateotp = random.randint(000000,1000000)
username = input("username: ")
print('Hello ',username )
print('Here is your otp for login', generateotp)
password = input("Enter the OTP to login ")
if password == str(generateotp):
    print("Login Success")
else:
    password != str(generateotp)
    print("Wrong Otp")