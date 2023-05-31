# Compute all powers of 2 up to 10
for i in range(11):
    print("2^{} = {}".format(i, 2**i))

# What does logarithm mean? If you were given log(n) = x, describe in plain English the relationship between n and x
print("If log(n) = x, then n = 10^x. In other words, x is the exponent to which 10 must be raised to get n.")

# How much larger is 2^31 than 2^28?
print("2^31 is 8 times larger than 2^28.")

# How much larger is 1 billion than 1 million?
print("1 billion is 1000 times larger than 1 million.")

# How much larger is log(1 million) than log(1 billion)?
print("log(1 million) is smaller than log(1 billion), since 1 billion is a larger number than 1 million. In fact, log(1 billion) is three times larger than log(1 million).")

# If log(64) = y, write log(128) in terms of y
print("log(128) = log(64*2) = log(64) + log(2) = y + log(2).")

# If log(x) = 128, write 128 in terms of x without using the logarithm
print("x = 10^128.")

# If log(x/y) = 4, write a relationship between x/y without using the logarithm
print("x/y = 10^4.")

# If log(x*y) = 8, write a relationship of x,y without using the logarithm
print("x*y = 10^8.")

# If the x = 2^8. Rewrite x using base 4. If x = 4^y what is y?
print("2^8 in base 4 is 1000. If x = 4^y, then y = log(4,x) = log(2^2,x) = 2*log(2,x) = 2*8 = 16.")
######
import math
y = 5
x = y + math.log(2, 10)

print(x)
#####



for hi in range(5):
  print(hi)
  
print('_' *10)

for lo in range (7, -7, -3):
  print(lo)
  
print('_' *10)

phrase = 'Monty Python'
for letter in phrase:
  print(letter, end='-')
print()

print('END')


def add(x, y):
   return x+ y
   print(' heyyo ' (x, y ))
sum = add(5, 7)

print('=', sum)

#######


#import numpy
#import matplotlib.pyplot

# Load data
#data = numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')
# Make Figure
#fig = matplotlib.pyplot.figure(figsize=(5.0, 7.0))

# Create subplots in 3 rows and 1 column
#axes1 = fig.add_subplot(3, 1, 1)
#axes2 = fig.add_subplot(3, 1, 2)
#axes3 = fig.add_subplot(3, 1, 3)

# Plot and label the average, max, and min of the data
#axes1.set_ylabel('average')
#axes1.plot(data.mean(axis=0))

#axes2.set_ylabel('max')
#axes2.plot(data.max(axis=0))

#axes3.set_ylabel('min')
#axes3.plot(data.min(axis=0))

#fig.tight_layout()

#matplotlib.pyplot.savefig("plot.png")

# Code adapted from Software Carpentry. Check out the full lesson here:
# http://swcarpentry.github.io/python-novice-inflammation/01-numpy.html
########\


#import turtle
#turtle.color('red')

#size = 100
#for i in range(3):
  #turtle.forward(size)
 # turtle.left(120)
###

##import turtle
#turtle.color('red')
#def back(len):
  #turtle.penup()
 # turtle.backward(len)
  ##turtle.pendown()

#def move(len):
 # back(-1 * len)
   
#def triangle(size):
 # for i in range(3):
   # turtle.forward(size)
   # turtle.left(120)
    
#def square(size):
 # for i in range(4):
   # turtle.backward(size)
   # turtle.left(90)
#def polygon(nums,size):
# for i in range(nums):
#  turtle.forward(nums)
#  turtle.left(360 / nums)
#for n in range(3, 10):
 # move(50)
 # square(n , 100 / n)
 # back(50)
 # turtle.right(360 / 7)   for a polygon distribution pattern
#def spiral(len, angle):
#  for i in range(len 5, -5):
#  turtle.forward(i)
#  turtle.right(angle)

#spiral(70, 35)
#move(150)
#turtle.blue
#spiral(100, 90)



#triangle(100)
#back(75)
#triangle(50)
#back(50)
#triangle(25)
#square(125)
#back(100)
#square(25)
#back(25)



