#project 8

# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Get user input in Colab
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

# Check if values are valid
if weight > 0 and height > 0:
    bmi = calculate_bmi(weight, height)

    # Display the BMI result
    print(f"\nYour BMI is: {bmi:.2f}")

    # BMI Categories
    if bmi < 18.5:
        print("Underweight – Thora zyada kha lena!")
    elif 18.5 <= bmi < 24.9:
        print("Normal Weight – Perfect!")
    elif 25 <= bmi < 29.9:
        print("Overweight – Exercise zaroori hai!")
    else:
        print("Obesity – Health ka khayal rakho!")
else:
    print("Please enter a valid weight and height to calculate BMI.")
