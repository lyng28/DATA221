# Controlled Multiplication Loop
threshold = 100
product = 1
currentNumber = 1

# Increase currentNumber first then multiply
# So that when the loop stops, currentNumber is the integer that caused the product exceeds threshold

while product <= threshold:
    currentNumber += 1
    product *= currentNumber

print("Final product is: ", product)
print("The integer that caused the product exceeds threshold is: ", currentNumber)