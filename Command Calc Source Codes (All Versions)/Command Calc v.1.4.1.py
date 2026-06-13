#Project Command Calc

#Welcome Screen
welcome='''
==================================================================================
                               COMMAND CALC
                                  v1.4.1
----------------------------------------------------------------------------------
                 A Multi-Feature Command Line Calculator Tool
----------------------------------------------------------------------------------
                      Developed by ©Illektron Softwares
==================================================================================

'''

#General instructions

inst='''

  i). Follow the Prompted Steps and Instructions Carefully to Proceed Anywhere.
  ii). Do not Forget to Press 'ENTER' Everytime you Enter an Input.
  iii). Press ENTER after each Prompt in Loading Screens.
  iv). Users do not Have to Worry Because the App is easy to Use... Patience is Key.

*~IMPORTANT NOTICE~*

   *Scientific Terms are Not Available.*
   **The Required Answer Will be Shown in Decimal Format.**
   
__________________________________________________________________________________        
'''

thx='''
Hello... Please Proceed.
'''

#Import Functions

import math
import statistics
import time
import os
import random

#Some Repeating Codes

#Quotes

qts1=[
"'Success is the sum of small efforts, repeated day in and day out.'",
"'Believe in yourself and all that you are.'",
"'The way to get started is to quit talking and begin doing.'",
"'There is no substitute for hard work.'",
"'Failure is the opportunity to begin again more intelligently.'",
"'Success is not final, failure is not fatal: it is the courage to continue that counts.'",
"'It always seems impossible until it’s done.'",
"'The wound is the place where the light enters you.'",
"'Don’t watch the clock; do what it does. Keep studying.'",
"'There is no elevator to success. You have to take the stairs.'",
"'Every focused hour is building a life you cannot see yet.'",
"'Only I can change my life. No one can do it for me.'",
"'In a world where you can be anything, be kind.'",
"'The power of imagination makes us infinite.'",
"'Try not to become a man of success, but a man of value.'"
]

#dialogues

rep1='\n GOOD LUCK!!! \n___________________________________________________________________________________ \n'

rep2='''\n Software Will Consider it as 'NO'
   GOOD LUCK!!!.
___________________________________________________________________________________
   '''

rep3='\n__________________________________________________________\n'

rep6="\n Thank you.\n"

rep7='\n Loading ........\n\n'

rep8="\n Thank You for Using Command Calc........\n================================================================================== "

rep9="\n Press ENTER to Continue... \n==================================================================================\n"

rep10='\n=================================================\n '

rep11='~~~~~~~~~~~~~~~~~~~~~~ COMMAND CALC ~~~~~~~~~~~~~~~~~~~~~~'

#Inputs

inp1=" \n Do you Want to View Instructions? ((Yes/y)/(No/n)): "

inp2="________________________________________________________\n \n Do you want to Continue?((Yes/y)/(No/n): "

#Validity

val1="\n INVALID DIMENSIONS.... Please Try again.\n__________________________________________________________\n"

val2='\n INVALID OPERATOR / Value.... Please Try Again.\n__________________________________________________________\n'

val3='\n INVALID CHOICE.... Please Try Again.\n__________________________________________________________\n'
#UX Functions

#1.Clean
#============================================================================================================

def clean():
   os.system('cls' if os.name=='nt' else 'clear')

#2.Location
#============================================================================================================
            
def pr(loc):
   print(rep11)       
   print(loc)


#2.Transition
#============================================================================================================

def trans():
   clean()
   print(rep11)
   print(rep7)
   print(random.choice(qts1),"\n")
   time.sleep(1.5)
   input(rep9)
   clean()

#Sub functions

#1.Guide
#============================================================================================================

def guide(txt):

   guide=input(inp1).strip().lower()

   if guide=='yes' or guide=='y':
     print(txt)
     input(rep9)
     clean()
  
   elif guide=='no' or guide=='n':
       print(rep1)
       time.sleep(1.5)
       clean()
   
   else:
       print(rep2)
       time.sleep(1.5)
       clean()       

#2.Continue
#============================================================================================================

def cont():
    while True:

         cont=input(inp2).strip().lower()

         if cont=='yes' or cont=='y':
            clean()
            return False
            

         elif cont=='no' or cont=='n':
              print(rep6)
              return True

         else:
              print(val2)
              continue

#Main Functions

#0.Main Menu.
#============================================================================================================
def mainguide():
   loc='''==========================================================
                  GENERAL INSTRUCTIONS
=========================================================='''
   
   pr(loc)
   print(inst)

#1.Basic Calculator.
#============================================================================================================

def basiccalc():
   #Instructions 1

   loc='''==========================================================
                   BASIC CALCULATOR
=========================================================='''

   pr(loc)

   txt='''___________________________________________________________________________________

Instructions:-

    Type the Question in the Form of Expression.

IMPORTANT NOTICE:-

    *Note that Variables DO NOT Work*
    **Pi Value is NOT Available.**
    ***Only Paranthests '()' is Available.***

        For Operations,

         Addition:'+'                 Subtraction:'-'
         Multiplication:'x' or '*'    Division:'/'
         Modulus:'%'

         EQUALS '=' is not Compulsory

   GOOD LUCK!!!
___________________________________________________________________________________
   '''
   
   guide(txt)
   
   #Main Program 1

   res=0
   accept1="1234567890=+-*xX/%(). "
   while True:
        pr(loc)
        expr1=input("Enter Expression: ")
        expr1=expr1.replace('x','*')
        expr1=expr1.replace('X','*')
        expr1=expr1.replace('=',' ')
      
        if not all(ch in accept1 for ch in expr1):
          print(val2)
          time.sleep(1.5)
          clean()
          continue
        
        try:
           res=eval(expr1, {"__builtins__": None}, {})
           print(rep10,"Solution: ",res,rep10)

        except (SyntaxError,TypeError):
              print(val2)
              time.sleep(1.5)
              clean()
              continue

        except ZeroDivisionError:
              print('\nCannot Divide by Zero(0)....',rep3)
              time.sleep(1.5)
              clean()
              continue

        except OverflowError:
              print('Sorry....SOLUTION TOO LONG....',rep3)
              time.sleep(1.5)
              clean()
              continue

        if cont():
          return
             
#2.Exponential Operations.
#============================================================================================================

