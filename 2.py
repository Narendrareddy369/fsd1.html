def name(Name):
    return Name
z=name("lakshman")
print(z)
print(name)

def square(num):
    result=num*num
    return result
sq=("square of the number is",square(5))
print(sq)

def my_function(PACE):
    for x in PACE:
       print(x)
courses=["Data science","Fullstack developement","Digital marketing"]
my_function(courses)

course="Data Science"
def display():
    print(course)
display()
print(course)

def show_number(*args):
    print(args)
show_number(10,20,30)

def show_details(**details):
    print(details)
show_details(name="Lakshman",age=18,city="Gonugunta",Number=562)
show_details(name="Venkata Lakshmi",age=18,city="LakshmiPuram",Number=562)

#string=input("Enter a string:")
#count=len(string)
#print("Number of characters:",count)

#text = input("Enter a string: ")
#vowels = "aeiouAEIOU"
#count = 0
#for char in text:
 #   if char in vowels:
  #      count += 1
#print("The number of vowels in the string is:", count)


#1
numbers = [1, 2, 3, 4, 5]
print(numbers)

#2
numbers = [1, 2, 3]
numbers.append(6)
print(numbers)

#3
numbers = [1, 2, 3, 4]
numbers.remove(2)
print(numbers)

#4
numbers = [5, 3, 8, 6, 1]
largest = max(numbers)
print(largest)

#5
numbers = [5, 3, 8, 6, 1]
largest = min(numbers)
print(largest)

#6
numbers = [10, 20, 30, 40]
print(numbers[1])

#7
numbers = [1, 2, 2, 3, 2]
count_2 = numbers.count(2)
print(count_2)

#8
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)
 
#9
numbers = [10, 20, 30, 40, 50]
first_three = numbers[:3]
print(first_three)

#10
even_numbers = []
for i in range(1, 6):
    even_numbers.append(i * 2)
print(even_numbers)
