#Project Command Calc

#Welcome
welcome='''
==================================================================================
                          WELCOME TO COMMAND CALC
----------------------------------------------------------------------------------               
©Illektron Softwares                                                   v-1.3.0
==================================================================================
==================================================================================
'''

print(welcome)

#General instructions

inst='''___________________________________________________________________________________

General Instructions:-

  i). To Execute the Operation press '=' in the Operation section.
  ii). Do not Forget to Press 'ENTER' Everytime you Enter an Input.
  iii). Restart the Program for Another Calculation.

IMPORTANT NOTICE:-

   *The 'π'(Pi) Symbol is not Recognized. Please Enter math.pi for 'π'.*
   **Scientific Terms are Not Available.**
   ***The Required Answer Will be Shown in Decimal Format.***
   ****If the Calculator Fails to Provide the Solution on Command Prompt,
       please Install Python and Run it on IDLE****
__________________________________________________________________________________        
'''

thx='''
Hello... Please Proceed.
'''

#Import Functions

import math
import statistics

#Some Repeating Codes

#dialogues

rep1='\n GOOD LUCK!!! \n___________________________________________________________________________________ \n'

rep2='''\n Software Will Consider it as 'NO'
   GOOD LUCK!!!.
___________________________________________________________________________________
   '''

rep4='\n INVALID OPERATOR / Value.... Please Try Again.\n__________________________________________________________\n'

rep5='\n INVALID CHOICE.... Please Try Again.\n__________________________________________________________\n'

rep6="\n Thank you.\n"

rep7='\n Proceeding ......... \n'

rep8="\n Thank You for Using Command Calc........\n================================================================================== "

rep9="\n Press ENTER to Continue... \n==================================================================================\n"

rep10='\n=================================================\n '

#Inputs

inp1=" \n Do you Want to View Instructions? (Yes/No): "

inp2="________________________________________________________\n \n Do you want to Continue?(Yes/No): "

#Validity

val1="\n INVALID DIMENSIONS.... Please Try again.\n__________________________________________________________\n"

#Sub functions

#1.Guide
#============================================================================================================

def guide(txt):

   guide=input(inp1)

   if guide.strip().lower()=='yes':
     print(txt)
  
   elif guide.strip().lower()=='no':
       print(rep1)
   
   else:
       print(rep2)

#2.Continue
#============================================================================================================

def cont():
    while True:

         cont=input(inp2).strip().lower()

         if cont=='yes':
            print(rep7)
            return False

         elif cont=='no':
              print(rep6)
              return True

         else:
              print(rep4)
              continue

#Main Functions

#1.Basic Calculator.
#============================================================================================================

def basiccalc():
   #Instructions 1

   loc='''==========================================================
                  BASIC CALCULATOR
=========================================================='''

   print(loc)

   txt='''___________________________________________________________________________________

Instructions:-

    Type the Question in the Form of Expression.

IMPORTANT NOTICE:-

    *Note that Variables DO NOT Work*
    **Pi Value is NOT Available.**
    ***Only Paranthests '()' is Available.***

        For Operations,

         Addition:'+'           Subtraction:'-'
         Multiplication:'x'     Division:'/'
         Modulus:'%'

         EQUALS '=' is not Compulsory

   GOOD LUCK!!!
___________________________________________________________________________________
   '''
   
   guide(txt)
   
   #Main Program 1

   res=0
   accept1="1234567890=+-*xX/%() "
   while True:
        expr1=input("Enter Expression: ")
        expr1=expr1.replace('x','*')
        expr1=expr1.replace('X','*')
        expr1=expr1.replace('=',' ')
      
        if not all(ch in accept1 for ch in expr1):
          print(rep4)
          continue
        
        try:
           res=eval(expr1, {"__builtins__": None}, {})
           print(rep10,"Solution: ",res,rep10)

        except (SyntaxError, ZeroDivisionError, OverflowError):
              print("\n Invalid Expression .... \n")

        if cont():
          return
             
