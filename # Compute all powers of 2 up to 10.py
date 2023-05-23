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


import turtle
turtle.color('red')

size = 100
for i in range(3):
  turtle.forward(size)
  turtle.left(120)
###

import turtle
turtle.color('red')
def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()

def move(len):
  back(-1 * len)
   
def triangle(size):
  for i in range(3):
    turtle.forward(size)
    turtle.left(120)
    
def square(size):
  for i in range(4):
    turtle.backward(size)
    turtle.left(90)
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



triangle(100)
back(75)
triangle(50)
back(50)
triangle(25)
square(125)
back(100)
square(25)
back(25)

