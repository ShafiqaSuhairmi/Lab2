def calculate_bmi(height, weight):
    print("Height=", height)
    print("Weight=", weight)

    # Add code here to calculate BMI
    bmi = weight / (height ** 2)  # Corrected the formula to use exponentiation

    # If-else statement goes here
    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi <= 25.0:
        print("Normal weight")
    else:
        print("Overweight")

    # Add code here to display BMI
    print("BMI=", bmi)

calculate_bmi(weight=57, height=1.73)