#2.Exponential Operations.
#============================================================================================================

def expops():

   loc='''==========================================================
                 EXPONENTIAL OPERATIONS
=========================================================='''

   print(loc)

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
           
          loc='''==========================================================
                 SQUARE AND CUBE ROOTS
=========================================================='''

          print(loc)
          
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
               try:
                  num1 = int(input("Enter the number: "))
               except ValueError:
                     print(rep4)
                     continue
             
               o1=input("Enter the operation: ")

               if o1.strip().lower()=='sqrt':
                 print(rep10,"Square Root: ",math.sqrt(num1),rep10)

               elif o1.strip().lower()=='cbrt':
                   print(rep10,"Cube Root: ",num1**(1/3),rep10)
         
               else:
                   print(rep4)
                   continue

               if cont():
                 return

        elif mode1=='2':

            loc='''==========================================================
                RAISE TO EXPONENTIAL FORM
=========================================================='''

            print(loc)

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
            
                 try:
                    num2=float(input("Enter the Number: "))
                
                 except ValueError:
                       print(rep4)
                       continue
                 try:     
                    pwr1=float(input("Enter the Power: "))
              
                 except ValueError:
                       print(rep4)
                       continue
          
                 print(rep10,"Solution: ",pow(num2,pwr1),rep10)

                 if cont():
                   return

                        
        elif mode1.lower()=='r':
            print(rep7)
            return

        else:
            print(rep5)
            continue
      
#3.Factorials.
#============================================================================================================

def factorial():

    #Instructions 3

    loc='''==========================================================
                      FACTORIALS
=========================================================='''

    print(loc)

    txt='''___________________________________________________________________________________

Instructions:-

    Enter the Number to Find its Factorial.

    GOOD LUCK!!!!
___________________________________________________________________________________
     '''

    guide(txt)
            
    #Main Program 3
    while True:   
         try:
            num3 = int(input("Enter the Number: "))
       
            if num3 < 0:
              print("Factorials not defined for negative numbers")
         
            elif num3 > 100:
                print("Number too large")
           
            else:
                print(rep10,"Solution: ",math.factorial(num3),rep10)
        
         except ValueError:
               print("Enter Integers Only")

         if cont():
           return
                        
#4.Basic Trigonometry.
#============================================================================================================

def trigonometry():
    #Instructions 4

    loc='''==========================================================
                      TRIGONOMETRY
=========================================================='''

    print(loc)
   
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
         try:
            num4=float(input("Enter the Angle: "))

         except ValueError:
               print(rep4)
               continue
              
         ang=math.radians(num4)

         o2=input("Enter the Trigonometric Function: ")

         if o2.strip().lower()=='sin':
           print(rep10,"Sin",num4,":",math.sin(ang),rep10)

         elif o2.strip().lower()=='cos':
             print(rep10,"Cos",num4,":",math.cos(ang),rep10)
        
         elif o2.strip().lower()=='tan':
             if math.cos(ang) == 0:
               print(rep10,"Not Defined",rep10)
             else:
                 print(rep10,"Tan",num4,":",math.tan(ang),rep10)
   
         elif o2.strip().lower()=='cosec':
             if math.sin(ang)==0:
                print(rep10,"Not Defined",rep10)
             else:
                 print(rep10,"Cosec",num4,":",1/math.sin(ang),rep10)

         elif o2.strip().lower()=='sec':
             if math.cos(ang) == 0:
               print(rep10,"Not Defined",rep10)
             else:
                 print(rep10,"Sec",num4,":",1/math.cos(ang),rep10)

         elif o2.strip().lower()=='cot':
             if math.tan(ang) == 0:
               print(rep10,"Not Defined",rep10)
             else:
                 print(rep10,"Cot",num4,":",1/math.tan(ang),rep10)

         else:
             print(rep4)
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

    print(loc)
   
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
      
         statinp=input("Enter the Data With Spaces: ")
         try:
            statdata = list(map(float, statinp.split()))
         except ValueError:
               print("Invalid data entered")
               continue
          
         if len(statdata) == 0:
           print("No data entered")
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
                  print(rep4)
                  continue

         if cont():
           return

