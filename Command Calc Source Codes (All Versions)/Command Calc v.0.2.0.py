#Command Calc

#Welcome
txt1='''WELCOME TO COMMAND CALC
- A Calculator that Runs on your "Command Prompt".
                 v-0.2.0
                 
Powered by Python            ©Illektron Softwares

'''

print(txt1)

#Instructions

txt2='''
Instructions:-

i). Enter a Number in Integer Form or Decimal Form.
ii). Enter the Required Operation.

     For Operations,

       Addition:'+'           Subtraction:'-'
       Multiplication:'x'     Division:'/'

iii). To Execute the Operation press '=' in the Operation section.
iv). Do not Forget to Press 'ENTER' Everytime you Enter an Input.
v). Restart the Program for Another Calculation.

IMPORTANT NOTICE:-

   *The 'Pi' Symbol is not Recognized. Please Enter 3.14 for 'Pi.'*
   **Scientific Terms are Not Available.**
   ***The Required Answer Will be Shown in Decimal Format.***
   ****If the Calculator Fails to Provide the Solution on Command Prompt,
      please Install Python and Run it on IDLE****
GOOD LUCK!!!

'''
txt3='''
GOOD LUCK!!!

'''
guide=input("Do you Want to View Instructions? (Yes/No):")

if guide=='yes':
  print(txt2)
  
elif guide=='Yes':
    print(txt2)

elif guide=='YES':
    print(txt2)
    
elif guide=='no':
    print(txt3)
    
elif guide=='No':
    print(txt3)
    
elif guide=='NO':
    print(txt3)
    
else:
    print("INVALID ANSWER.... Please Restart the Program to Continue")
    
#Main Program

res=float(input("Enter a Number: "))

while True:
     o=input("Enter Operator: ")

     if o=='=':
       print("Solution:",res)
       print('''
Please Restart for Another Calculation

      Thanks For Using Our App''')
       break

     num=float(input("Enter a Number: "))

     if o=='+':
       res += num

     elif o=='-':
       res -= num

     elif o=='x':
         res *= num

     elif o=='*':
         res *= num


     elif o=='/':
          if num != 0:
            res /= num

          else:
              print("Not Defined")

     else:
         print("Invalid operator.... Please Restart the Program to Continue")
         break