#import turtle
#turtle.color('green')
#my_turtle = turtle.Turtle()
#for _ in range(4):
 # my_turtle.forward(100)
  #my_turtle.right(90)
  
#turtle.done()


#Write a function, add, that takes two numbers as parameters and
#returns their sum.
#2. Write a function, multiply, that takes two numbers as parameters
#and returns their product.
#3. Now, test! Write python code that gets two numbers as input from
#the user and prints out their sum and product by calling the two
#functions above. Bonus points for putting this part in a main function


def add(x, y):
  return x +y
x = 5
y = 7
print(add(x, y))


def mult(x, y):
  return x * y
  
x = 7
y = 5
print(mult(x, y))

a = eval(input('enter a number nigga :'))
c = eval(input('enter a number nigga: '))
print('Sum:', add(a, c), 'multiplication:', mult(a, c))





'''
Tour class which is a collection of ordered points.
The functions allow you to insert points in a way that will 
keep the distance of the tour as small as possible.
Each Tour object should be able to print out the points in order, 
count its number of points, compute its total distance, 
and insert a new point using either of the two heuristics. 
The constructor creates an empty tour.
'''



# Hint: You will want to use a classic LinkedList Node to implement the tour.
class Node:
    def __init__(self, point):
        # This node's point 
        self.point = point

        # The next node
        self.next = None 

class Tour:
    # Creates an empty tour
    # Initialize any instance variables you think are needed.
    def __init__(self):   
        self.tour = []

    # Returns string representation of the Tour.
    # Should output a list of all points on the Tour.
    def __str__(self):
        points = [str(point) for point in self.tour]
        return '[' + ', '.join(points) + ']'

    # return the number of points on tour
    # Hint: You should not have to iterate through the entire Tour to get the size.
    def size(self):
        return len(self.tour)



    # Computers and returns the distance of entire tour
    def distance(self):
        total = 0.0
        variable_points = len(self.tour)
        for i in range(variable_points):
          current_point = self.tour[i]
          point_2 = self.tour[(i + 1) % variable_points]
          total += current_point.distance_following(point_2)
        return total

    # Helper function to insert a new point p into the Tour after a previous Node prev.
    # Example if the tour is a -> b -> c -> d
    # And you call _insert_at(p, c). Then the Tour should look like.
    # a -> b -> c -> p -> d
    # You can use this helper function in the insertNearest and insertSmallest
    # once you find the point you should insert p after.
    def _insert_at(self, p, prev: Node):
        if prev in self.tour:
          index = self.tour.index(prev)
          self.tour.insert(index + 1, p)
        else: 
          self.tour.append(p)

    # Insert a new Point p to the Tour using nearest neighbor heuristic
    def insert_nearest(self, p):
        if self.tour is not None:
          self.tour = Node(p)
          return
        min_dist = float('inf')
        nearest_node = None
        current_node = self.tour
        while current_node.next is not None:
          current_dist = current_node.point.distance_following(p)
        if nearest_node is not None:
          new_node = Node(p)
          new_node.next = nearest_node.next
          nearest_node.next = new_node
          self.tour.next = new_node

        else:
          new_node = Node(p)
          self.tour.next = new_node







    # Insert a new Point p to the Tour using smallest increase heuristic
    #def insert_smallest(self, p):                
        #if self.tour is not None:
       #   self.tour = Node(p)
       #   return

       # min_increment = float('inf')
       # ideal_node = None
        #current_node = self.tour
       # while current_node.next is not None:
         # curr_dist = current_node.point.distance_following(p)
          #next_dist = next_node.next.point.distance_following(p)
          #increment = next_dist - curr_dist

         # if increment < min_increment:
          # min_increment = increment
        #   ideal_node = current_node
        
        #  current_node = current_node.next

       # new_node = Node(p)
       # new_node.next = ideal_node.next 
       # ideal_node.next = new_node



class Node:
    def __init__(self, point):
        self.point = point
        self.next = None