#6.Interests.
#============================================================================================================

def interests():

   loc='''==========================================================
                      INTERESTS
=========================================================='''

   print(loc)
   
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
           loc='''==========================================================
                   SIMPLE INTEREST
=========================================================='''

           print(loc)
   
      
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
            
                #main program 6_1
                try:
                   prinamt=float(input("Enter the Total Principal Amount: "))
                   rateint=float(input("Enter the Rate of Interest: "))
                   time=float(input("Enter Time in years: "))
         
                except ValueError:
                      print(rep4)
                      continue

                if prinamt<=0:
                  print(val1)
                  continue
    
                if time<=0:
                  print(val1)
                  continue

                simpint=(prinamt*rateint*time)/100
                amtpay=prinamt+simpint

                print(rep10,"Simple Interest: ",simpint,rep10)
                print(rep10,"Amount Payable",amtpay,rep10)

                if cont():
                  return
                 
         elif mode2=='2':

             loc='''==========================================================
                  COMPOUND INTEREST
=========================================================='''

             print(loc)
        
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
        
                  #main program 6_2
                  try:
                     prinamt1=float(input("Enter the Total Principle Amount: "))
                     rateint1=float(input("Enter the Rate of Interest: "))
                     time1=float(input("Enter Time in years: "))
           
                  except ValueError:
                        print(rep4)
                        continue

                  if prinamt1 <= 0 or time1 <= 0:
                    print(val1)
                    continue

                  amtpay1=prinamt1*(1+rateint1/100)**time1
                  compint=amtpay1-prinamt1
     
                  print(rep10,"Compound Interest: ",compint,rep10)
                  print(rep10,"Amount Payable",amtpay1,rep10)

                  if cont():
                    return

         elif mode2.lower()=='r':
             return

         else:
             print(rep5)
             continue

#7.Multiplication Table.
#============================================================================================================

