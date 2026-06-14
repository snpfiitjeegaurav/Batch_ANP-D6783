# Problem Statement: Area of a Triangle Using Three Sides with Exception Handling 
# Design a Python program to calculate the area of a triangle using Heron's Formula. The program should 
# accept the lengths of the three sides of the triangle from the user and display the calculated area. 
# However, the program must handle the following exceptional situations gracefully: 
# 1. If the user enters a non-numeric value instead of a number for any side, display an appropriate error 
# message.  
# 2. If any of the entered side lengths are zero or negative, inform the user that triangle sides must be 
# greater than zero.  
# 3. If the three entered side lengths cannot form a valid triangle according to the Triangle Inequality 
# Theorem, notify the user that the triangle is invalid.  
# 4. Ensure that the program does not terminate abruptly due to invalid input and provides meaningful 
# feedback using exception handling.  
# 5. Display a message indicating that the triangle area calculation process has been completed, 
# regardless of whether the calculation was successful or an exception occurred.  
# Note: Use Heron's Formula to calculate the area of the triangle: 
# �
# �=𝑎+𝑏+𝑐
# 2 
# Area=√𝑠(𝑠−𝑎)(𝑠−𝑏)(𝑠−𝑐) 
 
# Sample Scenario: 
# A construction engineer is using an application to estimate the amount of material required for a triangular 
# plot of land. Incorrect measurements or invalid data entry should not cause the application to crash; 
# instead, it should guide the user by displaying appropriate error messages and allowing them to understand 
# the issue with the provided inputs. 
 

import math

def calculate_triangle_area():
    print("--- Triangle Area Calculator (Heron's Formula) ---")
    
    try:
        # 1. Accept inputs from the user and convert to float
        a = float(input("Enter the length of side a: "))
        b = float(input("Enter the length of side b: "))
        c = float(input("Enter the length of side c: "))
        
        # 2. Check for zero or negative side lengths
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Triangle sides must be greater than zero.")
        
        # 3. Check the Triangle Inequality Theorem
        # The sum of any two sides must be strictly greater than the third side
        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            raise ValueError("The entered side lengths cannot form a valid triangle.")
            
        # 4. Apply Heron's Formula if all validations pass
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        
        print(f"\nSuccess! The calculated area of the triangle is: {area:.2f} square units")

    except ValueError as e:
        # Handles non-numeric inputs (via float casting) and custom validation errors
        if "could not convert string to float" in str(e):
            print("\nError: Please enter appropriate numeric values. Text or special characters are not allowed.")
        else:
            print(f"\nError: {e}")
            
    except Exception as e:
        # Catch-all for any other unexpected runtime anomalies
        print(f"\nAn unexpected system error occurred: {e}")
        
    finally:
        # 5. This block always runs, satisfying the requirement to show process completion
        print("Triangle area calculation process has been completed.")

# Run the program
calculate_triangle_area()