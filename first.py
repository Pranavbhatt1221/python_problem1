#   #   import random
#   # num =67
#   # print("enter a number")

#   # user_num=int(input("enter a num to guess"))
#   # if(num==user_num):
#   #       print("you are correct")
      
#   # elif(num<user_num):
#   #       print("wapas guess kar bsdk")
#   # elif(num>user_num):
#   #       print("thoda kam guess kar bsdk")
#   # else:
#   #       print("nikal bkl") ***###

# def calc():
#     def add(num1,num2):
#         print("sum =",num1+num2)
#     add(int(input("enter number 1")),int(input("enter num 2")))
#     def mul(num1,num2):
#         print("mul =",num1*num2)
#     mul(int(input("enter number 1")),int(input("enter num 2")))
#     def sub(num1,num2):
#         print("sub =",num1-num2)
#     sub(int(input("enter number 1")),int(input("enter num 2")))
#     def div(num1,num2):
#         print("div =",num1/num2)
#     div(int(input("enter number 1")),int(input("enter num 2")))
# # calc()   
# month_con={
#     "jan":"january",
#     "feb":"feburary",
#     "mar":"march",
#     "apr":"april",

# }
# month_con ["jan"]="december"
# print(month_con["jan"])
# i=1
# while i<=10:
    
#     print(i)
#     i+=1
# print("done with loop")

#create a guess game

# screct_word="india"
# user_guess=""

# i=1
# while user_guess!=screct_word and i<4:
#     user_guess=input("Enter guess:")
#     if(user_guess!=screct_word):
#         print("try again harder")
#     else:
#         print("you win")   
#         break 
#     i+=1
# if(user_guess!=screct_word) :
#     print("you loose,out of guesses")  
# nums=["gian","suniyo","nobita","shizuka","doraemon"]
# for nums in nums:
#     print(nums)

# number_grid=[
# [1,2,3],
# [4,5,6],
# [7,8,9],
# [0] 
# ]
# for row in number_grid:
# print(number_grid)


#opps in python 1

# class Car :
#     brand="maruti"
#     color="torquioes"
#     price=2000000

# car1=Car()
# print(car1.brand)
# print(car1.color)

# car2=Car()
# print(car2.price)


# class Student:
#     def __init__(self):
#         print("daddys homes bitches")

# s1=Student()


# class Student:
#     def __init__(self,fullname,idno):
#         self.name=fullname
#         self.rollno=idno
# s1=Student("pranav",21)
# print(s1.name)
# print(s1.rollno)

# s2=Student("rahul",33)
# print( "my name is:", s2.name, "my roll no is:",s2.rollno)

# class Student:
#     monitor="yash"

# def __init__(self,name,marks):

#         self.name=name
#         self.marks=marks

# def hello(self):
#         print("hello",self.name)
        
# s1=Student("pranav",97)
# s1.hello()
           
# class student :
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def avg_mark(self):
#         sum=0
#         for val in self.marks:
#           sum +=val
#         print("Hi",self.name,"your avg marks are",sum/3)

# s1=student("pranav",[99,92,89])
# s1.avg_mark()
 
# class student:
#     def __init__(self):
            

#      @staticmethod
#      def hello(self):
#             print("hello")
# s1=student()
# s1.hello()
# del s1
# class Branch:
#     @staticmethod
#     def branch_name():
#         print("Branch name is sbi phatak road")

# class Bank(Branch):

#     def __init__(self,acc_no,acc_pass):
#         self.acc_no=acc_no
#         self.__acc_pass=acc_pass

#     def reset_pass(self):
#         print("ur current password is:",self.__acc_pass)
        

# b1=Bank(1234,"ababc")
# print(b1.acc_no)
# b1.reset_pass()
# print(b1.branch_name())

# class emp(Bank):
#     def __init__(self,empn):
#         self.empn=empn
# emp1=emp("harshit")
# emp1.branch_name() 

class A:
    varA=("fuck off")
class B:
    varB=("lick my balls bitch")
class C(B):
    varc=("hi asshole")
c1=C()
print(c1.varB)

  

class D(A,B,C):
    varD=("ho my name i d rdj")
d1=D()
print(d1.varc)
print(d1.varA) 