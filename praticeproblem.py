# 1# user input of name and age

# name=input("what is your name!\n")
# age=input("What is your age\n")

# print("My name is",name,"& My age is",age)


# 2.#pyramid 
# rows=5
# for i in range(1,rows+1):
#     print(" "*(rows-i), end="")
#     print("*"*(2*i-1))

# 3.#prime number check
# num=int(input("Enter a number to check if it is prime or not\n"))
# if num %2==0 and num>2 :
#    print(num,"is not a prime number")s
# else:
#     print(num,"is a prime number")

# 4#prime number check using for loop
# num=int(input("enter a number to check if it is prime or not\n"))
# if num>1:
#     for i in range(2,num+1):
#         if(num%2==0):
#             print(num,"is not a prime number")
#             break
#     else:
#         print(num,"is a prime number")

# 4.#area of triangle

# base=float(input("Enter The Base Of The Triangel\n"))
# hieght=float(input("Enter The Hieght Of The Triangle\n"))
# area=0.5*base*hieght
# print("The Area Of The Triangle is",area)

#5.calculate sq root
# num=int(input("Enter the no \n"))
# for i in range(1,num+1):
#     if num==i*i :
#         print("the sqrt of this num is:",i)
#         break

# else:
#         import math
#         result=math.sqrt(num)
#         print("The sqrt of the" ,num, "is:",result)


#6.decimal to binary
# def bin_conv(n):
#     if n>1:
#         bin_conv(n//2)
#     print(n%2,end="")

# n=int(input("Enter the number:\n"))
# bin_conv(n)

# n=int(input("Enter a no\n"))
# b =bin(n)
# b=b.replace("0b","")
# print(b)
7#.
# n=input("enter a string\n")
# reverse=reversed(n)
# flip_text="".join(reverse)
# print(flip_text)

n=input("ty smt\n")
rev_text=n[:: -1]

print(rev_text)