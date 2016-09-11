# """"""print out Happy Birthday the song""""""

name = input("What Is Your Name?")
date = input("What date is your Birthday?")
while date == 0:
    try:
        date = int(input("What date is your Birthday?"))
    except ValueError:
        print("You can only input numbers")
        date = 0
print("Hi! {},".format(name))

bd = input("Is today your Birthday?")

if bd == "y":
            print("DAMN!!! YOU'RE OLD AS HELL!!!"
                  "Here's to you, you old coot!!!"
                  "HAPPY BIRTHDAY TO YOU! "
                  "HAPPY BIRTHDAY TO YOU! "
                  "HAPPY BIRTHDAY DEAR({},".format(name))
            print("HAPPY BIRTHDAY TOOO YOOOOOUUUUU!!!! "
                  "AND MANNYYYYYYY MORRRREEEEEEEEEEE!!!")
else:
            print("Sorry man....Comeback on your birthday for a special surprise")
c_info = [name, date]
f = open("cinfo.txt", 'w')