def expops():

   loc='''==========================================================
                 EXPONENTIAL OPERATIONS
=========================================================='''

   pr(loc)

   while True:
  
        #Choice 1
  
        print(''' ________________________________________________________
|             Enter the Type of Operation                |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|                                                        |
|   1.   -|-     Square and Cube Roots                   |
|   2.   -|-     Raise to Exponential Form.              |
|   r.   -|-     Return to Main Menu.                    |  
|________________________________________________________|
''')

        mode1=input("Enter Your Choice: ").strip()

        if mode1=='1':
          clean()
           
          loc='''==========================================================
                 SQUARE AND CUBE ROOTS
=========================================================='''

          pr(loc)
          
          #Instructions 2
      
          txt='''___________________________________________________________________________________

Instructions:-

       For Operations,

          Square Root:'sqrt'
          Cube Root:'cbrt'
     
       GOOD LUCK!!!!
___________________________________________________________________________________
       '''

          guide(txt)
           
          #Main Program 2
          while True:
               pr(loc)
               
               try:
                  num1 = int(input("Enter the number: "))
               except ValueError:
                     print(val2)
                     time.sleep(1.5)
                     clean()
                     continue
             
               o1=input("Enter the operation: ")

               if o1.strip().lower()=='sqrt':
                  
                 if num1 < 0:
                   print("\n Square Root of negative numbers is not real.\n")
                   time.sleep(1.5)
                   clean()
                   continue
                  
                 else:
                     print(rep10,"Square Root: ",math.sqrt(num1),rep10)

               elif o1.strip().lower()=='cbrt':
                   print(rep10,"Cube Root: ",num1**(1/3),rep10)
         
               else:
                   print(val2)
                   time.sleep(1.5)
                   clean()
                   continue

               if cont():
                 return

        elif mode1=='2':
            clean()

            loc='''==========================================================
                RAISE TO EXPONENTIAL FORM
=========================================================='''

            pr(loc)

            #Instructions 2_2

            txt='''___________________________________________________________________________________

Instructions:-

        Enter the Value of Number and Power to the
        Respective Directories.

        GOOD LUCK!!!!
___________________________________________________________________________________
        '''
        
            guide(txt)
        
            #Main Program 2_2

            while True:
               
                 pr(loc)
            
                 try:
                    num2=float(input("Enter the Number: "))
                
                 except ValueError:
                       print(val2)
                       time.sleep(1.5)
                       clean()
                       continue
                 try:     
                    pwr1=float(input("Enter the Power: "))
              
                 except ValueError:
                       print(val2)
                       time.sleep(1.5)
                       clean()
                       continue

                 if num2==0 and pwr1<0:
                     print(rep10,"Solution: Not Defined",rep10)

                     if cont():
                       return
          
                 print(rep10,"Solution: ",pow(num2,pwr1),rep10)

                 if cont():
                   return

                        
        elif mode1.lower()=='r':
            return

        else:
            print(val3)
            time.sleep(1.5)
            clean()
            continue
      
#3.Factorials.
#============================================================================================================

def factorial():

    #Instructions 3

    loc='''==========================================================
                      FACTORIALS
=========================================================='''

    pr(loc)

    txt='''___________________________________________________________________________________

Instructions:-

    Enter the Number to Find its Factorial.

    GOOD LUCK!!!!
___________________________________________________________________________________
     '''

    guide(txt)
            
    #Main Program 3
    while True:
       
         pr(loc)
         
         try:
            num3 = int(input("Enter the Number: "))
       
            if num3 < 0:
              print("\nFactorials not defined for negative numbers...",rep3)
              time.sleep(1.5)
              clean()
              continue
         
            elif num3 > 100:
                print("\nNumber too large......",rep3)
                time.sleep(1.5)
                clean()
                continue
           
            else:
                print(rep10,"Solution: ",math.factorial(num3),rep10)
        
         except ValueError:
               print("\nEnter Integers Only...",rep3)
               time.sleep(1.5)
               clean()
               continue

         if cont():
           return
                        
#4.Basic Trigonometry.
#============================================================================================================

def trigonometry():
    #Instructions 4

    loc='''==========================================================
                      TRIGONOMETRY
=========================================================='''

    pr(loc)
   
    txt='''___________________________________________________________________________________

Instructions:-

    i)Enter the Angle
    ii)for operations,

         Type Sin, Cos, Tan, Cosec, Sec or Cot in the Operation Section.
      
    IMPORTANT NOTICE:-

        *The Solutions shown Below are in Decimal Format and Not
                in Rational Numbers.*
 
    GOOD LUCK!!!!
___________________________________________________________________________________
     '''
    
    guide(txt)
            
    #Main Program 4

    while True:
       
         pr(loc)
         
         try:
            num4=float(input("Enter the Angle: "))

         except ValueError:
               print(val2)
               time.sleep(1.5)
               clean()
               continue
              
         ang=math.radians(num4)

         o2=input("Enter the Trigonometric Function: ")

         if o2.strip().lower()=='sin':
           print(rep10,"Sin",num4,":",math.sin(ang),rep10)

         elif o2.strip().lower()=='cos':
             print(rep10,"Cos",num4,":",math.cos(ang),rep10)
        
         elif o2.strip().lower()=='tan':
             if round(math.cos(ang), 10)==0:
               print(rep10,"Not Defined",rep10)
             else:
                 print(rep10,"Tan",num4,":",math.tan(ang),rep10)
   
         elif o2.strip().lower()=='cosec':
             if round(math.sin(ang), 10)==0:
                print(rep10,"Not Defined",rep10)
             else:
                 print(rep10,"Cosec",num4,":",1/math.sin(ang),rep10)

         elif o2.strip().lower()=='sec':
             if round(math.cos(ang), 10)==0:
               print(rep10,"Not Defined",rep10)
             else:
                 print(rep10,"Sec",num4,":",1/math.cos(ang),rep10)

         elif o2.strip().lower()=='cot':
             if round(math.tan(ang), 10)==0:
               print(rep10,"Not Defined",rep10)
             else:
                 print(rep10,"Cot",num4,":",1/math.tan(ang),rep10)

         else:
             print(val2)
             time.sleep(1.5)
             clean()
             continue

         if cont():
           return
                
#5.Statistics(Ungrouped Data).
#============================================================================================================