def multable():

    loc='''==========================================================
                 MULTIPLICATION TABLE
=========================================================='''

    print(loc)
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
      
         try:    
            mul=int(input("Enter the Number for Generating table: "))

         except ValueError:
               print(rep4)
               continue

         try:    
            mul1=int(input("Enter the Maximum Multiplier: "))

         except ValueError:
               print(rep4)
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

    print(loc)

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
        
         #Choice 3

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
           loc='''==========================================================
             TWO DIMENSIONAL (2-D) GEOMETRY
=========================================================='''

           print(loc)

           while True:

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
                  loc='''==========================================================
                 TRIANGULAR GEOMETRY
=========================================================='''

                  print(loc)

                  while True:
                       
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

                         loc='''==========================================================
                  EQUILATERAL TRIANGLE
=========================================================='''

                         print(loc)

                         while True:
                              
                              try:
                                 sideeqt=float(input("\nEnter the Length: "))

                              except ValueError:
                                    print(rep4)
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

                           loc='''==========================================================
                  ISOSCELES TRIANGLE
=========================================================='''

                           print(loc)

                           while True:
          
                                sideorheight=input("\nIs Height given(Yes / No): ")
            
                                if sideorheight.strip().lower()=='yes':
                                    
                                  while True:
                   
                                       try:
                                          base1=float(input("\nEnter the Base: "))
                                          height1=float(input("Enter the Height: "))

                                       except ValueError:
                                             print(rep4)
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
     
                                elif sideorheight.strip().lower()=='no':
                                    
                                    while True:

                                         try:
                                            eqside1=float(input("\nEnter the Equal Side Length: "))
                                            base1=float(input("Enter the Base: "))

                                         except ValueError:
                                               print(rep4)
                                               continue

                                         if eqside1<=base1/2:
                                           print(val1)
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

                       elif tri=='3':

                           loc='''==========================================================
                    SCALENE TRIANGLE
=========================================================='''

                           print(loc)

                           while True:
                               
                                try:
                                   s1=float(input("\nEnter first Side: "))
                                   s2=float(input("Enter Second Side: "))
                                   s3=float(input("Enter Third Side: "))

                                except ValueError:
                                     print(rep4)
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
                                    continue

                       elif tri.lower()=="b":
                           print(rep7)
                           break
                        
                       else:
                           print(rep5)
                           continue

                elif dim1=='2':

                    loc='''==========================================================
                 QUADRILATERAL GEOMETRY
=========================================================='''

                    print(loc)

                    while True:
                         
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

                           loc='''==========================================================
                       SQUARE
=========================================================='''

                           print(loc)

                           while True:
            
                                try:
                                   sidesq=float(input("\nEnter the Length: "))

                                except ValueError:
                                      print(rep4)
                                      continue
                                    
                                pesq=sidesq*4
                                arsq=sidesq*sidesq
     
                                print(rep10,"Perimeter: ",pesq)
                                print("Area: ",arsq,rep10)
     
                                if cont():
                                  return
          
                         elif quad=='2':

                             loc='''==========================================================
                       RECTANGLE
=========================================================='''

                             print(loc)

                             while True:
          
                                  try:
                                     rect1=float(input("\nEnter the Length 1: "))
                                     rect2=float(input("Enter the Length 2: "))

                                  except ValueError:
                                       print(rep4)
                                       continue
     
                                  perect=2*(rect1+rect2)
                                  arrect=rect1*rect2

                                  print(rep10,"Perimeter: ",perect)
                                  print("Area: ",arrect,rep10)

                                  if cont():
                                    return
            
                         elif quad=='3':
                             loc='''==========================================================
                    PARALLELOGRAM
=========================================================='''

                             print(loc)

                             while True:
          
                                  try:
                                     parabase=float(input("\nEnter the Base: "))
                                     paraside=float(input("Enter the Side Length: "))

                                  except ValueError:
                                        print(rep4)
                                        continue

                                  pepara=2*(parabase+paraside)

                                  print(rep10,"Perimeter: ",pepara,rep10)

                                  while True:
            
                                       hinfo=input("\nDo you Know the Height?(Yes/No): ")

                                       if hinfo.strip().lower()=='yes':
                                         while True:
              
                                              try:
                                                 paraheight=float(input("\nEnter the Height: "))
     
                                              except ValueError:
                                                    print(rep4)
                                                    continue

                                              else:
                                                  break
                      
                                              paraarea=parabase*paraheight
                    
                                              print(rep10,"Area: ",paraarea,rep10)

                                         if cont():
                                            return
                
                                       elif hinfo.strip().lower()=='no':
                                           print("Area Cannot be Calculated Without Height")
                                      
                                           if cont():
                                             return
                                            
                                       else:
                                           print(rep5)
                                           continue
                                 
                         elif quad=='4':

                             loc='''==========================================================
                        RHOMBUS
=========================================================='''

                             print(loc)

                             while True:
            
                                  try:
                                     rhombside=float(input("Enter the Side Length: "))

                                  except ValueError:
                                        print(rep4)
                                        continue

                                  perhomb=4*rhombside

                                  print(rep10,"Perimeter: ",perhomb,rep10)
                 
                                  while True:

                                       try:
                                          hinfo1=input("Do you Know the Height or Diagonals?(H -(Height) / D -(Diagonals)) / No: ")

                                       except ValueError:
                                             print(rep4)
                                             continue

                                       if hinfo1.strip().lower()=='h':
                                         while True:

                                              try:
                                                 rhombheight=float(input("\nEnter the Height: "))

                                              except ValueError:
                                                    print(rep4)
                                                    continue

                                              else:
                                                  break
                    
                                              arrhomb=rhombside*rhombheight
               
                                              print(rep10,"Area: ",arrhomb,rep10)
     
                                         if cont():
                                           return
                
                                       elif hinfo1.strip().lower()=='d':

                                           while True:
                          
                                                try:
                                                   diagrhomb1=float(input("Enter the First Diagonal: "))
                                                   diagrhomb2=float(input("Enter the Second Diagonal: "))

                                                except ValueError:
                                                    print(rep4)
                                                    continue

                                                else:
                                                    break
                
                                                arrhomb=(diagrhomb1*diagrhomb2)/2

                                                print(rep10,"Area: ",arrhomb,rep10)
                
                                           if cont():
                                             return

                                       elif hinfo1.strip().lower()=='no':
                                           print("\nEither Height or Diagonal is Required to Proceed.\n")
                                           if cont():
                                             return
          
                                       else:
                                           print(rep5)
                                           continue
                                 
                         elif quad=='5':

                             loc='''==========================================================
                 TRAPEZIUM/TRAPEZOID
=========================================================='''

                             print(loc)


                             while True:

                                  try:
                                     trasidep1 = float(input("Enter the first parallel side: "))
                                     trasidep2 = float(input("Enter the second parallel side: "))
                                     trasidenp1 = float(input("Enter the first non-parallel side: "))
                                     trasidenp2 = float(input("Enter the second non-parallel side: "))

                                  except ValueError:
                                        print(rep4)
                                        continue

                                  petrap=trasidep1+trasidep2+trasidenp1+trasidenp2

                                  print(rep10,"Perimeter: ",petrap,rep10)

                                  while True:
                                       hinfo2=input("Do you Know the Height?(Yes/No): ")

                                       if hinfo2.strip().lower()=='yes':
                                         while True:

                                              try:
                                                 trapheight=float(input("Enter the Height: "))

                                              except ValueError:
                                                    print(rep4)
                                                    continue

                                              else:
                                                  break
                
                                              artrap=0.5*(trasidep1+trasidep2)*trapheight
               
                                              print(rep10,"Area: ",artrap,rep10)

                                         if cont():
                                           return

                                       elif hinfo2.strip().lower()=='no':
                                           print("Cannot Proceed Without Height")
                                           if cont():
                                             return

                         elif quad=='6':

                             loc='''==========================================================
                          KITE
=========================================================='''

                             print(loc)


                             while True:

                                  try:
                                     kite1=float(input("Enter the Length of First Pair of Equal Sides: "))
                                     kite2=float(input("Enter the Length of Second Pair of Equal Sides: "))

                                  except ValueError:
                                        print(rep4)
                                        continue
                
                                  pekite=2*(kite1+kite2)
                                  print(rep10,"Perimeter: ",pekite,rep10)

                                  while True:
                                       hinfo3=input("Do you Know the Height or Diagonals? (H -(Height) / D -(Diagonals) / No): ")

                                       if hinfo3.strip().lower()=='h':
                
                                         print("Height Must be Perpendicular to One Equal Side")
                          
                                         while True:

                                              try:
                                                 kiteheight=float(input("Enter the Height: "))

                                              except ValueError:
                                                    print(rep4)
                                                    continue

                                              else:
                                                  break
              
                                              arkite=kite1*kiteheight
                     
                                              print(rep10,"Area: ",arkite,rep10)
                     
                                         if cont():
                                           return

                                       elif hinfo3.strip().lower()=='d':
              
                                           while True:
                                                try:
                                                   diagkite1=float(input("Enter the First Diagonal: "))
                                                   diagkite2=float(input("Enter the Second Diagonal: "))


                                                except ValueError:
                                                      print(rep4)
                                                      continue

                                                else:
                                                    break
                
                                                arkite1=0.5*diagkite1*diagkite2
                
                                                print(rep10,"Area: ", arkite1,rep10)
                     
                                           if cont():
                                             return

                                       elif hinfo3.strip().lower()=='no':
                                           print("Cannot Proceed Without Height")
                                           if cont():
                                             return
       
                                       else:
                                           print(rep5)
                                           continue

                         elif quad.lower()=="b":
                           print(rep7)
                           break

                         else:
                             print(rep5)
                             continue

                elif dim1=='3':

                    loc='''==========================================================
                 CIRCULAR GEOMETRY
=========================================================='''

                    print(loc)

                    while True:
                         
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

                           loc='''==========================================================
                      CIRCLE
=========================================================='''

                           print(loc)

                           while True:
            
                                try:
                                   radii1=float(input("Enter the Radius: "))

                                except ValueError:
                                      print(rep4)
                                      continue
     
                                circum= 2*math.pi*radii1
                                carea=math.pi*radii1*radii1
       
                                print(rep10,"Circumference: ",circum)
                                print("Area: ",carea,rep10)

                                if cont():
                                  return

                         elif cir1=='2':

                             loc='''==========================================================
                      SEMI-CIRCLE
=========================================================='''

                             print(loc)

                             while True:
    
                                  try:
                                     radii2=float(input("Enter the Radius: "))

                                  except ValueError:
                                        print(rep4)
                                        continue
     
                                  scircum=math.pi*radii2+2*radii2
                                  sarea=0.5*math.pi*radii2*radii2

                                  print(rep10,"Perimeter: ",scircum)
                                  print("Area: ",sarea,rep10)
   
                                  if cont():
                                    return

                         elif cir1=='3':

                             loc='''==========================================================
                         SECTOR
=========================================================='''

                             print(loc)

                             while True:
    
                                  try:
                                     radii3=float(input("Enter the Radius: "))
                                     ang1=float(input("Enter the Angle: "))

                                  except ValueError:
                                        print(rep4)
                                        continue

                                  arclen=2*math.pi*radii3*(ang1/360)
                                  arsec1=math.pi*radii3*radii3*(ang1/360)

                                  print(rep10,"Arc Length: ",arclen)
                                  print("Area of Sector: ",arsec1,rep10)
          
                                  if cont():
                                    return

                         elif cir1=='4':

                             loc='''==========================================================
                        SEGMENT
=========================================================='''

                             print(loc)

                             while True:

                                  try:
                                     radii4 = float(input("Enter the Radius: "))
                                     ang2=float(input("Enter the Angle: "))

                                  except ValueError:
                                        print(rep4)
                                        continue
     
                                  arsec2=math.pi*radii4*radii4*(ang2/360)
                                  artri=0.5*radii4*radii4*math.sin(math.radians(ang2))
                                  arseg=arsec2-artri

                                  print(rep10,"Area of Segment: ",arseg,rep10)

                                  if cont():
                                    return

                         elif cir1.lower()=="b":
                             print(rep7)
                             break

                         else:
                             print(rep5)
                             continue

                elif dim1.lower()=="b":
                    print(rep7)
                    break 

                else:
                    print(rep5)
                    continue

         elif mode3=='2':
             loc='''==========================================================
             THREE DIMENSIONAL (3-D) SHAPES
=========================================================='''

             print(loc)
             
             while True:

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
                    loc='''==========================================================
                       SPHERE
=========================================================='''

                    print(loc)
             
                    while True:
          
                         try:
                            radsph=float(input("Enter the Radius: "))

                         except ValueError:
                               print(rep4)
                               continue
            
                         spvol=(4/3)*math.pi*radsph**3
                         spsa=4*math.pi*radsph**2

                         print(rep10,"Volume: ",spvol)
                         print("Surface Area: ",spsa,rep10)
            
                         if cont():
                           return

                  elif dim2=='2':

                      loc='''==========================================================
                      HEMISPHERE
=========================================================='''

                      print(loc)

                      while True:
            
                           try:
                              radhsph=float(input("Enter the Radius: "))

                           except ValueError:
                                 print(rep4)
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

                      loc='''==========================================================
                       CUBE
=========================================================='''

                      print(loc)

                      while True:

                           try:
                              cuside=float(input("Enter the Side Length: "))

                           except ValueError:
                                 print(rep4)
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

                      loc='''==========================================================
                       CUBOID
=========================================================='''

                      print(loc)

                      while True:

                           try:
                              lencud=float(input("Enter the Length: "))
                              brthcud=float(input("Enter the Breadth: "))
                              heightcud=float(input("Enter the Height: "))

                           except ValueError:
                                 print(rep4)
                                 continue
            
                           cudvol=lencud*brthcud*heightcud
                           cudlsa=2*heightcud*(lencud+brthcud)
                           cudtsa=2*(lencud*brthcud+brthcud*heightcud+heightcud*lencud)

                           print(rep10,"Volume: ",cudvol)
                           print("Lateral Surface Area (LSA): ",cudlsa)
                           print("Surface Area (TSA): ",cudtsa,rep10)
            
                           if cont():
                             return

                  elif dim2=='5':

                      loc='''==========================================================
                         CONE
=========================================================='''

                      print(loc)

                      while True:
            
                           try:
                              radcone=float(input("Enter the Radius of Base: "))
                              heightcone=float(input("Enter the Height: "))

                           except ValueError:
                                 print(rep4)
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

                      loc='''==========================================================
                       CYLINDER
=========================================================='''

                      print(loc)

                      while True:
            
                           try:
                              radcyl=float(input("Enter the Radius of Base: "))
                              heightcyl=float(input("Enter the Height: "))

                           except ValueError:
                                 print(rep4)
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

                      loc='''==========================================================
                PYRAMID (SQUARE PYRAMID)
=========================================================='''

                      print(loc)

                      while True:
            
                           try:
                              basepyr=float(input("Enter the Base Side Length: "))
                              heightpyr=float(input("Enter the Height: "))

                           except ValueError:
                                 print(rep4)
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

                      loc='''==========================================================
                    FRUSTUM
=========================================================='''

                      print(loc)

                      while True:
            
                           try:
                              frurad1=float(input("Enter the Radius of Larger Base: "))
                              frurad2=float(input("Enter the Radius of Smaller Base: "))
                              fruheight=float(input("Enter the Height: "))

                           except ValueError:
                                 print(rep4)
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
                      print(rep7)
                      break

                  else:
                      print(rep5)
                      continue

         elif mode3.lower()=="r":
             print(rep7)
             return

         else:
             print(rep5)
             continue

# BOOTSCREEN
while True:
     
     prompt=input('''Press ENTER to Start or Type 'Guide' to view General Instructions and Start
Your Answer: ''')
     print("================================================================================== ")
     if prompt.strip().lower()=='':
       print(thx)
       break
  
     elif prompt.strip().lower()=='guide':
         print(inst,thx)
         input(rep9)
         break
     
     else:
         print("Please Give a Right answer....... \n")
         continue
        
#Choose Modes
while True:
     loc='''==========================================================
                     MAIN MENU
=========================================================='''

     print(loc)

  
     print(''' ________________________________________________________
|               Please select your Mode                  |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|                                                        |
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
          
     if mode=='1':
       basiccalc()
       input(rep9)

     elif mode=='2':
         expops()
         input(rep9)
    
     elif mode=='3':
         factorial()
         input(rep9)

     elif mode=='4':
         trigonometry()
         input(rep9)
    
     elif mode=='5':
         stats()
         input(rep9)
    
     elif mode=='6':
         interests()
         input(rep9)
     
     elif mode=='7':
         multable()
         input(rep9)
    
     elif mode=='8':
         basicgeo()
         input(rep9)

     elif mode.lower()=='e':
         print(rep8)
         break
         
     else:
         print(rep5)
         continue



