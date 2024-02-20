######### minis func
mini functions project with a list of different functions, and
@calc_auto_probs

 def bracket_combinations(numbers: int):
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



def first_reverse(str: string):
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
print(stack.pop()) # verify the expect output


def FindIntersection(strArr):
    arrN1 = strArr[0].split(', ')
    arrN2 = strArr[1].split(', ')
    matchArr = []

    for e in arrN2:
        if e in arrN1:
            matchArr.append(e)

    return ','.join(matchArr) if matchArr else False

# keep this function call here to run 
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
# stack notes
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


  public class Node<T> {
	private T		data;
	private Node 	next;



	public Node(T data) { this(data, null); }
	public Node(T data, Node next) {
		this.data = data;
		this.next = next;
	}

public T get_data()    { return data; }
public Node get_next() { return next; }

public static void main(String[] args) {
	Node new_node = new Node(“first node data”);
	Node next_node = 
new Node(“second node data”, new_node);
System.out.println(next_node.get_data())
}
}//

function LongestWord(sen) {

  sen = sen.trim();
  sen = sen.replace(/[^a-zA-Z0-9 ]/g, '');
  
  let longest = ""

  var arr = sen.split(" ").forEach(word => {
      if(word.length > longest.length) longest = word;
  })

  return longest;

}


function PriorityQueue () {
  this.collection = [];
  this.printCollection = function() {
    console.log(this.collection);
  };
  // Only change code below this line
  this.enqueue = function (item, priority) {
   let index = this.collection.findIndex(elem => elem[1] > item[1]);
    if (index !== -1) {
      this.collection.splice(index, 0, item);
    } else {
      this.collection.push(item);
    }
  };
  this.dequeue = function (item, priority) {
  return this.collection.shift()[0];
  };
  this.size = function () {
  return this.collection.length;
  }
  this.front = function () {
   if (!this.isEmpty()) {
  return this.collection[0][0];
  }
  
  };
  this.isEmpty = function () {
  return this.collection.length === 0;
  };
  // Only change code above this line
}
   
// keep this function call here 
LongestWord(readline());


class MyHashMap:

    def __init__(self):
        self.map = [None _ for i in range(10000)]

    def put(self, key: int, value: int) -> None:
        hash_val = self.hash_func(key)
        if not self.map[hash_val]
           self.map[hash_val] = [(key, value)]
        else:
            j = self.map[hash_val]
            for k, v in j:
                if k == key
                   v = value
                   return 
            j.append(key, value)

           
        
    def hash_function(self, key):
        return key % 10000
    def get(self, key: int) -> int:
        hash_val = self.hash_function(key)
        if self.map[hash_val]:
            j = self.map[hash_val]
            for k, v in j:
                if k== key:
                    return v
        return -1
        

    def remove(self, key: int) -> None:
        hash_val = self.hash_function(key)
        if self.map[hash_val]:
            j = self.map[hash_val]
            for i in range(len(j)):
                tuples = j[i]
                  if tuples[0] == key:
                      if i != len(j) - 1:
                          temp = j.pop()
                          return 
                  j.pop()
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

/* 
     C Program for simple recursion
     This program similates the recurrence relation function , T(n) = T(n-1) +3, T(0)=5.
     By: randerson112358
 */

# include < stdio.h >
   
int T( int n); // Defining function T().
 
int main(void)
{
    int n = 8;
    int i;
     
   for(i=0; i < n;  i++)
    {
        printf("T(%d) = %d\n", i, T(i) ); // prints 5, 8, 11, 14, 17, 20, 23, 26
    }

     //Comment out the system("pause") if you are not using Windows
     system("pause");
 }

   int T( int n)
    {
        if( n == 0)
           return 5;
        else
           return T(n-1) + 3;
    }

    //will start creating a separator
    //monitor the commits

    #mix and matching code for the sake of sharpness
    def stringent(n):
    	for i in range(n-1):
     		print(i)

#currently mapping everything; 

