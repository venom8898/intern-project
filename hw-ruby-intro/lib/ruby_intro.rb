# When done, submit this entire file to the autograder.


# Part 1
def sum(arr)
if arr.length>0
  arr.inject { |sum, x| sum + x }
else 
  return 0 
end 
end 

def max_2_sum(array)
  if array.length > 1
    array.sort!
    max2=[]
    max2 << array.max
    array.pop
    max2 << array.max
    max2.inject { |sum, x| sum + x } 
else if array.length == 1
  array.max
else
  return 0 
end
  end
end

def sum_to_n?(array, n)
if array.length <2
  return false
end
hasValue = false 
currentPos=1
while hasValue == false 
possVal=array[currentPos-1]+array[currentPos]
if possVal==n
  hasValue = true
  return hasValue
else if currentPos < array.length-1
  currentPos +=1
else return false
end
end
end
end

# Part 2

def hello(name)
  return "Hello, " + name
end

def starts_with_consonant?(string)
arr = string.chars.to_a
properString= /[^aeiouAEIOU\W\d]/ =~arr[0]
if arr.length<1
  return false

else if properString == nil 
  return false 
else 
  return true
end  
end 
end

def binary_multiple_of_4?(string)
arr = string.chars.to_a 
properString= /[2-9\D]/ =~ string
if arr.length==1 and arr[0]=="0"
  return true 
end
if (properString != nil or arr.length < 3 )
return false 
else if arr[arr.length-1]=="0" and arr[arr.length-2]=="0"
  return true 
else
return false
end
end
end
# Part 3

class BookInStock
  def initialize (isbn, price)
  @isbn=isbn
  @price=price
  def argument_test(isbn, price)
    if isbn == "" or price <=0
      raise ArgumentError
    end
  end
  argument_test(isbn,price)
  end
def price_as_string
toString = sprintf "%.2f", @price
priceAsString= "$" + toString
return priceAsString
end
end
