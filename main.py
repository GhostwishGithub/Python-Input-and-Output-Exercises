# Continuing my practice with python
# #Exercise 1: Accept numbers from a user
# #Write a program to accept two numbers from the user and calculate multiplication
# #Basic stuff, input and what not.
# #Two numbers, so, two declarations
# num1 = int(input("Input the first number: "))
# num2 = int(input("Input the second number: "))
# #then multiply them together
# res = num1 * num2
# print("The multiplication is", res)
# Commented out exercise 1 for expediency

#Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”
#Use the print() function to format the given words in the mentioned format. Display the ** separator between each string.
#I honestly had to look at the solution for this. I'd never seen the sep function before. Neat new trick learned!
print('My', 'Name', 'Is', 'James', sep='**')

#Exercise 3: Convert Decimal number to octal using print() output formatting
# Now this is interesting. I'm not even sure what they're talking about. What's an octal? I had to use the solution as I had no idea what they were on about.
num = 8
print('%o' % num)

#Exercise 4: Display float number with 2 decimal places using print()
#All this math is rather.. uninteresting. What real world applications does it server?
num = 458.541315
print('%.2f' % num)

# #Exercise 5: Accept a list of 5 float numbers as an input from the user
# #Well that's back to basic simple. Loop, with float values and input. then stick em in a list and spit it back out
# results = []
# for x in range(1, 6):
#     print("Enter the number for space", x, ":")
#     userInput = float(input())
#     results.append(userInput)

# print("Here's the results:", results)
#Commented out for expediency's sake

#Exercise 6: Write all content of a given file into a new file by skipping line number 5
#Ohhhh. We never really got into this in devCodeCamp. I was very disappointed. This'll be interesting.
#So Python has a built in function called readlines() that accesses files. neat!
#Okay, made the test file, let's do this.
#Okay, so, to read this, you can use something called 'with open'. Which uses r as read and w as write. x is just a target variable.
# with open("test.txt", "r") as x:
#     lines = x.readlines()
# #Now, to make a new file and basically walk through test.txt in making it.
# with open("new.txt", "w") as x:
#     count = 0
#     for line in lines:
#         if count == 4:
#             count += 1
#             continue
#         else:
#             x.write(line)
#             count += 1
#             # Success! Now commenting out to keep it from making new files everytime lol.

#Exercise 7: Accept any three string from one input() call
#Write a program to take three names as input from a user in the single input() function call.
#The hint gives it away. You use the split function to control the input.
# str1, str2, str3 = input("Enter the three names, each seperated by a space:").split()
# print("Name 1 is:", str1)
# print("Name 2 is:", str2)
# print("Name 3 is:", str3)
#Commented out for expediency.

#Exercise 8: Format Variables using a string.format() method.
#So I was thinking they really should have included a hint with this one, but in review, I suppose that hint would have just been "google string.format()" because that function in 
#itself has a lot of strange variables that you can use.
totalMoney = 1000
quantity = 3
price = 450
#This is the part where a bit of googling helped: ':' says Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers) the . gets thrown in between the f, which sets a Fix point number format
answer = "I have {1} dollars so I can buy {0} football tickets for {2:.2f} dollars."
print(answer.format(quantity, totalMoney, price))

#Exercise 9: Check file is empty or not
#Okay! This'll tie in nicely with #6!
#Via the hint, there's a useful function: os.stat('file_name').st_size(). Let's try it out with an if/else statement
#it does require us to import os however.
import os
check = os.stat("test.txt").st_size
if check == 0:
    print("The file is empty.")
else:
    print("The file is NOT empty!")

#Exercise 10: Read line number 4 from the following file
#A bit of a refinement of #6. Easy enough?
# read file
with open("test.txt", "r") as fp:
    # read all lines from a file
    lines = fp.readlines()
    # get line number 4
    print(lines[3])

    #and they are all complete. I am exhausted today so I'll move onto the next exercise tomorrow.