def longest_subsequence(array):
    """
    Finds the length of the longest increasing subsequence in an array.

    Args:
        array: An array of numbers.

    Returns:
        The length of the longest increasing subsequence in the array.
    """

    n = len(array)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # Base cases.
    for i in range(n):
        dp[i][i] = 1

    # Recursive case.
    for i in range(n):
        for j in range(i + 1, n):
            if array[i] < array[j]:
                dp[i][j] = dp[i][j - 1] + 1
            else:
                dp[i][j] = dp[i][j - 1]

    return dp[0][n - 1]

 # Here is a practice code from a cypress test

 describe('Map Page Tests', () => {
  beforeEach(() => {
    // Log in as admin
    cy.loginAdmin();

    // Visit the map page
    cy.visit('/');

    // Wait for the page and required data to load
    cy.waitForHomePageData();
  });

  it('should interact with the map and verify location details', () => {
    // Click on the map tab (assuming there is a tab for the map)
    cy.contains('MAP').click(); // Make "MAP" all caps
    cy.contains('Satellite');
   
    cy.contains('ALABAMA').click();
    //cy.contains('MONTGOMERY');

   
  });
});
 
//will be adding more functions


'''
Given a DAG that is represented as a collection of edges, i.e. ["n1", "n2"] means that n1 precedes n2 (visually, n1 -> n2),
'''

'''
Create an adjacency list for it.
'''
def to_adjacency_list(edges: list[list[str]]) -> dict[str, list[str]]:
    adj_list = {}
    for edge in edges:
        n1, n2 = edge
        if n1 not in adj_list:
            adj_list[n1] = []
        if n2 not in adj_list:
            adj_list[n2] = []
        adj_list[n1].append(n2)
    return adj_list



from __future__ import annotations

'''
Complete the StreamHandlerKLargest class that has a capacity k by filling in the methods.
'''
import heapq
class StreamHandlerKLargest:
  def __init__(self, k: int) -> None:
    self.k = k
    self.k_largest_ele = []


  
  '''
  This method adds the stream element to the collection. 
  You only need to store the k largest elements seen so far at any given point in time.
  '''
  def add_stream_element(self, e: int) -> None: 
    if len(self.k_largest_ele) < self.k:
      self.k_largest_ele.append(e)
    else:
      min_e = min(self.k_largest_ele)
      if e > min_e:
        self.k_largest_ele.remove(min_e) 
        self.k_largest_ele.append(e)


  def k_largest(self) -> list[int]:
    return sorted(self.k_largest_ele)
'''
Complete the StreamHandlerKSmallest class that has a capacity k by filling in the methods.
'''

class StreamHandlerKSmallest:
  def __init__(self, k: int) -> None:
    self.k = k
    self.k_smallest_ele = []
  
  '''
  This method adds the stream element to the collection. 
  You only need to store the k smallest elements seen so far at any given point in time.
  '''
  def add_stream_element(self, e: int) -> None: 
   
    if len(self.k_smallest_ele) < self.k:
      self.k_smallest_ele.append(e)
    else:
      max_e= max(self.k_smallest_ele)
      if e < max_e:
        self.k_smallest_ele.remove(max_e)
        self.k_smallest_ele.append(e)

  ''' 
  This method returns the k smallest elements seen so far.
  '''
  def k_smallest(self) -> list[int]: 
    return sorted(self.k_smallest_ele)

''' 
Write a function that creates a copy of the list, and sorts it in ascending order
using a heap.
'''
def heapsort(input_list: list[int]) -> list[int]: 
  heap = []

  for item in input_list:
    heapq.heappush(heap, item)


  sorted_list = [heapq.heappop(heap) for _ in range(len(heap))]
  
  
  return sorted_list

'''
Suppose we have some data that can be expressed as a tuple (a, b, c). 
We want to get the top k tuples out of a collection of n total tuples, 
where k <= n. Each datapoint has a score, defined as 2*a + 5*b + 10*c, 
and the higher the score, the greater the datapoint. 
Complete the class for this datapoint object, and complete the below function, using a heap to do so.
'''
class Datapoint:
  def __init__(self, a: int, b: int, c: int) -> None:
    self.a = a
    self.b = b
    self.c = c

  def to_tuple(self) -> tuple[int, int, int]:
    return (self.a, self.b, self.c)

  
  def track(self) -> int:
    return 2 * self.a + 5 * self.b + 10 * self.c 

  


  # TODO: you may need to add additional methods here. 

