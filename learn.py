# print("https://meet.google.com/vpd-rynf-ixs".split(".")[1])
# print("https://web.whatsapp.com/".split(".")[1])
# print("https://www.youtube.com/watch?v=abc123".split(".")[1])
# print("https://www.example.com/path/to/resource".split(".")[1]) 
# print("https://www.example.com/path/to/resource".split(".")) 
# # forms  list and from list we extract index 1 so that we can get our  desired domain
# from os import sep
# from turtle import end_fill


# print("hello")
# print("hello, \n world")
# n=1
# print("hello",n,"world")
# print(f"hello {n} world")
# a=10
# b=20
# print(a+b,a-b,a*b,a/b,a%b,a**b)# arithmetic
# print(a>b,a<b,a==b,a!=b,a>=b,a<=b)# comparison
# a+=b# assignment
# print(a)
# print("hello","how are you",end="")
# end
# sep
# print()
# decision making or conditional statements
# if elif else
# mark=37
# if mark>=90:
#  print("grade A") #IndentationError: expected an indented block after 'if' statement on line 29
# elif mark>=80:
#     print("grade B")
# elif mark>=70:
#     print("grade C")
# elif mark>=60:
#     print("grade D")
# else:
#     print("fail")
# name="sriram"
# tamil=90
# english=80
# maths=77
# science=90
# social=80
# if tamil>=75 and english>=75 and maths>=75 and science>=75 and social>=75:
#     print(f"grade A {name} english={english} maths={maths} science={science} social={social}")
# else:
#     print(f"fail {name} english={english} maths={maths} science={science} social={social}")
# a=7
# b=8
# c=9
# if a>b and a>c:
#     print("a is greater")
# elif b>a and b>c:
#     print("b is greater")
# else:
#     print("c is greater")
# for loop
# for i in "sriram":
#     print(i)
# for i in range(1,20,2):
#     print(i)
# table =3
# name="sriram"
# phone=9876543210
# addresss="123 , street"
# print(f"name={name} phone={phone} address={addresss}")
# information=["sriram","9876543210","123 , street","sriram"]
# (information[1])=765432190
# print(information)
# print(type(information))
# for i in information:
#     if i==9876543210:
#         print("phone number is",i)

# print(dir(information))
# for i in dir(information):
#     if not i.startswith("__"):
#         print(i)
# information.append(["saravanan",9876543210,"123 , street"])
# # print(information)
# information.extend(["saravanan",9876543210,"123 , street"])
# print(information)
# information.insert(1,"saravanan")
# print(information)
# print(information.index("sriram",1))
# print(information)
# a=information
# print(a)
# # print(id(a),id(information))
# a.clear()
# print(a)
# print(information)
# list=[]
# for i in range(1,11):
#     list.append(i)
# print(list)
list=(i for i in range(1,11) if i%2==0)
print(list)









    

    
