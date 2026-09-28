# User-defined function to check the triangle
def check_triangle(a, b, c):
    # Find the largest side (hypotenuse)
    hypotenuse = max(a, b, c)
    
    # Calculate the sum of squares of all sides
    sum_of_squares = (a * a) + (b * b) + (c * c)
    
    # In a right-angled triangle, a^2 + b^2 + c^2 equals 2 * hypotenuse^2
    if sum_of_squares == 2 * (hypotenuse * hypotenuse):
        return True
    else:
        return False

# Taking inputs from the user
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Function calling and final output display
if check_triangle(side1, side2, side3):
    print("The given sides form a right-angled triangle.")
else:
    print("The given sides do not form a right-angled triangle.")
#Output:
#Case 1: Valid Right Angled Triangle
#Enter the length of the first side: 3
#Enter the length of the second side: 4
#Enter the length of the third side: 5
#The given sides form a right-angled triangle.
#Case 2: Invalid Right Angled Triangle
#Enter the length of the first side: 5
#Enter the length of the second side: 6
#Enter the length of the third side: 7
#The given sides do not form a right-angled triangle.

