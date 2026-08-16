# Student result System 

Student = input ("Enter your name: ")
Roll_no = input("Enter your roll number: ")

English_marks = int(input("Enter your English marks: "))
Mathematics_marks = int(input("Enter your Mathematics marks: "))
Physics_marks = int(input("Enter your Physics marks: "))
Chemistry_marks = int(input("Enter your Chemistry marks: "))
ComputerScience_marks = int(input("Enter your ComputerScience marks: "))

list = []

list.append(English_marks)
list.append(Mathematics_marks)
list.append(Physics_marks)
list.append(Chemistry_marks)
list.append(ComputerScience_marks)

Total = sum(list)
percentage = (Total/500)*100

print("\n\n----------------------------------------- Student Result ---------------------------------------------")
print("\n\tName\t\t\t: ",Student)
print("\tRoll No.\t\t: ",Roll_no)
print("\n--------------------------------------------- Marks --------------------------------------------------")
print("\n\tEnglish\t\t\t: ",English_marks)
print("\n\tMathematics\t\t: ",Mathematics_marks)
print("\n\tPhysics\t\t\t: ",Physics_marks)
print("\n\tChemistry\t\t: ",Chemistry_marks)
print("\n\tComputerScience\t\t: ",ComputerScience_marks)

print("\n------------------------------------------------------------------------------------------------------")
print("\n\tTotal\t\t\t: ",Total)
print("\n\tPercentage\t\t: ",percentage)

if(English_marks>100 or Mathematics_marks>100 or Physics_marks>100 or Chemistry_marks>100 or ComputerScience_marks>100 or English_marks<0 or Mathematics_marks<0 or Physics_marks<0 or Chemistry_marks<0 or ComputerScience_marks<0):
    print("\n\tInvalid marks entered please check thge marks again")
    
elif(percentage>=90 and percentage<= 100 and English_marks>=35 and Mathematics_marks>=35 and Physics_marks>=35 and Chemistry_marks>=35 and ComputerScience_marks>=35):
    print("\n\tGrade\t\t\t:  A+")
    print("\n\tResult\t\t\t:  Pass")

elif(percentage>=80 and percentage<= 89 and English_marks>=35 and Mathematics_marks>=35 and Physics_marks>=35 and Chemistry_marks>=35 and ComputerScience_marks>=35):
    print("\n\tGrade\t\t\t:  A")
    print("\n\tResult\t\t\t:  Pass")

elif(percentage>=70 and percentage<= 79 and English_marks>=35 and Mathematics_marks>=35 and Physics_marks>=35 and Chemistry_marks>=35 and ComputerScience_marks>=35):
    print("\n\tGrade\t\t\t:  B")
    print("\n\tResult\t\t\t:  Pass")

elif(percentage>=60 and percentage<= 69 and English_marks>=35 and Mathematics_marks>=35 and Physics_marks>=35 and Chemistry_marks>=35 and ComputerScience_marks>=35):
    print("\n\tGrade\t\t\t:  C")
    print("\n\tResult\t\t\t:  Pass")
    
elif(percentage>=40 and percentage<= 59 and English_marks>=35 and Mathematics_marks>=35 and Physics_marks>=35 and Chemistry_marks>=35 and ComputerScience_marks>=35):
    print("\n\tGrade\t\t\t:  D")
    print("\n\tResult\t\t\t:  Pass")

elif(percentage<40 and English_marks>=35 and Mathematics_marks>=35 and Physics_marks>=35 and Chemistry_marks>=35 and ComputerScience_marks>=35):
    print("\n\tGrade\t\t\t:  F")
    print("\n\tResult\t\t\t:  Fail")

else:
    print("\n\tGrade\t\t\t:  F")
    print("\n\tReason\t\t\t:  You had not clear the cut off of 35 marks in a perticular subject")
    print("\n\tResult\t\t\t:  Fail")

print("\n------------------------------------------------------------------------------------------------------")
    
    
    

