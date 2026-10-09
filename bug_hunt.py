count = 1
total = 0

# BUG: Fixed SyntaxError by adding missing colon ':' at the end of the while statement.
# BUG: Fixed Logic Error by changing condition from 'count < 5' to 'count <= 5' so that 5 is included in the loop.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Fixed TypeError by wrapping 'total' with str() to concatenate string with integer.
print("Sum of 1 to 5 is: " + str(total))