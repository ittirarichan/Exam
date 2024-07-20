# 13. Create a calculator using functions and modules 
from Exam.calculator.addition import *
from Exam.calculator.multiplication import *
from Exam.calculator.substraction import *
from Exam.calculator.division import *

a=[]
while True:
    print("\n1. Addition \n2. Multiplication \n3. Substraction \n4. Division")
    ch=int(input("\nEnter a choice : "))
    if ch==1:
        add(a)
    elif ch==2:
        multiplication(a)
    elif ch==3:
        substraction(a)
    elif ch==4:
        division(a)
    else:
        print("\nEnter a valid choice : ")