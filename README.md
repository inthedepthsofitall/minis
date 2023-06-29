# minis
mini projects


 def bracket_combinations(numbers):
    def combo_possibilities(open, shut):
        if open == 0 and shut == 0:
            return 1
        result = 0
        if open > 0:
            result += combo_possibilities(open - 1, shut)
        if closed > open:
            result += combo_possibilities(open, shut - 1)
        return result

    return calculate_possibilities(numbers, numbers)



def first_reverse(str):
    return str[::-1]

input_str = input("Enter a string: ")
print(first_reverse(input_str))


def __init__(self, item):
     self.item = item
      self.next = None
stack = Stack()#stack.push(1) 
stack.push(2) 
print(stack.pop()) 
stack.push(3) 
stack.push(4) 
print(stack.pop()) 
print(stack.pop())


def FindIntersection(strArr):
    arrN1 = strArr[0].split(', ')
    arrN2 = strArr[1].split(', ')
    matchArr = []

    for e in arrN2:
        if e in arrN1:
            matchArr.append(e)

    return ','.join(matchArr) if matchArr else False

# keep this function call here
print(FindIntersection(input()))

#Your buffer should be 64 bytes large.
#Passed:Your i32View view of your buffer should be 64 bytes large.
#Passed:Your i32View view of your buffer should be 16 elements long.

var byteSize = 64
var buffer = new ArrayBuffer(byteSize);
var i32View = new Int32Array(buffer);
buffer.bytelength;
i32View.byteLength;
var byteSize = 64
var buffer = new ArrayBuffer(byteSize);
console.log(i32View)

#Typed arrays do not have some of the methods traditional arrays have such as .pop() or .push(). Typed arrays also fail Array.isArray() that checks if something is an array. #Although simpler, this can be an advantage for less-sophisticated JavaScript engines to implement them.

#First create a buffer that is 64-bytes. Then create a Int32Array typed array with a view of it called i32View

#Here we have a stack of homework assignments represented as an array: "BIO12" is at the base, and "PSY44" is at the top of the stack.

#Modify the given array and treat it like a stack using the JavaScript methods mentioned above. Remove the top element "PSY44" from the stack. Then add "CS50" to be the new #top element of the stack.

var homeworkStack = ["BIO12","HIS80","MAT122","PSY44"];
// Only change code below this line
// we want to pop to get rid psy44 and append CS50
homeworkStack.pop()
homeworkStack.push("CS50")
console.log(homeworkStack)

function Queue() {
  var collection = [];
  this.print = function() {
    console.log(collection);
  };
  // Only change code below this line
    this.enqueue = function(val) {
    collection.push(val);
  };
  this.dequeue = function(val) {
     return collection.shift(val);
  };
  this.front = function() {
      return collection[0];
  };
  this.size = function() {
      return collection.length;
  };
  this.isEmpty = function() {
       return collection.length === 0; 
  };

}


def double(x):
  return 2 * x
  
def quad(x):
  return double(double(x))
  
def hello(name):
  print('hello cunt,', name + ' how are you today?')
  
def repeat(string, n):
  print(string, n)
  
def square(string, n):
  for i in range(n):
    print(repeat(string, n))
    
print(double(5))
print(quad(4))
hello('Kyke')
print(repeat('hi', 10))
square('*', 4)

def uniq_count_dict(string):
  unique_string = {}
  for i in string:
    unique_string[i] = True # a simple of way of stating that whatever index is fine plus the return on the length should measure each different i
  return len(unique_string)
print(uniq_count_dict("122233444555"))


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    
        max_sum = float('-inf')  # Initialize max_sum to negative infinity
    
        for i in range(4):
            for j in range(4):
                if -9 <= arr[i][j] <= 9:  # Check the constraint on arr[i][j]
                    # Calculate the sum of the current hourglass
                    current_sum = (
                        arr[i][j] + arr[i][j + 1] + arr[i][j + 2] +
                        arr[i + 1][j + 1] +
                        arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
                    )
    
                    # Update max_sum if the current_sum is greater
                    max_sum = max(max_sum, current_sum)
    
        return max_sum
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()


def insertNodeAtPosition(llist, data, position):
    if llist is None:
        llist = SinglyLinkedListNode(data)
        return llist

    if position == 0:
        new_node = SinglyLinkedListNode(data)
        new_node.next = llist
        return new_node

    prev_node = llist
    current_node = llist.next
    i = 1
    while i < position and current_node is not None:
        prev_node = current_node
        current_node = current_node.next
        i += 1

    if current_node is None:
        return llist

    new_node = SinglyLinkedListNode(data)
    new_node.next = current_node
    prev_node.next = new_node

    return llist
 Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    if head is None:
        new_node = SinglyLinkedListNode(data)
        return new_node
    current_node = head
    while current_node.next is not None:
        current_node = current_node.next
    
    new_node = SinglyLinkedListNode(data)
    current_node.next = new_node
    
    return head


def fec_sum(n):#recursion
  if n <= 1:
    return 0
  return n + fec_sum(n - 1)


def foo(lst: list[int], target: int):
  lo = 0
  hi = len(lst) - 1
  ans = -1
  while lo <= hi:
    mid = lo + (hi - lo) // 2
    if target == lst[mid]:
      return mid
    elif target > lst[mid]:
      lo = mid + 1
    else:
      hi = mid - 1
  print(ans)
