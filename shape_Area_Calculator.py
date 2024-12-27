#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Area Calculator
#This program calculates the are for a given shape

print("===================")
print("  Area Calculator  ")
print("===================")
print("\n")
print("1) Triangle")
print("2) Rectangle")
print("3) Square")
print("4) Circle")
print("5) Quit")
print("\n")

#While loop keeps asking what shape to calculate the area until user enters 5
menu_option = input ("Which shape: ")
while True:
    # If menu option is 5, then end the program
    if menu_option == '5':
        print("Goodbye!")
        break
        
    # 1) Calculate area of Triangle
    elif menu_option == '1':
        height = float(input("Enter height of triangle: "))
        base = float(input("Enter base of triangle: "))
        # area = (height * base) / 2
        triangle_area = (1/2) * (base * height)
        print("The area of the Triangle is: ", triangle_area)

    # 2) Calculate area of Rectangle
    elif menu_option == '2':
        length = float(input("Enter length of rectangle: "))
        width = float(input("Enter width of rectangle: "))
        # area = length x width
        rectangle_area = length * width
        print("The area of the Rectangle is: ", rectangle_area)
        
    # 3) Calculate area of Square
    elif menu_option == '3':
        side = float(input("Enter side length of square: "))
        # area = side^2
        square_area = side ** 2
        print("The area of the Square is: ", square_area)
        
    # 4) Calculate area of Circle
    elif menu_option == '4':
        PI = 3.14159 #The constant Pi
        radius = float(input("Enter radius of the circle: "))
        #area = Pi * r^2
        circle_area = PI * (radius ** 2)
        print("The area of the Circle is: ", circle_area)
        
    # Keeps asking user for a shape to calculate its area
    # until number 5 in which the while loop is exited 
    menu_option = input ("Which shape: ")
    

