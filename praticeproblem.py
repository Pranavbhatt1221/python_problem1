1# user input of name and age

name=input("what is your name!\n")
age=input("What is your age\n")

print("My name is",name,"& My age is",age)


2.#pyramid 
rows=5
for i in range(1,rows+1):
    print((" ",rows-i), end="")
    print("*",(2*i-1))
