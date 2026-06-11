Import hashlib
Import getpass
Def hash_password(password):
    Return hashlib.sha256(password.encode()).hexdigest()

Users = (“user1”: hash_password(“password1”), “user2”: hash_password(“password2”))
Def login():
    Username = input (“Enter your username: ”)
    Password = getpass.getpass(“Enter your password: ”)
       
   If username in users and users(username) == hash_password(password):
      Print(“Login Sucessful!”)
      Return True
    else:
        print(“Invalid creditials“)
        return False       
