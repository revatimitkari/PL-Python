substring=input("enter the secret message(substring):")
string=input("enter the coded message(string):")
if substring in string:
    print("secret message found")
else:
    print("secret message not found")
