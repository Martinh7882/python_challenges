
# https://www.reddit.com/r/dailyprogrammer/comments/pih8x/easy_challenge_1/

"""
create a program that will ask the users name, age, and reddit username. have it tell them the information back, in the format:
your name is (blank), you are (blank) years old, and your username is (blank)
for extra credit, have the program log this information in a file to be accessed later.
"""

name = input("What Is Your Name?")
age = input("What Is Your Age?")
redditusername = input("What Is Your Username?")
c_info = [name, age, redditusername]
f = open("cinfo.txt", 'w')

for i in c_info:
    f.write(i + '\n')
f.close()



print("Your Name Is {}, You Are {} Years Old, & Your Username is {}".format(name, age, redditusername))
