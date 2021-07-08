import math

# Point class
class Point:

    def __init__(self):
        self.x = 0
        self.y = 0

        # returns the distance between two provided points.
    def distance(self, point):
        d = math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)
        return d

    def move(self, i):

        # if the iteration is the 3rd a back step is taken.
        if i % 3 == 0:
            self.x -= backStep
            self.y -= backStep
            print('back to ', self.x)
            i += 1
            return i
        # else the forward steps are taken.
        else:
            self.x += step1
            self.y += step2
            print('Move to: ', self.x)
            i += 1
            return i


# Main program

start_current = Point()
temp = Point()

# Read in x and y for Point P
p = Point()
p.x = int(input())
p.y = int(input())

# Read in num of steps to be taken in X and Y directions
step1 = int(input())
step2 = int(input())

# Read in num of steps to be taken (backwards) every 3 steps
backStep = int(input())
iteration = 0 # iteration counter starts with the first iteration
# Write dynamic programming algorithm


temp.move(1)
while p.distance(start_current) > p.distance(temp):
    start_current = temp
    iteration += 1
    print(iteration)
    temp.move(iteration)
    if iteration + 1 %3 == 0:
        iteration += 1



# else return start_current


# Output
print('P: (', p.x, ',', p.y, ')')
print('Arrival point: (', start_current.x, ',', start_current.y, ')')
print('Distance between P and arrival: ', p.distance(start_current))
print('Number of iterations: ', iteration)


# Testing area

