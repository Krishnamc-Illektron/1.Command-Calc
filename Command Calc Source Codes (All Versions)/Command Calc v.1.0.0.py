#Command Calc

#Welcome
txt1='''WELCOME TO COMMAND CALC
- A Calculator that Runs on your "Command Prompt".
                 v-1.0.0
                 
Powered by Python            ©Illektron Softwares

'''

print(txt1)

#General instructions


txt2='''
General Instructions:-
  i). To Execute the Operation press '=' in the Operation section.
  ii). Do not Forget to Press 'ENTER' Everytime you Enter an Input.
  iii). Restart the Program for Another Calculation.

IMPORTANT NOTICE:-

   *The 'Pi' Symbol is not Recognized. Please Enter 3.14 for 'Pi.'*
   **Scientific Terms are Not Available.**
   ***The Required Answer Will be Shown in Decimal Format.***
   ****If the Calculator Fails to Provide the Solution on Command Prompt,
       please Install Python and Run it on IDLE****
           
'''

txt2_1='''
Thanks... Please Proceed.
'''

prompt=input('''Type 'Start' or Type 'Infostart' to view General instructions and start
Your Answer: ''')

if prompt=='start':
  print(txt2_1)
  
elif prompt=='Start':
    print(txt2_1)

elif prompt=='START':
    print(txt2_1)
    
elif prompt=='INFOSTART':
    print(txt2)

elif prompt=='infostart':
    print(txt2)
    
elif prompt=='Infostart':
    print(txt2)

elif prompt=='InfoStart':
    print(txt2)
    
else:
    print("System Would Consider it as 'Start'. ",txt2_1)

#Import Functions

import math
import statistics

#Choose Modes

print('''Please select your Mode:-

1.Basic Calculator.
2.Exponential Operations.
3.Factorials.
4.Basic Trigonometry.
5.Statistics.

''')
mode=input("Enter the Mode: ")
      
if mode=='1':
      
  #Instructions 1

   txt3='''
   Instructions:-

   i). Enter a Number in Integer Form or Decimal Form.
   ii). Enter the Required Operation.

        For Operations,

         Addition:'+'           Subtraction:'-'
         Multiplication:'x'     Division:'/'

   GOOD LUCK!!!

   '''
   txt4='''
   GOOD LUCK!!!

   '''
   
   guide=input("Do you Want to View Instructions? (Yes/No): ")

   if guide=='yes':
     print(txt3)
  
   elif guide=='Yes':
       print(txt3)

   elif guide=='YES':
       print(txt3)
    
   elif guide=='no':
       print(txt4)
    
   elif guide=='No':
       print(txt4)
    
   elif guide=='NO':
       print(txt4)
    
   else:
       print("System Would Consider it as 'NO'. ",txt4)
    
   #Main Program 1

   res=float(input("Enter a Number: "))

   while True:
        o=input("Enter Operator: ")

        if o=='=':
          print("Solution:",res)
          print('''
          Please Restart for Another Calculation.

               Thanks For Using Our App.''')
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
                print("Not Defined...")

        else:
            print("Invalid operator.... Please Restart the Program to Continue.")
            break

elif mode=='2':

    #Choice 1
    print('''
Enter the Type of Operation:-

1.Square and Cube Roots.
2.Raise to Exponential Form.

    ''')
    
    mode1=input("Enter Your Choice: ")

    if mode1=='1':
       #Instructions 2
      
       txt5='''Instructions:-

       For Operations,

          Square Root:'sqrt'
          Cube Root:'cbrt'
     
       GOOD LUCK!!!!

       '''
       txt6='''
       GOOD LUCK!!!

   '''
       guide1=input("Do you Want to View Instructions? (Yes/No): ")

       if guide1=='yes':
         print(txt5)
  
       elif guide1=='Yes':
           print(txt5)

       elif guide1=='YES':
           print(txt5)
    
       elif guide1=='no':
           print(txt6)
    
       elif guide1=='No':
           print(txt6)
    
       elif guide1=='NO':
           print(txt6)
     
       else:
           print("System Would Consider it as 'NO'. ",txt6)
           

       #Main Program 2
        
       num1=int(input("Enter the number: "))
       o1=input("Enter the operation: ")

       if o1=='sqrt':
         print(math.sqrt(num1))
        
       elif o1=='cbrt':
           print(math.cbrt(num1))

       else:
           print("Invalid operator.... Please Restart the Program to Continue.")

       print('''
       Please Restart for Another Calculation.

            Thanks For Using Our App.''')
       

    elif mode1=='2':

        #Instructions 3

        txt7='''Instructions:-

        Enter the Value of Number and Power to the
        Respective Directories.

        GOOD LUCK!!!!

        '''

        txt8='''
        GOOD LUCK!!!!

        '''
        
        guide2=input("Do you Want to View Instructions? (Yes/No): ")

        if guide2=='yes':
          print(txt7)
  
        elif guide2=='Yes':
            print(txt7)

        elif guide2=='YES':
            print(txt7)
    
        elif guide2=='no':
            print(txt8)
    
        elif guide2=='No':
            print(txt8)
    
        elif guide2=='NO':
            print(txt8)
     
        else:
            print("System Would Consider it as 'NO' ",txt8)
            
        #Main Program 3
            
        num2=float(input("Enter the Number: "))
        pwr1=float(input("Enter the Power: "))
          
        print("Solution:",pow(num2,pwr1))
        print('''
        Please Restart for Another Calculation.

            Thanks For Using Our App.''')

    else:
        print("INVALID CHOICE.... Please Restart the Program to Continue.")
      
