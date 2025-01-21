name = input("What is your name?")
print("hello", name)
age = input("How old are you? ")
try:
    # another way to format print is via f-strings
    print(f"{name}, you were born in {2024-int(age)}")
    # dision = int(age) / 0
except ValueError:
    print("Age must be a valid number")
    print(f"The value that typed was {age}")
except ZeroDivisionError:
    print("You can't divide by zero")
except:
    print("No idea what else can go wrong, but just in case")
else: # in case no exception happened
    print("Thanks for being a good sport and not trying to crash the game")
finally: # this runs in the end no matter what!
    print("Thanks for playing")