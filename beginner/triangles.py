import math

side1 = input("Side 1: ")
side2 = input("Side 2: ")
side3 = input("Side 3: ")

numericalside1 = int(side1)
numericalside2 = int(side2)
numericalside3 = int(side3)

def equilateral(side1, side2, side3):
    if side1==side2==side3:
        check = True
    else: check = False
    return check

def isosceles(numericalside1, numericalside2, numericalside3):
    if numericalside1 == numericalside2 or numericalside2 == numericalside3 or numericalside1 == numericalside3:
        check = True
    else: check = False
    return check
    
def scalene(numericalside1, numericalside2, numericalside3):
    if numericalside1 != numericalside2 != numericalside3:
        check = True
    else: check = False
    return check

def rightangle(numericalside1, numericalside2, numericalside3):
    if numericalside3 == math.sqrt(numericalside1) * 2 + (numericalside2) * 2:
        check = True
    else: check = False
    return check

properties = []

if (numericalside1 + numericalside2 > numericalside3) and (numericalside2 +numericalside3 > numericalside1) and (numericalside3 + numericalside1 > numericalside2):
    checkequilateral = equilateral(numericalside1, numericalside2, numericalside3)
    if checkequilateral == True:
        properties.append("equilateral triangle, ")
    checkisosceles = isosceles(numericalside1, numericalside2, numericalside3)
    if checkisosceles == True:
        properties.append("isosceles triangle, ")
    checkscalene = scalene(numericalside1, numericalside2, numericalside3)
    if checkscalene == True:
        properties.append("scalene triangle, ")
    checkright = rightangle(numericalside1, numericalside2, numericalside3)
    if checkright == True:
        properties.append("right-angle triangle, 4")
else: print("Not a triangle")

print(*properties)
