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


