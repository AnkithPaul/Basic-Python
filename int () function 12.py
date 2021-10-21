no1 = input("enter first number") # 5 
no2 = input("enter second number") # 5
total = no1 + no2 # 55 as input take the value as a string so "5" + "5" = 55
print("total is" + total)

# so to make the answer correct we need to use int (integer) and str(string) command 
no4 = int(input("enter your first number ")) # int is used to make the value an integer
no5 = int(input("enter your second number")) # same with this case# total = no4 + no5 # as no4 and no5 is made integer so the total became integer 
print("total is " + str(total) + ("\U0001F600")) # so we needed to add str inorder to make the total string.

# srt made 4---> "4"
# int made "4"---> 4
#and float is also and command with help to made string to float "4"--->4.0

no6 = str(4)
no7 = int("4") 
no8 = float("4")
print(no6 + no8)

no8 = str(float("4"))# to add str with float but the answer will also come as float
print(no6 + no8) # float!