def stats():
    #Instructions 5

    loc='''==========================================================
                      STATISTICS
=========================================================='''

    pr(loc)
   
    txt='''___________________________________________________________________________________

Instructions:-

    i)Enter the Numbers as in Format:
           2 4 56.4 234 
    ii)for operations,

         Type Mean, Median, Mode, Variance or Standard Deviation
         in the Operation Section.

         
    IMPORTANT NOTICE:-

        *Please Note that this Statistics Mode is Only For Raw/Ungrouped Data.*
                  eg:- 6,5,3,7,28,4,34,5,11,56.
                  
    GOOD LUCK!!!!
___________________________________________________________________________________
     '''
    
    guide(txt)
            
    #Main Program 5

    while True:

         pr(loc)
      
         statinp=input("Enter the Data With Spaces: ")
         
         try:
            statdata = list(map(float, statinp.split()))
         except ValueError:
               print("Invalid data entered")
               time.sleep(1.5)
               clean()
               continue
          
         if len(statdata) == 0:
           print("No data entered")
           time.sleep(1.5)
           clean()
           continue
            
         else:
              o3=input("Enter the Operation: ").strip().lower()

              if o3=='mean':
                print(rep10,"Mean: ",statistics.mean(statdata),rep10)

              elif o3=='median':
                  print(rep10,"Median: ",statistics.median(statdata),rep10)
             
              elif o3=='mode':
                  print(rep10,"Mode: ",statistics.multimode(statdata),rep10)

              elif o3=='variance':
                  if len(statdata) < 2:
                    print(rep10,"Variance requires at least two values",rep10)
                  else:
                      print(rep10,"Variance: ",statistics.variance(statdata),rep10)

              elif o3=='standard deviation' or o3=='standarddeviation' or o3=='stdev':
                 
                  if len(statdata) < 2:
                    print(rep10,"Standard Deviation requires at least two values",rep10)
                    
                  else:
                      print(rep10,"Standard Deviation: ",statistics.stdev(statdata),rep10)
                  
              else:
                  print(val2)
                  time.sleep(1.5)
                  clean()
                  continue

         if cont():
           return

#6.Interests.
#============================================================================================================

def interests():

   loc='''==========================================================
                      INTERESTS
=========================================================='''

   pr(loc)
   
   while True:
     
    #Choice 2
         print(''' ________________________________________________________
|             Enter the Type of Operation                |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|                                                        |
|   1.   -|-     Simple Interest.                        |
|   2.   -|-     Compound Interest.                      |
|   r.   -|-     Return to Main Menu.                    |  
|________________________________________________________|
''')
    
         mode2=input("Enter Your Choice: ").strip()

         if mode2=='1':
            
           clean()
           
           loc='''==========================================================
                   SIMPLE INTEREST
=========================================================='''

           pr(loc)
      
           #Instructions 6_1

           txt='''___________________________________________________________________________________
Instructions:-

       i)Enter the Principal amount,rate of Interest and Time Period.
       ii)Press 'Enter' and wait for the Answers.
 
      GOOD LUCK!!!!
___________________________________________________________________________________
       '''

           guide(txt)

           while True:

                pr(loc)
            
                #main program 6_1
                try:
                   prinamt=float(input("Enter the Total Principal Amount: "))
                   rateint=float(input("Enter the Rate of Interest: "))
                   tp=float(input("Enter Time in years: "))
         
                except ValueError:
                      print(val2)
                      time.sleep(1.5)
                      clean()
                      continue

                if prinamt<=0 or tp<=0:
                  print(val2)
                  time.sleep(1.5)
                  clean()
                  continue
    
                simpint=(prinamt*rateint*tp)/100
                amtpay=prinamt+simpint

                print(rep10,"Simple Interest: ",simpint,rep10)
                print(rep10,"Amount Payable",amtpay,rep10)

                if cont():
                  return
                 
         elif mode2=='2':

             clean()

             loc='''==========================================================
                  COMPOUND INTEREST
=========================================================='''

             pr(loc)
        
             #Instructions 6_2

             txt='''___________________________________________________________________________________

Instructions:-

       i)Enter the Principle amount,rate of Interest and Time Period.
       ii)Press 'Enter' and wait for the Answers.
 
      GOOD LUCK!!!!
___________________________________________________________________________________
       '''
    
             guide(txt)

             while True:

                  pr(loc)
        
                  #main program 6_2
                  try:
                     prinamt1=float(input("Enter the Total Principle Amount: "))
                     rateint1=float(input("Enter the Rate of Interest: "))
                     tp1=float(input("Enter Time in years: "))
           
                  except ValueError:
                        print(val2)
                        time.sleep(1.5)
                        clean()
                        continue

                  if prinamt1<=0 or tp1<=0:
                    print(val2)
                    time.sleep(1.5)
                    clean()
                    continue

                  amtpay1=prinamt1*(1+rateint1/100)**tp1
                  compint=amtpay1-prinamt1
     
                  print(rep10,"Compound Interest: ",compint,rep10)
                  print(rep10,"Amount Payable",amtpay1,rep10)

                  if cont():
                    return

         elif mode2.lower()=='r':
             return

         else:
             print(val3)
             time.sleep(1.5)
             clean()
             continue

#7.Multiplication Table.
#============================================================================================================

def multable():

    clean()

    loc='''==========================================================
                 MULTIPLICATION TABLE
=========================================================='''

    pr(loc)
    #Instructions 7

    txt='''___________________________________________________________________________________

Instructions:-

    i)Enter the Number in the Number section and Maximum Multiplier.
    ii)Maximum multiplier- The Maximum Number of Lines to Generate in the Table.
    iii)The table will be Automatically generated in an Instant.

    GOOD LUCK!!!!
___________________________________________________________________________________
     '''
    
    guide(txt)
            
    #Main Program 7
    while True:

         pr(loc)
      
         try:    
            mul=int(input("Enter the Number for Generating table: "))
            mul1=int(input("Enter the Maximum Multiplier: "))

         except ValueError:
               print(val2)
               time.sleep(1.5)
               clean()
               continue

         print(rep10,"Multiplication Table for ",mul,''':
''')
         for i in range(1,mul1+1):
            table=mul*i
            print(mul,"x",i,"=",table)

         print(rep10)

         if cont():
           return
                
#8.Basic Geometry.
#============================================================================================================

