#string = collection of characters inside single quotes or double qoutes


no_1 = "ankith"
no_2 = "paul"
no_3 = no_1 + " " + no_2
print(no_3)
# rule1 = a string cant be added to a number
print(no_1 + 3) # we will find an error in it as the string is added tp a no.
print(no_1 + "3") # no error as it is under double quotes
print(no_1 + str(3)) # no error as we use an comand to make the no. a string
print(no_1 * 3) # we can multiply string with number
