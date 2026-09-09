password = input("Enter password: ")
role = input("Enter role: ")
if password == "python123":
    if role == "admin":
        print("Administrator Access")
    else:
        print("User Access")
else:
    print("Incorrect Password")
