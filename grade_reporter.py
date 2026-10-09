# Start with the required list of scores
scores = [72, 45, 90, 61, 38]

# Initialize counter variables and running total
passes = 0
fails = 0
total_score = 0

# Loop through each score in the list
for score in scores:
    total_score += score
    
    # Determine letter grade using conditional statements
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"
        
    # Track pass and fail counts
    if score >= 50:
        passes += 1
    else:
        fails += 1
        
    # Print individual score and grade
    print(f"Score: {score} - Grade: {grade}")

# Calculate average score rounded to 1 decimal place
average = round(total_score / len(scores), 1)

# Print summary metrics
print("-" * 25)
print(f"Passed: {passes}")
print(f"Failed: {fails}")
print(f"Average: {average}")