# geometry.py
import math

def area_circle(radius):
    return math.pi * radius ** 2

def area_triangle(base, height):
    return 0.5 * base * height

def area_rectangle(length, width):
    return length * width

import geometry

# Area of Circle
r = float(input("Enter radius of the circle: "))
print("Area of Circle:", geometry.area_circle(r))

# Area of Triangle
b = float(input("Enter base of the triangle: "))
h = float(input("Enter height of the triangle: "))
print("Area of Triangle:", geometry.area_triangle(b, h))

# Area of Rectangle
l = float(input("Enter length of the rectangle: "))
w = float(input("Enter width of the rectangle: "))
print("Area of Rectangle:", geometry.area_rectangle(l, w))

