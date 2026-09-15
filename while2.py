correctPassword="abcd"
notfound=True
while(notfound):
    passwordIn=input("Enter password:")
    if(passwordIn==correctPassword):
        notfound=False
print("correct password")