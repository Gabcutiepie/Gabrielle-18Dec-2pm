# Write all your codes for Day 4 here.
# REMEMBER to change main.py to import this file.
# You can COMMENT out the previous task before going on to the next task

#counter1=0
#while counter1 <10:
#    print(counter1)
#    counter1=counter1+1

#counter2=5
#while counter2 <33:
#    print(counter2)
#    counter2=counter2+1

#counter3=50
#while counter3 >0:
#    print(counter3)
#    counter3=counter3+ -1

riddleAns="meh"
userAns = input("What sound does a sheep make? ")
counter=1
while userAns != riddleAns:
    if counter ==5:
        print("Hint: The answer has 3 words.")
    if counter ==10:
        print("Hint: The answer starts with m.")
    if counter ==15:
        print("Hint: The answer is me_.")   
    userAns=input("What sound does a sheep make? ")
    counter=counter+1
print("You are correct! You took " + str(counter) + " attempts.")

riddleAns="SEE O DOUBLE YOU"
userAns = input("How do you spell COW in thirteen letters? ")
counter=1
while userAns != riddleAns:
    if counter ==5:
        print("Hint: All the words are capitalized.")
    if counter ==10:
        print("Hint: There are 4 words.")
    if counter ==15:
        print("Hint: The answer starts with SEE _ ______ ___.")
    if counter ==20:
        print("Hint: The answer starts with SEE O ______ ___.")
    if counter ==25:
        print("Hint: The answer starts with SEE O DOUBLE ___.")
    if counter ==30:
        print("The answer is SEE O DOUBLE YOU.")
    userAns=input("How do you spell COW in thirteen letters? ")
    counter=counter+1
print("You are correct! You took " + str(counter) + " attempts.")