elif mode=='3':

    #Instructions 4

    txt9='''Instructions:-

    Enter the Number to Find its Factorial.

    GOOD LUCK!!!!

     '''

    txt10='''
    GOOD LUCK!!!!

        '''
    guide3=input("Do you Want to View Instructions? (Yes/No): ")

    if guide3=='yes':
      print(txt9)
  
    elif guide3=='Yes':
        print(txt9)

    elif guide3=='YES':
        print(txt9)
    
    elif guide3=='no':
        print(txt10)
    
    elif guide3=='No':
        print(txt10)
    
    elif guide3=='NO':
        print(txt10)
     
    else:
        print("System Would Consider it as 'NO'. ",txt10)
            
    #Main Program 4
        
    num3=int(input("Enter the Number: "))
    print("Factorial of",num3,":",math.factorial(num3))
    print('''
    Please Restart for Another Calculation.

       Thanks For Using Our App.''')

elif mode=='4':

    #Instructions 4

    txt11='''Instructions:-

    i)Enter the Angle
    ii)for operations,

         Type Sin, Cos or Tan in the Operation Section.
      
    IMPORTANT NOTICE:-

        *The Solutions shown Below are in Decimal format.*
 
    GOOD LUCK!!!!

     '''

    txt12='''
    GOOD LUCK!!!!

        '''
    
    guide4=input("Do you Want to View Instructions? (Yes/No): ")

    if guide4=='yes':
      print(txt11)
  
    elif guide4=='Yes':
        print(txt11)

    elif guide4=='YES':
        print(txt11)
    
    elif guide4=='no':
        print(txt12)
    
    elif guide4=='No':
        print(txt12)
    
    elif guide4=='NO':
        print(txt12)
     
    else:
        print("System Would Consider it as 'NO'. ",txt12)
            
    #Main Program 4

    num4=float(input("Enter the Angle: "))
    o2=input("Enter the Trigonometric Function: ")

    if o2=='sin':
      print("Sin",num4,":",math.sin(num4))

    elif o2=='SIN':
        print("Sin",num4,":",math.sin(num4))

        
    elif o2=='Sin':
        print("Sin",num4,":",math.sin(num4))

    elif o2=='COS':
        print("Cos",num4,":",math.cos(num4))

    elif o2=='Cos':
        print("Cos",num4,":",math.cos(num4))

    elif o2=='cos':
        print("Cos",num4,":",math.cos(num4))
        
    elif o2=='TAN':
        print("Tan",num4,":",math.tan(num4))

    elif o2=='Tan':
        print("Tan",num4,":",math.tan(num4))

    elif o2=='tan':
        print("Tan",num4,":",math.tan(num4))

    else:
        print("Invalid operator.... Please Restart the Program to Continue.")

    print('''
       Please Restart for Another Calculation.

            Thanks For Using Our App.''')

elif mode=='5':

    #Instructions 5

    txt13='''Instructions:-

    i)Enter the Numbers as in Format:
           2 4 56.4 234 
    ii)for operations,

         Type Mean, Median, Mode or Standard Deviation in the Operation Section.

         
    IMPORTANT NOTICE:-

        *Please Note that this statistics Mode is Only For Raw Data.*
                  eg:- mean for 6,5,3,7,28,4,34,5,11,56.

        
    GOOD LUCK!!!!

     '''

    txt14='''
    GOOD LUCK!!!!

        '''
    
    guide5=input("Do you Want to View Instructions? (Yes/No): ")

    if guide5=='yes':
      print(txt13)
  
    elif guide5=='Yes':
        print(txt13)

    elif guide5=='YES':
        print(txt13)
    
    elif guide5=='no':
        print(txt14)
    
    elif guide5=='No':
        print(txt14)
    
    elif guide5=='NO':
        print(txt14)
     
    else:
        print("System Would Consider it as 'NO'. ",txt14)
            
    #Main Program 5

    statinp=input("Enter the Data With Spaces: ")
    statdata=list(map(float, statinp.split()))
    o3=input("Enter the Operation: ")

    if o3=='mean':
      print("Mean: ",statistics.mean(statdata))

    elif o3=='Mean':
        print("Mean: ",statistics.mean(statdata))
        
    elif o3=='MEAN':
        print("Mean: ",statistics.mean(statdata))

    elif o3=='MEDIAN':
        print("Median: ",statistics.median(statdata))

    elif o3=='median':
        print("Median: ",statistics.median(statdata))

    elif o3=='Median':
        print("Median: ",statistics.median(statdata))
        
    elif o3=='Mode':
        print("Mode: ",statistics.mode(statdata))

    elif o3=='MODE':
        print("Mode: ",statistics.mode(statdata))

    elif o3=='mode':
        print("Mode: ",statistics.mode(statdata))

    elif o3=='standard deviation':
        print("Standard Deviation: ",statistics.stdev(statdata))
        
    elif o3=='Standard Deviation':
        print("Standard Deviation: ",statistics.stdev(statdata))
        
    elif o3=='STANDARD DEVIATION':
        print("Standard Deviation: ",statistics.stdev(statdata))

    elif o3=='standarddeviation':
        print("Standard Deviation: ",statistics.stdev(statdata))
        
    elif o3=='StandardDeviation':
        print("Standard Deviation: ",statistics.stdev(statdata))
        
    elif o3=='STANDARDDEVIATION':
        print("Standard Deviation: ",statistics.stdev(statdata))


    else:
        print("Invalid operator.... Please Restart the Program to Continue.")

    print('''
       Please Restart for Another Calculation.

            Thanks For Using Our App.''')

else:
    print("INVALID CHOICE.... Please Restart the Program to Continue.")


