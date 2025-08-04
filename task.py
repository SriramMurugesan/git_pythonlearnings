# Use Python's built-in functions (Easy):

# 1. Find the Maximum in a List
numbers = [3, 7, 2, 8, 1]
max = numbers[0]
for i in numbers:
    if i > max:
        max = i
print(max)

# 2. Sort a List in Descending Order
numbers = [4, 1, 9, 2]
numbers.sort(reverse=True)
print(numbers)

# 3. Convert a List of Strings to Integers
string_list = ['10', '20', '30', '40']
int_list = []
for i in string_list:
    x = int(i)
    int_list.append(x)
print(int_list)

# 4. Find the Length of Each Word in a List
words = ['apple', 'banana', 'cherry']
l = []
for i in words:
    x = len(i)
    l.append(x)
print(l)

# 5. Filter Even Numbers
numbers = [1, 2, 3, 4, 5, 6]
even = []
for i in numbers:
    if i % 2 == 0:
        even.append(i)
print(even)

# 6. Get the Sum of Elements in a List
numbers = [5, 10, 15]
x = 0
for i in numbers:
    x = x + i
print(x)

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
numbers = [1, 2, 3, 4]
all_positive = True
for i in numbers:
    if i < 0:
        all_positive = False
print(all_positive)

numbers = [1, -2, 3]
all_positive = True
for i in numbers:
    if i < 0:
        all_positive = False
print(all_positive)

# 9. Check if Any Element is Negative
numbers = [1, 2, 3, -4, 5]
any_negative = False
for i in numbers:
    if i < 0:
        any_negative = True
print(any_negative)

numbers = [1, 2, 3, 4, 5]
any_negative = False
for i in numbers:
    if i < 0:
        any_negative = True
print(any_negative)

# 10. Reverse a String
s = 'Python'
reversed = ""
for i in s:
    reversed = i + reversed
print(reversed)