class Tour:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        self.total_distance = 0.0

    def __str__(self):
        if self.head is None:
            return "Empty tour"
        points = []
        current_node = self.head
        while current_node:
            points.append(str(current_node.point))
            current_node = current_node.next
        return " -> ".join(points)

    def size(self):
        return self.count

    def distance(self):
        return self.total_distance

    def _insert_at(self, p, prev):
        new_node = Node(p)
        new_node.next = prev.next
        prev.next = new_node
        if prev == self.tail:
            self.tail = new_node
        self.count += 1
        self.total_distance += prev.point.distance_to(p) + p.distance_to(new_node.next.point) - prev.point.distance_to(new_node.next.point)

    def insert_nearest(self, p):
        if not self.head:
            self.head = Node(p)
            self.tail = self.head
            self.count += 1
        else:
            current_node = self.head
            min_dist = float("inf")
            nearest_node = None
            while current_node:
                current_dist = current_node.point.distance_to(p)
                if current_dist < min_dist:
                    min_dist = current_dist
                    nearest_node = current_node
                current_node = current_node.next
            self._insert_at(p, nearest_node)

    def insert_smallest(self, p):
        if not self.head:
            self.head = Node(p)
            self.tail = self.head
            self.count += 1
        else:
            current_node = self.head
            min_increment = float("inf")
            ideal_node = None
            while current_node:
                next_node = current_node.next
                if next_node:
                    curr_dist = current_node.point.distance_to(next_node.point)
                    new_dist = (current_node.point.distance_to(p) +
                                p.distance_to(next_node.point) - curr_dist)
                    if new_dist < min_increment:
                        min_increment = new_dist
                        ideal_node = current_node
                current_node = current_node.next
            self._insert_at(p, ideal_node)

#tour_instance = Tour()
#p1 = Point(0, 0)
#p2 = Point(3, 0)
#p3 = Point(0, 4)
#tour_instance.insert_nearest(p1)
#tour_instance.insert_nearest(p2)
#tour_instance.insert_nearest(p3)
#p4 = Point(2, 2)
#tour_instance.insert_smallest(p4)
#print(tour_instance)
#########

#def main():
  #header("Hello, World!", "*") 
  #header("Python Rocks", "!") 
  #header("Coders 4 EVER", "+") 
  
#Write a function, pyramid, that takes a single character and a number as parameters and
#displays an ASCII art pyramid to the screen with number rows:

#yramid(“*”, 2) *

#pyramid(“+”, 5) +

#pyramid(“x”, 10) x

def actionsPyramid(character, nums):
  for i in range(1, nums + 1):
    print(character * i)
  print('*' * 2)
  for a in range(1, 3):
    print('*' * a)
  
  for i in range(1, 6):
    print('+' * i)
    
  for j in range(1, 11):
    print('x' * j)

def difference(nums1, num2):
   subtr = nums1 - num2
   return subtr
    
def main():
    print(difference(5, 10) == 5)
    print(difference(10, 5) == 5)
    print(difference(200, -200) == 400)
    print('pyramid ("*", 2)' )
    actionsPyramid('*',  2)
    print('pyramid("+", 5)')
    actionsPyramid('+', 5 )
    print('pyramid("x", 10)')
    actionsPyramid('x', 10)
main()
    



#Write a function is_even that takes a number as a parameter and
#returns whether or not it is even. Test that your function works by
#calling it twice, once with an even number and once with an odd
#number, and print the results.

def even(num):
  if num % 2 == 0:
    print(num, 'Even')
  else:
    print(num, 'Odd')

def main():
  print(even(7))
  print(even(2))
  
main()


#fux = []
#for i in range(20):
# num = float(input('Enter a number:' ))
#fux.append(num) 

#avg = sum(fux) / len(fux)
#print('avg:', avg)

def mangle(hello):
  string = hello.upper()

  string = string[:2] + string[3:]
  string = string[:-3] + string[-2: ]
  return string
  
  
def main():
  print(mangle("hellothere"))
  print(mangle("42 degrees Celsius"))
  print(mangle("42 degrees Celsius"))
  print(mangle('ffffff'))
  test_in = ["hellothere", "42 degrees Celsius"]
  test_out = ["HELOTHRE","42DEGREES CELSUS"]
  for i in range(len(test_in)):
    print('mangle', test_out[i] + ':', mangle(test_in[i]) == test_out[i] )
main()    