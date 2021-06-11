def say_hello(name1, name2):
    print("Hello, " + name1 + " welcome " + name2 + " is waiting for you!")
say_hello("Ester", "David")


def fahr2celsius(fahr):
    celsius = (5 * (fahr - 32)) / 9
    return celsius

print("Celsius", round (fahr2celsius(100),2) )
print("Kelvin", round (fahr2celsius(100) + 237.5 ,2) )