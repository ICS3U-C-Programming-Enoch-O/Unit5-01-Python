#!/usr/bin/env python3
# Created by: Enoch O
# Created on: April 22, 2025
# #This function takes a temperature in Celsius as input from the user
# converts it to Fahrenheit, and displays the result.


def fahrenheit():

    try:
        # Get the temperature in Celsius from the user.
        celsius = float(input("Enter temperature: "))

        # Calculate the temperature in Fahrenheit using the formula.
        fahrenheit = (9 / 5) * celsius + 32

        # Display the result to the user, formatted to two decimal places.
        print(
            f"{celsius:.2f} degrees Celsius is equal to {fahrenheit:.2f} degrees Fahrenheit."
        )

    except ValueError:

        print("Invalid input. Please enter a number for temperature.")


def main():

    # This is the main function that calls the fahrenheit() function.

    fahrenheit()  # Calling the function


if __name__ == "__main__":
    main()
