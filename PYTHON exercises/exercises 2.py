# ask user to input 3 numbers and you have to print average of 3 numbers using string python.
# Bonus : try to take all three space sperated inpuuts in one line.

no1 = input("Enter your 1st number.")
no2 = input("Enter your 2nd number.")
no3 = input("Enter your 3rd number.")
average = int(no1 + no2 + no3)//3
print(f"Your average is {average}")

# Bonus : -----
no1 , no2 , no3 = input("type three nubmers : ").split()
print(f"Your average is {int(no1 + no2 + no3 )/3}")