def basicgeo():

    loc='''==========================================================
                   BASIC GEOMETRY
=========================================================='''

    pr(loc)

    #Instructions 8

    txt='''___________________________________________________________________________________

Instructions:-

    i).Follow the Instructions Given by the Software.
    ii).Enter Dimensions Wherever Required.

    IMPORTANT NOTICE:-

        *Please Ensure that the Measurements are of UNIFORM UNITS*
        **Please Check the Values Before Entering to Avoid Getting Wrong Answers**

    GOOD LUCK!!!!
___________________________________________________________________________________
     '''
    
    guide(txt)

    while True:

         pr(loc)

         print(''' ________________________________________________________
|             Please select the Dimension                |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|                                                        |
|   1.   -|-     Two Dimensional (2-D) Shapes.           |
|   2.   -|-     Three Dimensional (3-D) Shapes.         |
|   r.   -|-     Return to Main Menu.                    |  
|________________________________________________________|

''')

         mode3=input("Enter Your Choice: ").strip()

         if mode3=='1':

           clean()
           
           loc='''==========================================================
             TWO DIMENSIONAL (2-D) GEOMETRY
=========================================================='''

           while True:

                pr(loc)             

                print(''' ________________________________________________________
|             Please select your Requirement             |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|                                                        |
|   1.   -|-     Triangular Geometry.                    |
|   2.   -|-     Quadrilateral Geometry.                 |
|   3.   -|-     Circular Geometry.                      |  
|   b.   -|-     Go Back                                 |  
|________________________________________________________|

''')

                dim1=input("Enter your Requirement: ").strip()

                if dim1=='1':
                  clean()
                  
                  loc='''==========================================================
                 TRIANGULAR GEOMETRY
=========================================================='''

                  while True:

                       pr(loc)
                       
                       print(''' ________________________________________________________
|          Please select the Type of Triangle            |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|                                                        |
|   1.   -|-     Equilateral Triangle.                   |
|   2.   -|-     Isosceles Triangle.                     |
|   3.   -|-     Scalene Triangle.                       |  
|   b.   -|-     Go Back                                 |  
|________________________________________________________|


''')

                       tri=input("Enter the Type of Triangle: ").strip()
        
                       if tri=='1':
                         clean()

                         loc='''==========================================================
                  EQUILATERAL TRIANGLE
=========================================================='''

                         while True:

                              pr(loc)
                                                     
                              try:
                                 sideeqt=float(input("\nEnter the Length: "))

                              except ValueError:
                                    print(val1)
                                    time.sleep(1.5)
                                    clean()
                                    continue

                              if sideeqt<=0:
                                print(val1)
                                time.sleep(1.5)
                                clean()
                                continue
            
                              peeqt=sideeqt*3
                              semipeeqt=peeqt/2
                              areqt=math.sqrt(3)/4*sideeqt*sideeqt

                              print(rep10,"Perimeter: ",peeqt)
                              print("Semi Perimeter: ",semipeeqt)
                              print("Area: ",areqt,rep10)

                              if cont():
                                return
                       elif tri=='2':
                           clean()

                           loc='''==========================================================
                  ISOSCELES TRIANGLE
=========================================================='''

                           while True:

                                pr(loc)
          
                                sideorheight=input("\nIs Height given((Yes/y)/(No/n)): ").strip().lower()
            
                                if sideorheight=='yes' or sideorheight=='y':
                                  clean()
                                  
                                  while True:

                                       pr(loc)
                   
                                       try:
                                          base1=float(input("\nEnter the Base: "))
                                          height1=float(input("Enter the Height: "))

                                       except ValueError:
                                             print(val1)
                                             time.sleep(1.5)
                                             clean()
                                             continue

                                       if base1<=0 or height1<=0:
                                         print(val1)
                                         time.sleep(1.5)
                                         clean()
                                         continue
              
                                       eqside1=math.sqrt((base1/2)**2+height1**2)
                                       ariso1=0.5*base1*height1
                                       peiso1=base1+2*eqside1
                                       semipeiso1=peiso1/2
 
                                       print(rep10,"Equal Side Length: ",eqside1)
                                       print("Perimeter: ",peiso1)
                                       print("Semi Perimeter: ",semipeiso1)
                                       print("Area: ",ariso1,rep10)

                                       if cont():
                                         return
     
                                elif sideorheight=='no' or sideorheight=='n':
                                    clean()
                                    
                                    while True:

                                         pr(loc)

                                         try:
                                            eqside1=float(input("\nEnter the Equal Side Length: "))
                                            base1=float(input("Enter the Base: "))

                                         except ValueError:
                                               print(val1)
                                               time.sleep(1.5)
                                               clean()
                                               continue

                                         if eqside1<=base1/2:
                                           print(val1)
                                           time.sleep(1.5)
                                           clean()
                                           continue
     
                                         else:
                                             height1= math.sqrt(eqside1**2-(base1/2)**2)
                                             ariso1=0.5*base1*height1
                                             peiso1=base1+2*eqside1
                                             semipeiso1=peiso1/2

                                             print(rep10,"Height: ",height1)
                                             print("Perimeter: ",peiso1)
                                             print("Semi Perimeter: ",semipeiso1)
                                             print("Area: ",ariso1,rep10)

                                             if cont():
                                               return

                                else:
                                    print(val3)
                                    time.sleep(1.5)
                                    clean()
                                    continue

                       elif tri=='3':
                           clean()

                           loc='''==========================================================
                    SCALENE TRIANGLE
=========================================================='''

                           while True:

                                pr(loc)
                               
                                try:
                                   s1=float(input("\nEnter first Side: "))
                                   s2=float(input("Enter Second Side: "))
                                   s3=float(input("Enter Third Side: "))

                                except ValueError:
                                     print(val1)
                                     time.sleep(1.5)
                                     clean()
                                     continue

                                if s1+s2>s3 and s2+s3>s1 and s1+s3>s2:
              
                                   pesc=s1+s2+s3
                                   semipesc=pesc/2
                                   arsc = math.sqrt(semipesc*(semipesc-s1)*(semipesc-s2)*(semipesc-s3))

                                   print(rep10,"Perimeter: ",pesc)
                                   print("Semi-perimeter: ",semipesc)
                                   print("Area: ",arsc,rep10)

                                   if cont():
                                     return

                                else:
                                    print(val1)
                                    time.sleep(1.5)
                                    clean()
                                    continue

                       elif tri.lower()=="b":
                           trans()
                           break
                        
                       else:
                           print(val3)
                           continue

                elif dim1=='2':

                    clean()

                    loc='''==========================================================
                 QUADRILATERAL GEOMETRY
=========================================================='''

                    while True:

                         pr(loc)
                         
                         print(''' ________________________________________________________
|        Please select the Type of Quadrilateral         |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|                                                        |
|   1.   -|-     Square.                                 |
|   2.   -|-     Rectangle.                              |
|   3.   -|-     Parallelogram.                          |  
|   4.   -|-     Rhombus.                                |
|   5.   -|-     Trapezium / Trapezoid.                  |
|   6.   -|-     Kite.                                   |
|   b.   -|-     Go Back                                 |
|________________________________________________________|

''')

                         quad=input("Enter the Type of Quadrilateral: ").strip()
        
                         if quad=='1':
                           clean()

                           loc='''==========================================================
                       SQUARE
=========================================================='''

                           while True:
                                pr(loc)
                                
                                try:
                                   sidesq=float(input("\nEnter the Length: "))

                                except ValueError:
                                      print(val1)
                                      time.sleep(1.5)
                                      clean()
                                      continue

                                if sidesq<=0:
                                  print(val1)
                                  time.sleep(1.5)
                                  clean()
                                  continue
                                    
                                pesq=sidesq*4
                                arsq=sidesq*sidesq
     
                                print(rep10,"Perimeter: ",pesq)
                                print("Area: ",arsq,rep10)
     
                                if cont():
                                  return
          
                         elif quad=='2':
                             clean()

                             loc='''==========================================================
                       RECTANGLE
=========================================================='''

                             while True:
                                  pr(loc)
                                  
                                  try:
                                     rect1=float(input("\nEnter the Length: "))
                                     rect2=float(input("Enter the Breadth: "))

                                  except ValueError:
                                       print(val1)
                                       time.sleep(1.5)
                                       clean()
                                       continue

                                  if rect1<=0 or rect2<=0:
                                    print(val1)
                                    time.sleep(1.5)
                                    clean()
                                    continue
     
                                  perect=2*(rect1+rect2)
                                  arrect=rect1*rect2

                                  print(rep10,"Perimeter: ",perect)
                                  print("Area: ",arrect,rep10)

                                  if cont():
                                    return
            
                         elif quad=='3':
                             clean()
                             
                             loc='''==========================================================
                    PARALLELOGRAM
=========================================================='''

                             while True:
                                  pr(loc)
          
                                  try:
                                     parabase=float(input("\nEnter the Base: "))
                                     paraside=float(input("Enter the Side Length: "))

                                  except ValueError:
                                        print(val1)
                                        time.sleep(1.5)
                                        clean()
                                        continue

                                  if parabase<=0 or paraside<=0:
                                    print(val1)
                                    time.sleep(1.5)
                                    clean()
                                    continue

                                  pepara=2*(parabase+paraside)

                                  hinfo=input("\nDo you Know the Height?((Yes/y)/(No/n)): ").strip().lower()

                                  if hinfo=='yes' or hinfo=='y':
              
                                    try:
                                       paraheight=float(input("\nEnter the Height: "))
     
                                    except ValueError:
                                          print(val1)
                                          time.sleep(1.5)
                                          clean()
                                          continue

                                    if paraheight<=0:
                                       print(val1)
                                       time.sleep(1.5)
                                       clean()
                                       continue

                                    paraarea=parabase*paraheight
                                    print(rep10,"Perimeter: ",pepara,"\n  Area: ",paraarea,rep10)

                                    if cont():
                                      return 
                
                                  elif hinfo=='no' or hinfo=='n':
                                             
                                      print(rep10,"Perimeter: ",pepara,"\n  Area: Calculation requires Height...... ",rep10)
                                      
                                      if cont():
                                        return
                                            
                                  else:
                                      print(val3)
                                      time.sleep(1.5)
                                      clean()
                                      continue
                                 
                         elif quad=='4':
                             clean()

                             loc='''==========================================================
                        RHOMBUS
=========================================================='''

                             while True:
                                  pr(loc)
                                  
                                  try:
                                     rhombside=float(input("Enter the Side Length: "))

                                  except ValueError:
                                        print(val1)
                                        time.sleep(1.5)
                                        clean()
                                        continue

                                  if rhombside<=0:
                                     print(val1)
                                     time.sleep(1.5)
                                     clean()
                                     continue

                                  perhomb=4*rhombside

                                  try:
                                     hinfo1=input("Do you Know the Height or Diagonals?(H -(Height) / D -(Diagonals)) / No: ").strip().lower()

                                  except ValueError:
                                        print(val1)
                                        time.sleep(1.5)
                                        clean()
                                        continue

                                  if hinfo1=='h':

                                    try:
                                       rhombheight=float(input("\nEnter the Height: "))

                                    except ValueError:
                                          print(val1)
                                          time.sleep(1.5)
                                          clean()
                                          continue

                                    if rhombheight<=0:
                                      print(val1)
                                      time.sleep(1.5)
                                      clean()
                                      continue
                    
                                    arrhomb=rhombside*rhombheight
                                    print(rep10,"Perimeter: ",perhomb,"\n  Area: ",arrhomb,rep10)
     
                                    if cont():
                                      return
                
                                  elif hinfo1=='d':
                          
                                      try:
                                         diagrhomb1=float(input("Enter the First Diagonal: "))
                                         diagrhomb2=float(input("Enter the Second Diagonal: "))

                                      except ValueError:
                                            print(val1)
                                            time.sleep(1.5)
                                            clean()
                                            continue

                                      if diagrhomb1<=0 or diagrhomb2<=0:
                                        print(val1)
                                        time.sleep(1.5)
                                        clean()
                                        continue
                
                                      arrhomb=(diagrhomb1*diagrhomb2)/2
                                      print(rep10,"Perimeter: ",perhomb,"\n  Area: ",arrhomb,rep10)
                
                                      if cont():
                                        return

                                  elif hinfo1=='no':
                                      print(rep10,"Perimeter: ",perhomb,"\n  Area: Either Height or Diagonal is Required....",rep10)

                                      if cont():
                                        return
          
                                  else:
                                      print(val3)
                                      time.sleep(1.5)
                                      clean()
                                      continue
                                 
                         elif quad=='5':
                             clean()

                             loc='''==========================================================
                 TRAPEZIUM/TRAPEZOID
=========================================================='''

                             while True:
                                
                                  pr(loc)

                                  try:
                                     trasidep1 = float(input("Enter the first parallel side: "))
                                     trasidep2 = float(input("Enter the second parallel side: "))
                                     trasidenp1 = float(input("Enter the first non-parallel side: "))
                                     trasidenp2 = float(input("Enter the second non-parallel side: "))

                                  except ValueError:
                                        print(val1)
                                        time.sleep(1.5)
                                        clean()
                                        continue

                                  if trasidep1<=0 or trasidep2<=0 or trasidenp1<=0 or trasidenp2<=0:
                                    print(val1)
                                    time.sleep(1.5)
                                    clean()
                                    continue

                                  petrap=trasidep1+trasidep2+trasidenp1+trasidenp2

                                  hinfo2=input("Do you Know the Height?((Yes/y)/(No/n)): ").strip().lower()

                                  if hinfo2=='yes' or hinfo2=='y':

                                    try:
                                       trapheight=float(input("Enter the Height: "))

                                    except ValueError:
                                          print(val1)
                                          time.sleep(1.5)
                                          clean()
                                          continue

                                    if trapheight <= 0:
                                      print(val1)
                                      time.sleep(1.5)
                                      clean()
                                      continue
       
                                    artrap=0.5*(trasidep1+trasidep2)*trapheight
                                    print(rep10,"Perimeter: ",petrap,"\n  Area: ",artrap,rep10)

                                    if cont():
                                      return

                                  elif hinfo2=='no' or hinfo2=='n':
                                      print(rep10,"Perimeter: ",petrap,"\n  Area: Calculation requires Height......",rep10)
                                           
                                      if cont():
                                        return

                         elif quad=='6':
                             clean()

                             loc='''==========================================================
                          KITE
=========================================================='''

                             while True:
                                  pr(loc)

                                  try:
                                     kite1=float(input("Enter the Length of First Pair of Equal Sides: "))
                                     kite2=float(input("Enter the Length of Second Pair of Equal Sides: "))

                                  except ValueError:
                                        print(val1)
                                        time.sleep(1.5)
                                        clean()
                                        continue

                                  if kite1<=0 or kite2<=0:
                                        print(val1)
                                        time.sleep(1.5)
                                        clean()
                                        continue
                
                                  pekite=2*(kite1+kite2)
                                  

                                  hinfo3=input("Do you Know the Height or Diagonals? (H -(Height) / D -(Diagonals) / No): ").strip().lower()

                                  if hinfo3=='h':
                
                                    print("\n[Height Must be Perpendicular to One Equal Side]\n")
                                    
                                    try:
                                       kiteheight=float(input("Enter the Height: "))

                                    except ValueError:
                                          print(val1)
                                          time.sleep(1.5)
                                          clean()
                                          continue

                                    if kiteheight<=0:
                                          print(val1)
                                          time.sleep(1.5)
                                          clean()
                                          continue

                                    arkite=kite1*kiteheight
                                    print(rep10,"Perimeter: ",pekite,"\n  Area: ",arkite,rep10)
                     
                                    if cont():
                                      return

                                  elif hinfo3=='d':
              
                                      try:
                                         diagkite1=float(input("Enter the First Diagonal: "))
                                         diagkite2=float(input("Enter the Second Diagonal: "))

                                      except ValueError:
                                            print(val1)
                                            time.sleep(1.5)
                                            clean()
                                            continue

                                      if diagkite1<=0 or diagkite2<=0:
                                        print(val1)
                                        time.sleep(1.5)
                                        clean()
                                        continue
                
                                      arkite1=0.5*diagkite1*diagkite2
                                      print(rep10,"Perimeter: ",pekite,"\n  Area: ",arkite1,rep10)
                     
                                      if cont():
                                        return

                                  elif hinfo3=='no':
                                      print(rep10,"Perimeter: ",pekite,"\n  Area: Either Height or Diagonal is Required....",rep10)
                                           
                                      if cont():
                                        return
       
                                  else:
                                      print(val3)
                                      time.sleep(1.5)
                                      clean()
                                      continue

                         elif quad.lower()=="b":
                           trans()
                           break

                         else:
                             print(val3)
                             continue

                elif dim1=='3':
                    clean()

                    loc='''==========================================================
                 CIRCULAR GEOMETRY
=========================================================='''

                    while True:

                         pr(loc)
                         
                         print(''' ________________________________________________________
|        Please select the Type of Circular Models       |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|                                                        |
|   1.   -|-     Circle.                                 |
|   2.   -|-     Semi-circle.                             |
|   3.   -|-     Sector.                                 |  
|   4.   -|-     Segment.                                |
|   b.   -|-     Go Back                                 |
|________________________________________________________|

''')
     
                         cir1=input("Enter the Type of Circular Operation: ").strip()
        
                         if cir1=='1':
                           clean()

                           loc='''==========================================================
                      CIRCLE
=========================================================='''

                           while True:
                                pr(loc)
            
                                try:
                                   radii1=float(input("Enter the Radius: "))

                                except ValueError:
                                      print(val1)
                                      time.sleep(1.5)
                                      clean()
                                      continue

                                if radii1<=0:
                                  print(val1)
                                  time.sleep(1.5)
                                  clean()
                                  continue
     
                                circum= 2*math.pi*radii1
                                carea=math.pi*radii1*radii1
       
                                print(rep10,"Circumference: ",circum)
                                print("Area: ",carea,rep10)

                                if cont():
                                  return

                         elif cir1=='2':
                             clean()

                             loc='''==========================================================
                      SEMI-CIRCLE
=========================================================='''

                             while True:
                                  pr(loc)
                                  
                                  try:
                                     radii2=float(input("Enter the Radius: "))

                                  except ValueError:
                                        print(val1)
                                        time.sleep(1.5)
                                        clean()
                                        continue

                                  if radii2<=0:
                                    print(val1)
                                    time.sleep(1.5)
                                    clean()
                                    continue
     
                                  scircum=math.pi*radii2+2*radii2
                                  sarea=0.5*math.pi*radii2*radii2

                                  print(rep10,"Perimeter: ",scircum)
                                  print("Area: ",sarea,rep10)
   
                                  if cont():
                                    return

                         elif cir1=='3':
                             clean()

                             loc='''==========================================================
                         SECTOR
=========================================================='''

                             while True:
                                  pr(loc)
    
                                  try:
                                     radii3=float(input("Enter the Radius: "))
                                     ang1=float(input("Enter the Angle: "))

                                  except ValueError:
                                        print(val1)
                                        time.sleep(1.5)
                                        clean()
                                        continue

                                  if radii3<=0 or ang1<=0:
                                    print(val1)
                                    time.sleep(1.5)
                                    clean()
                                    continue

                                  arclen=2*math.pi*radii3*(ang1/360)
                                  arsec1=math.pi*radii3*radii3*(ang1/360)

                                  print(rep10,"Arc Length: ",arclen)
                                  print("Area of Sector: ",arsec1,rep10)
          
                                  if cont():
                                    return

                         elif cir1=='4':
                             clean()

                             loc='''==========================================================
                        SEGMENT
=========================================================='''

                             while True:
                                  pr(loc)

                                  try:
                                     radii4 = float(input("Enter the Radius: "))
                                     ang2=float(input("Enter the Angle: "))

                                  except ValueError:
                                        print(val1)
                                        time.sleep(1.5)
                                        clean()
                                        continue

                                  if radii4<=0 or ang2<=0:
                                        print(val1)
                                        time.sleep(1.5)
                                        clean()
                                        continue
     
                                  arsec2=math.pi*radii4*radii4*(ang2/360)
                                  artri=0.5*radii4*radii4*math.sin(math.radians(ang2))
                                  arseg=arsec2-artri

                                  print(rep10,"Area of Segment: ",arseg,rep10)

                                  if cont():
                                    return

                         elif cir1.lower()=="b":
                             trans()
                             break

                         else:
                             print(val3)
                             continue

                elif dim1.lower()=="b":
                    trans()
                    break 

                else:
                    print(val3)
                    continue

         elif mode3=='2':

             clean()
             
             loc='''==========================================================
             THREE DIMENSIONAL (3-D) SHAPES
=========================================================='''
             
             while True:
                
                  pr(loc)

                  print(''' ________________________________________________________
|               Please select your Figure                |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|                                                        |
|   1.   -|-     Sphere.                                 |
|   2.   -|-     Hemisphere.                             |
|   3.   -|-     Cube.                                   |
|   4.   -|-     Cuboid.                                 |
|   5.   -|-     Cone.                                   |
|   6.   -|-     Cylinder.                               |
|   7.   -|-     Pyramid (Square Pyramid).               |
|   8.   -|-     Frustum.                                | 
|   b.   -|-     Go Back.                                |
|________________________________________________________|

''')

                  dim2=input("Enter the Figure Type: ").strip()
                  
                  if dim2=='1':
                     
                    clean()
                    
                    loc='''==========================================================
                       SPHERE
=========================================================='''
             
                    while True:

                         pr(loc)
          
                         try:
                            radsph=float(input("Enter the Radius: "))

                         except ValueError:
                               print(val1)
                               time.sleep(1.5)
                               clean()
                               continue

                         if radsph<=0:
                           print(val1)
                           time.sleep(1.5)
                           clean()
                           continue
            
                         spvol=(4/3)*math.pi*radsph**3
                         spsa=4*math.pi*radsph**2

                         print(rep10,"Volume: ",spvol)
                         print("Surface Area: ",spsa,rep10)
            
                         if cont():
                           return

                  elif dim2=='2':

                      clean()

                      loc='''==========================================================
                      HEMISPHERE
=========================================================='''

                      while True:

                           pr(loc)
            
                           try:
                              radhsph=float(input("Enter the Radius: "))

                           except ValueError:
                                 print(val1)
                                 time.sleep(1.5)
                                 clean()
                                 continue

                           if radhsph<=0:
                             print(val1)
                             time.sleep(1.5)
                             clean()
                             continue
            
                           hspvol=(2/3)*math.pi*radhsph**3
                           hspcsa=2*math.pi*radhsph**2
                           hsptsa=3*math.pi*radhsph**2

                           print(rep10,"Volume: ",hspvol)
                           print("Curved Surface Area (CSA): ",hspcsa)
                           print("Total Surface Area (TSA): ",hsptsa,rep10)
            
                           if cont():
                             return
                      
                  elif dim2=='3':

                      clean()

                      loc='''==========================================================
                       CUBE
=========================================================='''

                      while True:

                           pr(loc)

                           try:
                              cuside=float(input("Enter the Side Length: "))

                           except ValueError:
                                 print(val1)
                                 time.sleep(1.5)
                                 clean()
                                 continue

                           if cuside<=0:
                             print(val1)
                             time.sleep(1.5)
                             clean()
                             continue
                      
                           cuvol=cuside**3
                           culsa=4*cuside**2
                           cutsa=6*cuside**2

                           print(rep10,"Volume: ",cuvol)
                           print("Lateral Surface Area (LSA): ",culsa)
                           print("Total Surface Area (TSA): ",cutsa,rep10)
            
                           if cont():
                             return
                            
                  elif dim2=='4':

                      clean()

                      loc='''==========================================================
                       CUBOID
=========================================================='''

                      while True:

                           pr(loc)

                           try:
                              lencud=float(input("Enter the Length: "))
                              brthcud=float(input("Enter the Breadth: "))
                              heightcud=float(input("Enter the Height: "))

                           except ValueError:
                                 print(val1)
                                 time.sleep(1.5)
                                 clean()
                                 continue

                           if lencud<=0 or brthcud<=0 or heightcud<=0:
                             print(val1)
                             time.sleep(1.5)
                             clean()
                             continue
            
                           cudvol=lencud*brthcud*heightcud
                           cudlsa=2*heightcud*(lencud+brthcud)
                           cudtsa=2*(lencud*brthcud+brthcud*heightcud+heightcud*lencud)

                           print(rep10,"Volume: ",cudvol)
                           print("Lateral Surface Area (LSA): ",cudlsa)
                           print("Total Surface Area (TSA): ",cudtsa,rep10)
            
                           if cont():
                             return

                  elif dim2=='5':

                      clean()

                      loc='''==========================================================
                         CONE
=========================================================='''

                      while True:

                           pr(loc)
            
                           try:
                              radcone=float(input("Enter the Radius of Base: "))
                              heightcone=float(input("Enter the Height: "))

                           except ValueError:
                                 print(val1)
                                 time.sleep(1.5)
                                 clean()
                                 continue

                           if radcone<=0 or heightcone<=0:
                             print(val1)
                             time.sleep(1.5)
                             clean()
                             continue
                 
                           slant=math.sqrt(heightcone**2+radcone**2)
                           conevol=(1/3)*math.pi*radcone**2*heightcone
                           conecsa=math.pi*radcone*slant
                           conetsa=conecsa+math.pi*radcone**2

                           print(rep10,"Volume: ",conevol)
                           print("Curved Surface Area (CSA): ",conecsa)
                           print("Total Surface Area (TSA): ",conetsa,rep10)
            
                           if cont():
                             return
     
                  elif dim2=='6':

                      clean()

                      loc='''==========================================================
                       CYLINDER
=========================================================='''

                      while True:

                           pr(loc)
            
                           try:
                              radcyl=float(input("Enter the Radius of Base: "))
                              heightcyl=float(input("Enter the Height: "))

                           except ValueError:
                                 print(val1)
                                 time.sleep(1.5)
                                 clean()
                                 continue

                           if radcyl<=0 or heightcyl<=0:
                             print(val1)
                             time.sleep(1.5)
                             clean()
                             continue
            
                           cylvol=math.pi*radcyl**2*heightcyl
                           cylcsa=2*math.pi*radcyl*heightcyl
                           cyltsa=cylcsa+2*math.pi*radcyl**2

                           print(rep10,"Volume: ",cylvol)
                           print("Curved Surface Area (CSA): ",cylcsa)
                           print("Total Surface Area (TSA): ",cyltsa,rep10)
            
                           if cont():
                             return

                  elif dim2=='7':

                      clean()

                      loc='''==========================================================
                PYRAMID (SQUARE PYRAMID)
=========================================================='''

                      while True:

                           pr(loc)
            
                           try:
                              basepyr=float(input("Enter the Base Side Length: "))
                              heightpyr=float(input("Enter the Height: "))

                           except ValueError:
                                 print(val1)
                                 time.sleep(1.5)
                                 clean()
                                 continue

                           if basepyr<=0 or heightpyr<=0:
                             print(val1)
                             time.sleep(1.5)
                             clean()
                             continue
            
                           slant1=math.sqrt((basepyr/2)**2+heightpyr**2)
                           pyrvol=(1/3)*basepyr**2*heightpyr
                           pyrlsa=2*basepyr*slant1
                           pyrtsa=basepyr**2+pyrlsa

                           print(rep10,"Volume: ",pyrvol)
                           print("Lateral Surface Area (LSA): ",pyrlsa)
                           print("Total Surface Area (TSA): ",pyrtsa,rep10)
            
                           if cont():
                             return

                  elif dim2=='8':

                      clean()

                      loc='''==========================================================
                    FRUSTUM
=========================================================='''

                      pr(loc)

                      while True:
            
                           try:
                              frurad1=float(input("Enter the Radius of Larger Base: "))
                              frurad2=float(input("Enter the Radius of Smaller Base: "))
                              fruheight=float(input("Enter the Height: "))

                           except ValueError:
                                 print(val1)
                                 time.sleep(1.5)
                                 clean()
                                 continue

                           if frurad1<=0 or frurad2<=0 or fruheight<=0:
                             print(val1)
                             time.sleep(1.5)
                             clean()
                             continue
            
                           slant2=math.sqrt(fruheight**2+(frurad1-frurad2)**2)
                           fruvol=(1/3)*math.pi*fruheight*(frurad1**2+frurad2**2+frurad1*frurad2)
                           frucsa=math.pi*(frurad1+frurad2)*slant2
                           frutsa=frucsa+math.pi*(frurad1**2+frurad2**2)
            
                           print(rep10,"Volume: ",fruvol)
                           print("Curved Surface Area (CSA): ",frucsa)
                           print("Total Surface Area (TSA): ",frutsa,rep10)
                        
                           if cont():
                             return

                  elif dim2.lower()=="b":
                      trans()
                      break

                  else:
                      print(val3)
                      time.sleep(1.5)
                      clean()
                      continue

         elif mode3.lower()=="r":
             return

         else:
             print(val3)
             time.sleep(1.5)
             clean()
             continue
