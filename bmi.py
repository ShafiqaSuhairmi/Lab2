def calculate_bmi(height, weight):
    # Calculate BMI
    bmi = weight / (height ** 2)  # Corrected the formula to use exponentiation

    # Check BMI and return corresponding values
    if bmi < 18.5:
        return -1  # Underweight
    elif 18.5 <= bmi <= 25.0:
        return 0  # Normal weight
    else:
        return 1  # Overweight

# Example usage
result = calculate_bmi(height=1.73, weight=57)
print("BMI category code:", result)
