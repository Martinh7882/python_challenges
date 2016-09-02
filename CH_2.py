# https://www.reddit.com/r/dailyprogrammer/comments/pjbj8/easy_challenge_2/

"""Challenge 2: Create a calculator application that is a F = M * A calculator.
EXTRA CREDIT: It should be able to not only calculate F = M * A, but also A = F/M, and M = F/A!"""

def forcecalc(f: int=0,m: int=0,a: int=0):
    if f == 0:
        return m*a
    elif m == 0:
        return f/a
    else:
        return f/m

force = 0
mass = 0
acc = 0

while sum([force, mass, acc]) == 0:
    force = int(input("How much force?"))
    acc = int(input("How much acceleration?"))
    mass = int(input("How much mass?"))

answer = forcecalc(force, mass, acc)
print(answer)

