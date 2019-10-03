# Exercise 1
print ("Exercise 1")
aircrafts = {
    "x": 567.888,
    "y": 895.11
}
f = open("exercise_1.txt", "w")
f.write("X -" + str(aircrafts["x"]) + ", Y -" + str(aircrafts["y"]))
f.close()

print ("X -", aircrafts["x"], ", Y -", aircrafts["y"])
multipleAircrafts = [{"x": 123.345, "y": 234.567},
                     {"x": 23.345, "y": 24.567},
                     {"x": 13.345, "y": 23.567},
                     {"x": 129.345, "y": 237.567},
                     {"x": 193.345, "y": 239.567},
                     {"x": 123.366, "y": 236.67}]
for aircraft in multipleAircrafts:
    print ("X -", aircraft["x"], ", Y -", aircraft["y"])

# Exercise 2
print ("\n\nExercise 2")


class Aircraft(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.acc = 1

    def moveRight(self):
        self.x += 1

    def moveLeft(self):
        self.x += -1

    def moveUp(self):
        self.y += -1

    def moveDown(self):
        self.y += 1


aircraft = Aircraft()
aircraft.moveDown()
aircraft.moveDown()
aircraft.moveUp()
aircraft.moveLeft()
aircraft.moveLeft()
aircraft.moveRight()
aircraft.moveDown()
aircraft.moveDown()
aircraft.moveUp()
aircraft.moveLeft()
aircraft.moveLeft()
aircraft.moveRight()
print ("Aircraft X -", aircraft.x, ", Y -", aircraft.y)
f = open("exercise_2.txt", "w")
f.write("Aircraft X - " + str(aircraft.x) + ", Y - " + str(aircraft.y))
f.close()
# Exercise 3
print ("\n\nExercise 3")

aircraft1 = Aircraft()
aircraft2 = Aircraft()
aircraft3 = Aircraft()
aircraft4 = Aircraft()
aircraft5 = Aircraft()
for i in range(0, 10):
    aircraft1.moveRight()
    aircraft1.moveRight()
    aircraft1.moveLeft()
    aircraft1.moveUp()
    aircraft1.moveUp()
    aircraft1.moveDown()

    aircraft2.moveRight()
    aircraft2.moveRight()
    aircraft2.moveUp()
    aircraft2.moveUp()

    aircraft3.moveRight()
    aircraft3.moveLeft()
    aircraft3.moveUp()
    aircraft3.moveUp()
    aircraft3.moveDown()

    aircraft1.moveRight()
    aircraft1.moveRight()
    aircraft1.moveLeft()
    aircraft1.moveUp()
    aircraft1.moveDown()

    aircraft4.moveRight()
    aircraft4.moveLeft()
    aircraft4.moveDown()
    aircraft4.moveDown()

    aircraft5.moveLeft()
    aircraft5.moveLeft()
    aircraft5.moveUp()
    aircraft5.moveUp()
    aircraft5.moveDown()
    aircraft5.moveDown()
    aircraft5.moveDown()
print ("Aircraft1 X -", aircraft1.x, ", Y -", aircraft1.y)
print ("Aircraft2 X -", aircraft2.x, ", Y -", aircraft2.y)
print ("Aircraft3 X -", aircraft3.x, ", Y -", aircraft3.y)
print ("Aircraft4 X -", aircraft4.x, ", Y -", aircraft4.y)
print ("Aircraft5 X -", aircraft5.x, ", Y -", aircraft5.y)
f = open("exercise_3.txt", "w")
f.write("Aircraft X - " + str(aircraft1.x) + ", Y - " + str(aircraft1.y))
f.write("\nAircraft X - " + str(aircraft2.x) + ", Y - " + str(aircraft2.y))
f.write("\nAircraft X - " + str(aircraft3.x) + ", Y - " + str(aircraft3.y))
f.write("\nAircraft X - " + str(aircraft4.x) + ", Y - " + str(aircraft4.y))
f.write("\nAircraft X - " + str(aircraft5.x) + ", Y - " + str(aircraft5.y))
f.close()

# Exercise 4
print ("\n\nExercise 4")


class AircraftNew(object):
    def __init__(self, x=0, y=0, acc=1):
        self.x = x
        self.y = y
        self._acc = acc

    def moveRight(self):
        self.x += 1

    def moveLeft(self):
        self.x += -1

    def moveUp(self):
        self.y += -1

    def moveDown(self):
        self.y += 1


aircraftNew = AircraftNew()
aircraftNew1 = AircraftNew(9, 9)
f = open("exercise_4.txt", "w")
f.write("Aircraft X - " + str(aircraftNew.x) + ", Y - " + str(aircraftNew.y))
f.write("Aircraft X - " + str(aircraftNew1.x) + ", Y - " + str(aircraftNew1.y))
f.close()
print ("AircraftNew X -", aircraftNew.x, ", Y -", aircraftNew.y)
print ("AircraftNew1 X -", aircraftNew1.x, ", Y -", aircraftNew1.y)

# Exercise 5
print ("\n\nExercise 5")

import numpy


class Boeing_747(AircraftNew):  # inherits class AircraftNew
    def __init__(self, xOrg=0, yOrg=0, xDes=0, yDes=0, acc=1):
        self.xOrg = xOrg
        self.yOrg = yOrg
        self.xDes = xDes
        self.yDes = yDes

    def printValues(self):
        f = open("exercise_5.txt", "w")
        f.write("Starting Point(" + str(self.xOrg) + "," + str(self.yOrg)+ ")")
        f.write("\nEnding Point(" + str(self.xDes) + "," + str(self.yDes)+ ")")
        f.close()
        print ("Starting Point(", self.xOrg, ",", self.yOrg, ")")
        print ("Ending Point(", self.xDes, ",", self.yDes, ")")


Boeing_747_obj = Boeing_747(numpy.random.randint(2, 100), numpy.random.randint(2, 100),
                            numpy.random.randint(2, 100), numpy.random.randint(2, 100))
Boeing_747_obj.printValues()
# Exercise 6
print ("\n\nExercise 6")


class Aircraft_Aircraft(object):
    def __init__(self, xOrg=0, yOrg=0, xDes=0, yDes=0, acc=1):
        self.xOrg = xOrg
        self.yOrg = yOrg
        self.xDes = xDes
        self.yDes = yDes
        self.slope = 0
        self.path = []
        self.b = 0
        self.calculateSlope()
        self.calculateB()
        self.calculatePath()

    def calculateSlope(self):
        self.slope = ((self.yOrg - self.yDes) / (self.xOrg - self.xDes))

    def calculateB(self):
        self.b = self.yOrg - (self.slope * self.xOrg)

    def calculatePath(self):
        path = []
        rangeOfX = []
        if self.xOrg < self.xDes:
            rangeOfX = range(self.xOrg + 1, self.xDes + 1)
        else:
            rangeOfX = range(self.xOrg + 1, self.xDes + 1, -1)
        for x in rangeOfX:
            y = (self.slope * x) + self.b
            path.append((x, y))
        self.path = path

    def printValues(self):
        print ("Starting Point(", self.xOrg, ",", self.yOrg, ")")
        print ("Ending Point(", self.xDes, ",", self.yDes, ")")
        print ("Slope", self.slope)
        print ("b", self.b)
        print ("Equation(y= mx +b ) - y =", self.slope, "x +", self.b)
        f = open("exercise_6.txt", "w")
        f.write("Starting Point(" + str(self.xOrg) + "," + str(self.yOrg)+ ")")
        f.write("\nEnding Point(" + str(self.xDes) + "," + str(self.yDes)+ ")")
        f.write("\nSlope"+ str(self.slope))
        f.write("\nb"+ str(self.b))
        f.write("\nEquation(y= mx +b ) - y = "+str(self.slope)+"x + "+str(self.b))
        f.close()
    def printPath(self):
        f = open("exercise_6.txt", "a")
        for i in self.path:
            print ("Accelerating-", i)
            f.write("\nAccelerating -" + str(i) )
        f.write("We have arrived")
        print ("We have arrived")
        f.close()


a = Aircraft_Aircraft(12, 10, 17, 80)
a.printValues()
a.printPath()
