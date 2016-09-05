# https://www.reddit.com/r/dailyprogrammer/comments/pjbj8/easy_challenge_2/

"""Challenge 2: Create a calculator application that is a F = M * A calculator.
EXTRA CREDIT: It should be able to not only calculate F = M * A, but also A = F/M, and M = F/A!"""


def forcecalc(f: int = 0, m: int = 0, a: int = 0):
    if f == 0:
        return m * a
    elif m == 0:
        return f / a
    else:
        return f / m


force = 0
mass = 0
acc = 0

question = input("What do you want to solve for?")
ans = ['force', 'mass', 'acc']

while question not in ans:
    question = input('You can only use "force", "mass", & "acc"')

if question == "force":
    while mass == 0 or acc == 0:
        try:
            acc = int(input("How much acceleration?"))
            mass = int(input("How much mass?"))
        except ValueError:
            print("You can only input numbers")
            acc = 0
            mass = 0
elif question == "mass":
    while force == 0 or acc == 0:
        try:
            force = int(input("How much force?"))
            acc = int(input("How much acceleration?"))
        except ValueError:
            print("You can only input numbers")
            force = 0
            acc = 0
else:
    while mass == 0 or force == 0:
        try:
            mass = int(input("How much mass?"))
            force = int(input("How much force?"))
        except ValueError:
            print("You can only input numbers")
            mass = 0
            force = 0

answer = forcecalc(force, mass, acc)

print("""Your answer is:""")
print(answer)

