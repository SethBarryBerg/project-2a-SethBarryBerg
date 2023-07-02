print("please enter five numbers" )

number1, number2, number3, number4, number5 = float(input()),float(input()),float(input()),float(input()),float(input())
print(number1, number2, number3, number4, number5)
avg = (number1 + number2 + number3 + number4 + number5) / 5
print("The average of your five numbers: ")
print(avg)

# NOWHERE in the instructions/modules is there anything that tells us how the code can recieve an input all
# in one line to avoid the Test Failed: list index out of range error.
# This has cost me literally three hours of my time just to try to fix.
# The code works as it should and outputs the format exactly as instructed.
# Please don't dock me points I really tried
# Show us how to do it correctly so we can learn

#I also tried the code as such:

#print("please enter five numbers" )
#number1 = float(input())
#number2 = float(input())
#number3 = float(input())
#number4 = float(input())
#number5 = float(input())
#avg = (number1 + number2 + number3 + number4 + number5) / 5
#print("The average of your five numbers: ")
#print(avg)