# Return them as tuples, using the to_tuple method in the Datapoint class.
import heapq
def get_top_k_datapoints(data_collection: list[Datapoint], k: int) -> set[tuple[int, int, int]]:
  max_heap = []

  for data in data_collection:
    track = 2 * data.a + 5 * data.b + 10 * data.c
    if len(max_heap) < k:
      heapq.heappush(max_heap, (-track, data.to_tuple()))

  
  top_k = set()
  for _ in range(k):
    if max_heap:
      _, datapoint = heapq.heappop(max_heap)
      top_k.add(datapoint)


  return top_k




  from __future__ import annotations
from typing import List
import copy
# =============== BEGIN DO NOT MODIFY ========================
class Treasure:
    pass

class Monster:
    def __init__(self, name: str, damage: int):
        self.name = name 
        self.damage = damage 
        self.next = []

    def append_monster(self, monster):
        self.next.append(monster)

    def append_treasure(self, treasure: Treasure):
        self.next.append(treasure)

class Player:
    def __init__(self, health: int):
        self.health = health 
    
    def battle(self, monster: Monster):
        self.health -= monster.damage
# =============== END DO NOT MODIFY ========================


#####


words = ["cat", "act", dog", "tac"]

# This is effectively an adjacency list, but we use a map as the implementation.
anagram_neighbors_map = {}
for word1 in words:
  anagram_neighbors_map[word1] = []
  for word2 in words:
    if word1 != word2:
      # If word1 equals word2 when sorted they are anagrams.
      if sorted(word1) == sorted(word2):
        anagram_neighbors_map[word1].append(word2)

for word in anagram_neighbors_map:
  print(word,anagram_neighbors_map[word])

# This prints
# "cat" : ["act", "tac"]
# "act" : ["cat", "tac"]
# "dog" : []
# "tac" : ["act", "cat"]




def _dfs_count_paths_with_player(self, node: Monster, player: Player, visited: set) -> (int, int):
      if node in visited and player.health <= 0:
        return 0, 0
      
      visited.add(player)
      total_paths, successful_paths = 0, 0

      for child in node.next:
        if child not in visited and hasattr(child, 'next'): #check if visited, if not increment with success
          child_total, child_successful = self._dfs_count_paths_with_player(child, player, visited)
          total_paths += child_total
          successful_paths += child_successful
      
      return total_paths, successful_paths
############adding to

def probability_player_will_make_it(self, player: Player) -> float:
      visited = set()
      
      def dfs(node, current_health):
        if current_health < 0:
            return 0.0

        if isinstance(node, Treasure):
            visited.add(node)
            return 1.0

        if isinstance(node, Monster):
            current_health -= node.damage

        if not node.next:
            return 0.0

        return sum(dfs(neighbor, current_health) for neighbor in node.next) / len(node.next)

      return dfs(self.monster, player.health) 
###


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    time_obj = datetime.strptime(s, '%I:%M:%S%p')

    return time_obj.strftime('%H:%M:%S')







    def countApplesAndOranges(s, t, a, b, apples, oranges):
    
    app_count= 0
    oran_count = 0
    
    for app_dist in apples:
        appl_pos = a + app_dist
        if s <= appl_pos <= t:
            app_count += 1
    
    for oran_dist in oranges:
        oran_pos = b + oran_dist
        if s <= oran_pos <= t:
            oran_count += 1
    
    print(app_count)
    print(oran_count)



    def breakingRecords(scores):
    # will require dynamic programming due to the tabulation of records
    #int[2]: An array with the numbers of times she broke her records. Index 0 is for breaking most points records, and index 1 is for breaking least points records.
    
    if not scores:
        return [0, 0]
    
    low_score = high_score = scores[0]
    low_brok_rec = high_brok_rec = 0
    
    for score in scores[1:]:
        if score < low_score:
            low_score = score
            low_brok_rec += 1
        elif score > high_score:
            high_score = score
            high_brok_rec +=1
            
    return [high_brok_rec, low_brok_rec]


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #which point is closest 
        #k in the input
        #points will be in a list method function
        #using euclidean between the two points
        #function for the actual space complex/dist
        
        def dist(pointer):
            print(pointer)
            return (pointer[0] ** 2) + (pointer[1] ** 2)
               
        # 
        min_val = min(points, key=dist) # sort and compare each element using key=
        print("min", min_val)
        max_val = max(points, key=dist)
        print("max", max_val) 

        closest = [pointer for pointer in points if dist(pointer) < dist(max_val)]
        print("closest", closest)
        result = (closest)

        return result



class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #which point is closest 
        #k in the input
        #points will be in a list method function
        #using euclidean between the two points
        #function for the actual space complex/dist
        # min heap kth, should partition the list
        # you could do k * m
        # possibly bubblesort
        # sorting is auto nlogn
        def dist(pointer):
            print(pointer)
            return (pointer[0] ** 2) + (pointer[1] ** 2) # O(1)
               
        # 
        sorted_list = sorted(points, key=dist) # because of the set values O(n )

     # closest = [pointer for pointer in points if dist(pointer) < dist(k)]
     # print("closest", closest)
     # result = (closest)
     # nlogn
        return sorted_list[:k]


'''
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
'''

'''
Question 1. Solve the above problem using Top Down Dynamic Programming
'''
def unique_paths_top_down(m: int, n: int) -> int:
  dp = [[0] * n for _ in range(m)]

  # helper func for top down approach
  def dfs(i: int, j: int) -> int:
    nonlocal dp
    if i == m - 1 and j == n - 1:
      return 1
    if i >= m or j >= n:
      return 0
    if dp[i][j] > 0:
      return dp[i][j]
    
    #cal the number of paths
    down = dfs(i + 1, j)
    right = dfs(i, j + 1)

    dp[i][j] = down + right
    return dp[i][j]
  
  return dfs(0, 0)

'''
Question 2. Solve the above problem using Bottom Up Dynamic Programming
'''
def unique_paths_bottom_up(m: int, n: int) -> int:
  dp = [[0] * n for _ in range(m)]

  #base case through only way which is first column or first row
  for i in range(m):
    dp[i][0] = 1

  for j in range(n):
    dp[0][j] = 1
  
  #calc number of paths using bottom up
  for i in range(1, m):
    for j in range(1, n):
      dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
  
  return dp[m -1][n - 1]


 import unittest


def get_permutations(string):
    
    # 1. build up a cache to store sub-problem solutions
    # 2. aggregate the solutions to build a bigger solution
    
    # 'abcd'
    # 1. 
    # 2. 
    
    # solutions = {
    #     '': [''],
        # 'a': ['a'],
        # 'b': ['b'],
        # 'c': ['c'],
        # 'ab': ['ab', 'ba'],
        # 'abc': ['abc', 'bac', 'acb', 'bca', 'cab', 'cba'],
        # 'abcd': ['abcd', 'bacd', 'acbd', 'bcad', .... ]
    # }
    # for letter in string:
    #     solutions[letter] = [letter]
    
    permutations = [''] # ['abc', 'bac', 'acb', 'bca', 'cab', 'cba']
    # for i, letter in enumerate(string):
    for i in range(len(string)):
        letter = string[i]
        
        next_permutations = []
        for permutation in permutations:
            for pos in range(len(permutation) + 1):
                # add the letter to that position
                # if permutation== '':
                #     pass
                new_perm = permutation[:pos] + letter + permutation[pos:] # 
                next_permutations.append(new_perm)
        
        permutations = next_permutations
    return set(permutations)
    
    # code will need
    # 1. array of previous solutions
    # 2. for loop.. to do what?


  # Tests

class Test(unittest.TestCase):
    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
```

