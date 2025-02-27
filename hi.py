def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32  
    return fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")



months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
month_number = int(input("Enter a month number (1-12): "))
if 1 <= month_number <= 12:
 
    print(f"The month is: {months[month_number - 1]}")
else:
    print("Invalid month number! Please enter a number between 1 and 12.") 



number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

    def calculate_interest(principal, rate):
    time = 1 
    return principal * (rate / 100) * time

def main():
    try:
        principal = float(input("Enter the principal amount (in your currency): "))
        rate = float(input("Enter the annual interest rate (in percentage): "))
        
        interest = calculate_interest(principal, rate)
        print(f"The interest earned in a leap year is: {interest:.2f} (in your currency)")
    except ValueError:
        print("Please enter valid numeric values for principal and interest rate.")

if __name__ == "__main__":
    main()
    

    distance = float(input("Enter the distance traveled (in km): "))

if distance < 30:
    fee = 120
elif distance < 80:
    fee = 210
elif distance < 180:
    fee = 260
elif distance < 300:
    fee = 450
else:
    fee = "invalid distance"

print("Fee:", fee)





      
