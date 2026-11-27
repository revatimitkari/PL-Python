try:
    earth = 9.8
    moon = 1.6
mass = float(input("enter the mass in kg: "))
    earth_weight = mass * earth
    moon_weight = mass * moon
    print("weight on earth =", earth_weight, "n")
    print("weight on moon =", moon_weight, "n")
except:
    print("please enter a valid number.")
