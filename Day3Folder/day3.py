# Write all your codes for Day 3 here.
# REMEMBER to change main.py to import this file.
# You can COMMENT out the previous task before going on to the next task
# input:name bought num_pen pens.
name=input("What is your name? ")
num_pen=input("How many pens did you buy? ")
print(name+" bought "+num_pen+" pens.")
# input:num1 + num2 = ans
num1=int(input("What is the first number to add/minus/times/divide? "))
num2=int(input("What is the second number to add/minus/times/divide? "))
print(str(num1)+" + "+str(num2)+" = "+str(num1+num2))
print(str(num1)+" - "+str(num2)+" = "+str(num1-num2))
print(str(num1)+" * "+str(num2)+" = "+str(num1*num2))
print(str(num1)+" / "+str(num2)+" = "+str(num1/num2))
# if&else
age1=int(input("How old is PersonA? "))
age2=int(input("How old is PersonB? "))
if age1 > age2:
    print("PersonA is older than PersonB.")
else:
    print ("PersonA is not older than PersonB")
#passworrd
password="mehmehmeh"
userPass=input("What is the password? ")
if userPass==password:
    print("Access granted!:)")
else:
    print("Access denied!:(")
#3 tries password
password="passwordisthepassword"
userPass="meh"
tries=0
for i in range(3):
    if userPass != password:
        userPass = input("What is the password? ")
    if tries < 3:
            if userPass == password:
                print("Access granted!:)")
                name=input("What is you name? ")
                print("Welcome "+name)
            else:
                print("Access denied!:(")
                tries=tries+1
if tries >= 3:
    print("System has locked out!:(")
#addition quiz
import random
num1=random.randint(1, 100)
num2=random.randint(1, 100)
ans=num1+num2
sum=int(input("What is " + str(num1) + " + " + str(num2) + "? "))
if sum == ans:
    print("You are correct!:)")
else:
    print("Womp womp. You got it wrong. Go see the principal for not paying attention in class.:(")