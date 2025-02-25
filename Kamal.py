def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index (BMI).

    Parameters:
    weight (float): Weight in kilograms
    height (float): Height in meters

    Returns:
    float: BMI value
    """
    if height <= 0:
        raise ValueError("Height must be greater than zero.")
    if weight <= 0:
        raise ValueError("Weight must be greater than zero.")
    
    bmi = weight / (height ** 2)
    return bmi

def main():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        bmi = calculate_bmi(weight, height)
        print(f"Your BMI is: {bmi:.2f}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()