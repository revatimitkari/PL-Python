while True:
  password = input("Enter password (or type stop to exit): ")

  if password == "stop":
    break

  if (
      len(password) >= 8
      and any(c.isupper() for c in password)
      and any(c.islower() for c in password)
  ):
    print("Password is Strong")
  else:
    print("Password is Weak")
