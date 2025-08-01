# Use Python's built-in functions (Easy):

# 1. Find the Maximum in a List
# numbers = [3, 7, 2, 8, 1]
# max=numbers[0]
# for i in numbers:
#     if i > max:
#      max=i
# print(max)
# 2. Sort a List in Descending Order
#     numbers = [4, 1, 9, 2]
#     Output: [9, 4, 2, 1]
# numbers=[4,1,9,2]
# numbers.sort(reverse=True)
# print(numbers)
# 3. Convert a List of Strings to Integers
# string_list = ['10', '20', '30', '40']
#     Output: [10, 20, 30, 40]
# int_list=[]
# for i in string_list:
#     x=int(i)
#     int_list.append(x)
# print(int_list)


# 4. Find the Length of Each Word in a List
# words = ['apple', 'banana', 'cherry']
#     Output: [5, 6, 6]
# l=[]
# for i in words:
#     x=len(i)
#     l.append(x)
# print(l)

# 5. Filter Even Numbers
# numbers = [1, 2, 3, 4, 5, 6]
#     Output: [2, 4, 6]
# even=[]
# for i in numbers:
#     if i%2==0:
#         even.append(i)
# print(even)
# 6. Get the Sum of Elements in a List
# numbers = [5, 10, 15]
#     Output: 30
# x=0
# for i in numbers:
#     x=x+i
# print(x)
# 7. Find the Minimum and Maximum
numbers = [12, 3, 9, 1, 5]
#     Output: (1, 12)
max=0
min=numbers[0]
for i in numbers:
    if i>max:
        max=i
    if i<min:
        min=i
print(min,max,sep=",")
        

# 8. Check if All Elements are Positive
#     numbers = [1, 2, 3, 4]
#     Output: True

#     numbers = [1, -2, 3]
#     Output: False

# 9. Check if Any Element is Negative
#     numbers = [1, 2, 3, -4, 5]
#     Output: True

#     numbers = [1, 2, 3, 4, 5]
#     Output: False

# 10. Reverse a String
#     s = 'Python'
#     Output: 'nohtyP'