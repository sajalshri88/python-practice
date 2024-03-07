#numeric data type
# num1 = 5
# print(num1,"is of type",type(num1))
# num2 = 2.0
# print(num2,"is of type",type(num2))
# num3=(1+2j)
# print(num3,"is of type",type(num3))
import nt

# numbers=(1,2,3)
# print(numbers)

#python list data type

# language=["swift","java","python"]
# print(language[0])
# print(language[1])
# print(language[2])

#python tuple data type
#
# product=("Xbox",2,2.3)
# print(product[0],type(product[0]),"inside tuple")
# print(product[1],type(product[1]),"inside tuple")
# print(product[2],type(product[2]),"inside tuple")

#numbers = (1,2,-5)
# print(numbers)
# print(numbers[0])
# print(numbers[2])
# print("total:",len(numbers))
# #for loop in tuple
# for i in numbers:
#     print(i)
#print(1 in numbers)
#fruits = ("apple","cherry","orange","mango")
#fruits[1] = 'tusas'
#print(fruits)
#^ this shows how tuples are imutable

#del fruits


# name="python"
# print(name)
#
# message="pythone for beginners"
# print(message)

#pythone set data type

# student_id={112,114,116,118,115}
# # print(student_id)
# #
# # print(type(student_id))
# print("initial set:",student_id)
#
# student_id.add(117)
# print("updated set:",student_id)
#
# new_student_id=[119,201,202,203,204]
# student_id.update(new_student_id)
# print("freshly added new students_id's:-",student_id)
# cancelled=student_id.discard(119)
# print("New admission is cancelled",student_id)
#
#students_name={"sameer","sajal","saksham","shweta"}
# cancelled=students_name.discard("shweta")
# print("New admission is cancelled",students_name)
#for i in students_name:
#    print(i)

#print("total elements:",len(students_name))

#a={1,2,3,4}
#b={5,6,7,8}
#print(a.union(b))

#print(a&b)

#print(b.difference(a))

#print(a^b)
#print(a==b)
#
# print(b.remove(6))


#python dictionary data type
#
#capital={"nepal":"kathmandu","italy":"turin","India":"delhi"}
#  print(capital)
#  print(type(capital))
# print(capital["nepal"])
#To delete element from dictionary using deleet function
# capital={"nepal":"kathmandu","italy":"turin","India":"delhi"}
# del (capital["nepal"])
# print(capital)

#to clear dictionary using clear function
# capital.clear()
# print(capital)

#to change the values of key use this
#capital["italy"]="Rome"
#print(capital)

#for loop for dictionary
# for cap in capital:
#     print(cap)
#     print()
# for itals in capital:
#     itals=capital["india"]
#     print(itals)
# a=capital.keys()
# print(a)
# b=capital.values()
# print(b)

#python string data type
#a=("hello")
#print(a)

#a=("hello",)
#print(a)
#print(type(a))

#this is how to make tuple out of string
# string=tuple("sajal")
# print("string becomes tuple here=",string)

#this is how to make tuple out of string
# list=("mango",1,1.23)
# list=tuple(list)
# print("a list becomes tuple=",list)
# print(type(list))

#a="sajal shrivastava is best person i know and also he is great professional i know."
# print("true if there are any digits will be there:-",a.isdigit())
# print("true if there are is any title will be there:",a.istitle())
# print("true if there are any digits will be there:",a.isalnum())
# print("true if there are any digits will be there:",a.isalpha())
# print("this will convert sentance into title:-",a.title())
# print("the count of o santence is :",a.count("o"))
# print("the index of _a_ in given santence:",a.index("a"))

#variations in strings
# a,b,c=5,3.2,"hello"
# print(a)
# print(b)
# print(c)
# a=b="program"
# print(a)
# print(b)

#User input
# name=input("please enter your name here: ")
# print(name)
# print("thank you, your name has been registered")

#name="john"
#print(name)
# num1 =10
# num2 =20
# sum=num1+num2
# print("the sum of give values is:",sum)
# multiplication=num1*num2
# print("the multiplication of given values is:",multiplication)
# subtract=num1-num2
# print("the suntraction of givenvalues is ",subtract)
# divide=num1/num2
# print(divide)

#now with user input
# num1 =int(input("enter 1st number here: "))
# num2 =int(input("enter 2nd number here: "))
# sum=num1+num2
# print("the sum of give values is:",sum)
# multiplication=num1*num2
# print("the multiplication of given values is:",multiplication)
# subtract=num1-num2
# print("the suntraction of givenvalues is ",subtract)
# divide=num1/num2
# print("the devisionof given values:",divide)

#Marks sheet and the results
# marks=int(input("enter a number here: "))
# if marks>=10:
#     print("you are awarede with new iphone 15")
# elif marks < 10 and marks>=9:
#     print("you are awared with new ipod")
# elif marks<9 and marks>=8 :
#     print("you are awarded with new phone cover")
# else:
#     print("i belive in you can do lot better than this son")

#For loop and break
# for i in range(1,30):
#     if i==17:
#         break
#     print(i)

#iteration
# a =("hello")
# for i in a:
#     print(a)

#While loop
# number=int(input("enter a number here: "))
# total=0
#
# while number !=0:
#     total +=number
#     number = int(input("enter a number here: "))
#     print("the sum is :",total)

# number=0
# while number <=4:
#     number =number+1
#     print("sajal is great professional sajal is rich, sajal is healthy, sajal is happy, sajal is achiving everthing he wanted from life" )
#
# number=int(input("enetr a number here: "))
# count=10
#
# while count >=1:
#     product = number * count
#     print(number, "*", count, "=", product)
#     count=count-1

 # a="2"
 # i=0
 # while i<=10:
 #      i=i+1
 #      print(a)

# num="hello"
# for i in range(4):
#      print(num)

# whats dictionary its nothing but set of keys and values

# dict={"name":"sajal","cgpa":3.2,"marks":88}
# print(dict)
# print(dict["name"])
# dict["name"]="shradhha"
# print(dict)

#nested dictionary
# dict={"name":"sajal","cgpa":3.2,"marks":
#     {"phy":88,
#      "chem":88,
#      "math":95}
#       }
# print(dict)
# print(dict["marks"]["chem"])
# print(list(dict.keys()))
# print(list(dict.values()))
# print(len(dict.keys()))
#
# new_dict={"city":"gondia"}
# dict.update(new_dict)
# print(dict)


#set
# nums={"randome",1,2,3,4,"set"}
# print(nums)
# print(type(nums))
#
# nums.pop()
# print(nums)
#
# nums.add(7)
# print(nums)
#
# nums.remove(7)
# print(nums)
#
# nums.clear()
# print(nums)


# dict={"table":["a piece if furniture","list of fact and figure"]}
# print(dict)
# dict2={"cat":"a small animal"}
# print(dict2)

# institute={"python","java","c++","pyhton","javascript","java","python","java","c++","c"}
# print(len(institute))

# marsksheet={"student_name":"sajal",
#             "marks":{"phy":int(input("enter marks here: ")),
#                      "chem":int(input("enter marks here: ")),
#                      "math":int(input("enter marks here: "))}}
# print(marsksheet)
#
# num={9,"9.0"}
#
# print(num)