#Boot Screen

clean()
print(welcome)
time.sleep(1.5)
input("Press ENTER to Start Calculations... \n==================================================================================")
clean()

#Choose Modes
while True:
     loc='''==========================================================
                       MAIN MENU
=========================================================='''

     pr(loc)
  
     print(''' ________________________________________________________
|               Please select your Mode                  |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|                                                        |
|   g.   -|-     General Instructions.                   |
|   1.   -|-     Basic Calculator.                       |
|   2.   -|-     Exponential Operations.                 |
|   3.   -|-     Factorials.                             |
|   4.   -|-     Basic Trigonometry.                     |
|   5.   -|-     Statistics(Ungrouped Data).             |
|   6.   -|-     Interests.                              |
|   7.   -|-     Multiplication Table.                   |
|   8.   -|-     Basic Geometry.                         | 
|   e.   -|-     Exit                                    |
|________________________________________________________|
''')
     mode=input("Enter the Mode: ").strip()

#Execute Functions

     if mode.lower()=='g':
       clean()
       mainguide()
       input(rep9)
       clean()
          
     elif mode=='1':
         trans()
         basiccalc()
         input(rep9)
         trans()

     elif mode=='2':
         trans()
         expops()
         input(rep9)
         trans()
    
     elif mode=='3':
         trans()
         factorial()
         input(rep9)
         trans()

     elif mode=='4':
         trans()
         trigonometry()
         input(rep9)
         trans()
    
     elif mode=='5':
         trans()
         stats()
         input(rep9)
         trans()
    
     elif mode=='6':
         trans()
         interests()
         input(rep9)
         trans()
     
     elif mode=='7':
         trans()
         multable()
         input(rep9)
         trans()
    
     elif mode=='8':
         trans()
         basicgeo()
         input(rep9)
         trans()

     elif mode.lower()=='e':
         clean()
         print(rep11)
         print(rep8)
         time.sleep(1.5)
         clean()
         break
         
     else:
         print(val3)
         time.sleep(1.5)
         clean()
         continue



