# 1. Define a function message(text="Keep Learning!") and call it with and without an argument.

def message(text = "Keep Learning!"):
    print(text)

message("Learn something new!")
message()

# 2. Create a function login(username, password="Qwe@1234") that prints the credentials.

def login(username, password = "Qwe@1234"):
    print(f"Username: {username}\nPasword: {password}")

login(username = "admin")