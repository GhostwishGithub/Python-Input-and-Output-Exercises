#Continuing my practice with python
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