'''
Corbin Goodman
Python
Triangle Area
1/8/2020
'''
import math

'''
Parameters are the three sides of the triange
s is the semiperimeter 
takes the sides of the triange and prints the area
'''
def triangeArea(a,b,c):
  s = float((a + b + c)/2)
  area = math.sqrt((s * (s - a)) * (s - b) * (s - c))

  print("Area of the triange: " + str(area))

#checks input to make sure its a positive number and keeps throwing error until user makes it positive
def checkData(a):
  while(a < 0):
    a = float(input("ERROR! Please enter a value over 0: "))

  return a

repeatArea = ""

#keeps calculating triangles until user types "STOP"
while(repeatArea != "STOP"):
  sideA = checkData(float(input("Enter side A: ")))
  sideB = checkData(float(input("Enter side B: ")))
  sideC = checkData(float(input("Enter side C: ")))
  triangeArea(sideA, sideB, sideC)
  repeatArea = (input("\nPress Enter to calculate another triangle, type \"STOP\" to stop: "))
