import math

hogsmeade = {"x": 34, "z": 220}
kakariko = {"x": 0, "z": 0}
solitude = {"x": 140, "z": 456}


def getDistance(x1, x2, z1, z2):
    distance = math.sqrt((x1 - x2) ** 2 + (z1 - z2) ** 2)
    return distance


def stringFormater(city, distance):
    return "Distancia para {city}: {distance: .2f}".format(city=city, distance=distance)


x1 = int(input())
z1 = int(input())

print(stringFormater("Hogsmeade", getDistance(x1, hogsmeade["x"], z1, hogsmeade["z"])))
print(stringFormater("Kakariko", getDistance(x1, kakariko["x"], z1, kakariko["z"])))
print(stringFormater("Solitude", getDistance(x1, solitude["x"], z1, solitude["z"])))
