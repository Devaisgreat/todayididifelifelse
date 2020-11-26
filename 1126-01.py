print("Welcome to the love calculator!!")
name = input("What is your name? ")
another = input("What is their name? ")

name1 = name.lower()
another1 = another.lower()

t = name1.count('t')
r = name1.count('r')
u = name1.count('u')
e = name1.count('e')

l = another1.count('l')
o = another1.count('o')
v = another1.count('v')
e = another1.count('e')

true = t+r+u+e
love = l+o+v+e

if true + love < 10 or true + love > 90:
    true2 = str(true)
    love2 = str(love)
    print(f"Your score is {true}{love}, you go together like coke and mentos.")
elif 40 < (l+o+v+e) + (t+r+u+e) < 50:
    true2 = str(true)
    love2 = str(love)
    print(f"Your score is {true}{love}, you are alright together.")
else:
    true2 = str(true)
    love2 = str(love)
    print(f"Your score is {true}{love}.")

# i did it my own. but something went wrong.
