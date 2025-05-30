# Prompt the user for mass as an integer (in kilograms)
m = int(input("Enter mass in kilograms: "))

# Calculate the Einstein formula (don't forget to convert the input from str to
# int)
c = 300000000
answer = (m * c * c)

# Print the result
print (answer)
