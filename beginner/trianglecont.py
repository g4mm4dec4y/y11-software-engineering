import math

sidea = int(input("side 1: "))
sideb = int(input("side 2: "))
sidec = int(input("side 3: "))

def angle(sidea, sideb, sidec):
    angleA = math.degrees(math.acos((sideb**2 + sidec**2 - sidea**2) / (2 * sideb * sidec)))
    angleB = math.degrees(math.acos((sideb**2 + sidea**2 - sidec**2) / (2 * sideb * sidea)))
    angleC = 180 - angleA - angleB 
    angleA = round(angleA, 1)
    angleB = round(angleB, 1)
    angleC = round(angleC, 1)

    return angleA, angleB, angleC

if (sidea + sideb > sidec) and (sideb +sidec > sidea) and (sidec + sidea > sideb):
    print(angle(sidea, sideb, sidec))
