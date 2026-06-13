#Project Command Calc

#Welcome
welcome='''
==================================================================================
                          WELCOME TO COMMAND CALC
==================================================================================                
©Illektron Softwares                                                   v-1.2.1
================================================================================== 
'''

print(welcome)

#General instructions

inst='''
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
Thanks... Please Proceed.
'''

prompt=input('''Type 'Start' or Type 'Guide' to view General instructions and start
Your Answer: ''')

if prompt.strip().lower()=='start':
  print(thx)
  
elif prompt.strip().lower()=='guide':
    print(inst,thx)

else:
    print('''
Software Will Consider it as 'Start.''',thx)

#Import Functions

import math
import statistics

#Some Repeating Codes

#dialogues

rep1='''
   GOOD LUCK!!!

   '''

rep2='''
Software Will Consider it as 'NO'
   GOOD LUCK!!!.

   '''

rep3='''
  Please Restart for Another Calculation.

       Thanks For Using Our App.

       '''



rep4='''
INVALID OPERATOR / Value.... Please Restart the Program to Continue.'''

rep5='''
INVALID CHOICE.... Please Restart the Program to Continue.'''

#Inputs

inp1="Do you Want to View Instructions? (Yes/No): "

#Validity

val1="INVALID DIMENSIONS.... Please Restart the Program to Continue."

#Choose Modes

print('''Please select your Mode:-

1.Basic Calculator.
2.Exponential Operations.
3.Factorials.
4.Basic Trigonometry.
5.Statistics(Ungrouped Data).
6.Interests.
7.Multiplication Table.
8.Basic Geometry.
''')
mode=input("Enter the Mode: ").strip()

#Important Functions

#1.Basic Calculator.
#============================================================================================================

def basiccalc():
   #Instructions 1

   txt1='''
   Instructions:-

   i). Enter a Number in Integer Form or Decimal Form.
   ii). Enter the Required Operation.

        For Operations,

         Addition:'+'           Subtraction:'-'
         Multiplication:'x'     Division:'/'

   GOOD LUCK!!!

   '''
   
   guide=input(inp1)

   if guide.strip().lower()=='yes':
     print(txt1)
  
   elif guide.strip().lower()=='no':
       print(rep1)
   
   else:
       print(rep2)
    
   #Main Program 1

   try:
      res=float(input("Enter a Number: "))
      
   except ValueError:
         print(rep4)
         exit()

   while True:
        o=input("Enter Operator: ").strip()

        if o=='=':
          print('''
  Solution:''',res)
          print(rep3)
          break
        try:
           num=float(input("Enter a Number: "))

        except ValueError:
              print(rep4)
              exit()
              
        if o=='+':
          res += num

        elif o=='-':
            res -= num

        elif o=='x':
            res *= num

        elif o=='*':
            res *= num

        elif o=='/':
            try:
               res /= num
            except ZeroDivisionError:
                  print("Not Defined")
                  break
            
        else:
            print(rep4)
            break

#2.Exponential Operations.
#============================================================================================================

def expops():
    #Choice 1
    print('''
Enter the Type of Operation:-

1.Square and Cube Roots.
2.Raise to Exponential Form.

    ''')
    
    mode1=input("Enter Your Choice: ").strip()

    if mode1=='1':
       #Instructions 2
      
       txt2_1='''Instructions:-

       For Operations,

          Square Root:'sqrt'
          Cube Root:'cbrt'
     
       GOOD LUCK!!!!

       '''

       guide1=input(inp1)

       if guide1.strip().lower()=='yes':
         print(txt2_1)
  
       elif guide1.strip().lower()=='no':
           print(rep1)
    
       else:
           print(rep2)
           

       #Main Program 2
        
       try:
          num1 = int(input("Enter the number: "))
       except ValueError:
             print(rep4)
             exit()
             
       o1=input("Enter the operation: ")

       if o1.strip().lower()=='sqrt':
         print('''
   Square Root: ''',math.sqrt(num1))

       elif o1.strip().lower()=='cbrt':
           print('''
   Cube Root: ''',num1**(1/3))
         
       else:
           print(rep4)

       print(rep3)
       

    elif mode1=='2':

        #Instructions 2_2

        txt2_2='''Instructions:-

        Enter the Value of Number and Power to the
        Respective Directories.

        GOOD LUCK!!!!

        '''
        
        guide2=input(inp1)

        if guide2.strip().lower()=='yes':
          print(txt2_2)
  
        elif guide2.strip().lower()=='no':
            print(rep1)
    
        else:
            print(rep2)
            
        #Main Program 2_2
            
        try:
           num2=float(input("Enter the Number: "))
           
        except ValueError:
              print(rep4)
              exit()
        try:     
           pwr1=float(input("Enter the Power: "))
        except ValueError:
              print(rep4)
              exit()
          
        print('''
   Solution:''',pow(num2,pwr1))
        print(rep3)

    else:
        print(rep5)
      
#3.Factorials.
#============================================================================================================

def factorial():
    #Instructions 3

    txt3='''Instructions:-

    Enter the Number to Find its Factorial.

    GOOD LUCK!!!!

     '''

    guide3=input(inp1)

    if guide3.strip().lower()=='yes':
      print(txt3)
  
    elif guide3.strip().lower()=='no':
        print(rep1)
  
    else:
        print(rep2)
            
    #Main Program 3
        
    try:
       num3 = int(input("Enter the Number: "))
       
       if num3 < 0:
         print("Factorials not defined for negative numbers")
         
       elif num3 > 100:
           print("Number too large")
           
       else:
           print("Factorial:",math.factorial(num3))
        
    except ValueError:
          print("Enter Integers Only")
    
    print(rep3)

#4.Basic Trigonometry.
#============================================================================================================

def trigonometry():
    #Instructions 4

    txt4='''Instructions:-

    i)Enter the Angle
    ii)for operations,

         Type Sin, Cos, Tan, Cosec, Sec or Cot in the Operation Section.
      
    IMPORTANT NOTICE:-

        *The Solutions shown Below are in Decimal Format and Not
                in Rational Numbers.*
 
    GOOD LUCK!!!!

     '''

    
    guide4=input(inp1)

    if guide4.strip().lower()=='yes':
      print(txt4)
  
    elif guide4.strip().lower()=='no':
        print(rep1)
    
    else:
        print(rep2)
            
    #Main Program 4

    try:
       num4=float(input("Enter the Angle: "))

    except ValueError:
          print(rep4)
          exit()
    ang=math.radians(num4)

    o2=input("Enter the Trigonometric Function: ")

    if o2.strip().lower()=='sin':
      print("Sin",num4,":",math.sin(ang))

    elif o2.strip().lower()=='cos':
        print("Cos",num4,":",math.cos(ang))
        
    elif o2.strip().lower()=='tan':
        if math.cos(ang) == 0:
          print("Not Defined")
        else:
            print("Tan",num4,":",math.tan(ang))
   
    elif o2.strip().lower()=='cosec':
        if math.sin(ang)==0:
           print("Not Defined")
        else:
            print("Cosec",num4,":",1/math.sin(ang))

    elif o2.strip().lower()=='sec':
        if math.cos(ang) == 0:
          print("Not Defined")
        else:
            print("Sec",num4,":",1/math.cos(ang))

    elif o2.strip().lower()=='cot':
        if math.tan(ang) == 0:
          print("Not Defined")
        else:
            print("Cot",num4,":",1/math.tan(ang))

    else:
        print(rep4)

    print(rep3)

#5.Statistics(Ungrouped Data).
#============================================================================================================

def stats():
    #Instructions 5

    txt5='''Instructions:-

    i)Enter the Numbers as in Format:
           2 4 56.4 234 
    ii)for operations,

         Type Mean, Median, Mode, Variance or Standard Deviation
         in the Operation Section.

         
    IMPORTANT NOTICE:-

        *Please Note that this Statistics Mode is Only For Raw/Ungrouped Data.*
                  eg:- 6,5,3,7,28,4,34,5,11,56.
                  
    GOOD LUCK!!!!

     '''
    
    guide5=input(inp1)

    if guide5.strip().lower()=='yes':
      print(txt5)
  
    elif guide5.strip().lower()=='no':
        print(rep1)
     
    else:
        print(rep2)
            
    #Main Program 5

    statinp=input("Enter the Data With Spaces: ")
    try:
       statdata = list(map(float, statinp.split()))
    except ValueError:
          print("Invalid data entered")
          exit()
          
    if len(statdata) == 0:
      print("No data entered")
    else:
         o3=input("Enter the Operation: ")

         if o3.strip().lower()=='mean':
           print("Mean: ",statistics.mean(statdata))

         elif o3.strip().lower()=='median':
             print("Median: ",statistics.median(statdata))
             
         elif o3.strip().lower()=='mode':
             print("Mode: ",statistics.multimode(statdata))

         elif o3.strip().lower()=='variance':
             if len(statdata) < 2:
               print("Variance requires at least two values")
             else:
                 print("Variance: ",statistics.variance(statdata))

         elif o3.strip().lower()=='standard deviation' or o3.strip().lower()=='standarddeviation':
             print("Standard Deviation: ",statistics.stdev(statdata))
             
         else:
             print(rep4)
     
         print(rep3)


#6.Interests.
#============================================================================================================

def interests():
  
    #Choice 2
    print('''
Enter the Type of Operation:-

1.Simple Interest.
2.Compound Interest.

    ''')
    
    mode2=input("Enter Your Choice: ").strip()

    if mode2=='1':
      
      #Instructions 6_1

      txt6_1='''Instructions:-

       i)Enter the Principal amount,rate of Interest and Time Period.
       ii)Press 'Enter' and wait for the Answers.
 
      GOOD LUCK!!!!

       '''

      guide6_1=input(inp1)
  
      if guide6_1.strip().lower()=='yes':
        print(txt6_1)
  
      elif guide6_1.strip().lower()=='no':
          print(rep1)
    
      else:
          print(rep2)
            
      #main program 6_1
      try:
         prinamt=float(input("Enter the Total Principal Amount: "))
         rateint=float(input("Enter the Rate of Interest: "))
         time=float(input("Enter Time in years: "))
         
      except ValueError:
            print(rep4)
            exit()

      if prinamt<=0:
        print(val1)
        exit()
    
      if time<=0:
        print(val1)
        exit()

      simpint=(prinamt*rateint*time)/100
      amtpay=prinamt+simpint

      print("Simple Interest: ",simpint)
      print("Amount Payable",amtpay)

      print(rep3)

    elif mode2=='2':
        
        #Instructions 6_2

        txt6_2='''Instructions:-

       i)Enter the Principle amount,rate of Interest and Time Period.
       ii)Press 'Enter' and wait for the Answers.
 
      GOOD LUCK!!!!

       '''
    
        guide6_2=input(inp1)
  
        if guide6_2.strip().lower()=='yes':
          print(txt6_2)
  
        elif guide6_2.strip().lower()=='no':
            print(rep1)
    
        else:
            print(rep2)
            
        #main program 6_2
        try:
           prinamt1=float(input("Enter the Total Principle Amount: "))
           rateint1=float(input("Enter the Rate of Interest: "))
           time1=float(input("Enter Time in years: "))
           
        except ValueError:
              print(rep4)
              exit()

        if prinamt1 <= 0 or time1 <= 0:
          print(val1)
          exit()

        amtpay1=prinamt1*(1+rateint1/100)**time1
        compint=amtpay1-prinamt1

        print("Compound Interest: ",compint)
        print("Amount Payable",amtpay1)

        print(rep3)

    else:
        print(rep5)

#7.Multiplication Table.
#============================================================================================================

def multable():
    #Instructions 7

    txt7='''Instructions:-

    i)Enter the Number in the Number section and Maximum Multiplier.
    ii)Maximum multiplier- The Maximum Number of Lines to Generate in the Table.
    iii)The table will be Automatically generated in an Instant.

    GOOD LUCK!!!!

     '''
    
    guide7=input(inp1)

    if guide7.strip().lower()=='yes':
      print(txt7)
  
    elif guide7.strip().lower()=='no':
        print(rep1)
     
    else:
        print(rep2)
            
    #Main Program 7

    try:    
       mul=int(input("Enter the Number for Generating table: "))

    except ValueError:
          print(rep4)
          exit()

    try:    
       mul1=int(input("Enter the Maximum Multiplier: "))

    except ValueError:
          print(rep4)
          exit()

    print("Multiplication Table for ",mul,''':
''')
    for i in range(1,mul1+1):
       table=mul*i
       print(mul,"x",i,"=",table)

    print(rep3)

#8.Basic Geometry.
#============================================================================================================

def basicgeo():

    #Instructions 8

    txt8='''Instructions:-

    i).Follow the Instructions Given by the Software.
    ii).Enter Dimensions Wherever Required.

    IMPORTANT NOTICE:-

        *Please Ensure that the Measurements are of UNIFORM UNITS*
        **Please Check the Values Before Entering to Avoid Getting Wrong Answers**

    GOOD LUCK!!!!

     '''
    
    guide8=input(inp1)

    if guide8.strip().lower()=='yes':
      print(txt8)
  
    elif guide8.strip().lower()=='no':
        print(rep1)
     
    else:
        print(rep2)

    #Choice 3

    print('''Please select the Dimension:-

1.Two Dimensional (2-D) Shapes.
2.Three Dimensional (3-D) Shapes.

''')

    mode3=input("Enter Your Choice: ").strip()

    if mode3=='1':

      print('''Please select your Requirement:-

1.Triangular Geometry.
2.Quadrilateral Geometry.
3.Circular Geometry.
''')

      dim1=input("Enter your Requirement: ").strip()

      if dim1=='1':
        print('''Please select the Type of Triangle:-

1.Equilateral Triangle.
2.Isosceles Triangle.
3.Scalene Triangle.
''')

        tri=input("Enter the Type of Triangle: ").strip()
        
        if tri=='1':
          sideeqt=float(input("Enter the Length: "))

          peeqt=sideeqt*3
          semipeeqt=peeqt/2
          areqt=math.sqrt(3)/4*sideeqt*sideeqt

          print("Perimeter: ",peeqt)
          print("Semi Perimeter: ",semipeeqt)
          print("Area: ",areqt)

          print(rep3)

        elif tri=='2':
          
            sideorheight=input("Is Height given(Yes / No): ")
            
            if sideorheight.strip().lower()=='yes':
              
              base1=float(input("Enter the Base: "))
              height1=float(input("Enter the Height: "))
              
              eqside1=math.sqrt((base1/2)**2+height1**2)
              ariso1=0.5*base1*height1
              peiso1=base1+2*eqside1
              semipeiso1=peiso1/2

              print("Equal Side Length: ",eqside1)
              print("Perimeter: ",peiso1)
              print("Semi Perimeter: ",semipeiso1)
              print("Area: ",ariso1)

              print(rep3)

            elif sideorheight.strip().lower()=='no':

              eqside1=float(input("Enter the Equal Side Length: "))
              base1=float(input("Enter the Base: "))

              if eqside1<=base1/2:
                print(val1)

              else:
                  height1= math.sqrt(eqside1**2-(base1/2)**2)
                  ariso1=0.5*base1*height1
                  peiso1=base1+2*eqside1
                  semipeiso1=peiso1/2

                  print("Height: ",height1)
                  print("Perimeter: ",peiso1)
                  print("Semi Perimeter: ",semipeiso1)
                  print("Area: ",ariso1)

                  print(rep3)

        elif tri=='3':
            s1=float(input("Enter first Side: "))
            s2=float(input("Enter Second Side: "))
            s3=float(input("Enter Third Side: "))

            if s1+s2>s3 and s2+s3>s1 and s1+s3>s2:
              
               pesc=s1+s2+s3
               semipesc=pesc/2
               arsc = math.sqrt(semipesc*(semipesc-s1)*(semipesc-s2)*(semipesc-s3))

               print("Perimeter: ",pesc)
               print("Semi-perimeter: ",semipesc)
               print("Area: ",arsc)

               print(rep3)

            else:
                print(val1)
        else:
            print(rep5)

      elif dim1=='2':
          print('''Please select the Type of Quadrilateral:-

1.Square.
2.Rectangle.
3.Parallelogram.
4.Rhombus.
5.Trapezium / Trapezoid.
6.Kite.
''')

          quad=input("Enter the Type of Quadrilateral: ").strip()
        
          if quad=='1':
            
            sidesq=float(input("Enter the Length: "))

            pesq=sidesq*4
            arsq=sidesq*sidesq

            print("Perimeter: ",pesq)
            print("Area: ",arsq)

            print(rep3)
          
          elif quad=='2':
          
              rect1=float(input("Enter the Length 1: "))
              rect2=float(input("Enter the Length 2: "))

              perect=2*(rect1+rect2)
              arrect=rect1*rect2

              print("Perimeter: ",perect)
              print("Area: ",arrect)

              print(rep3)
  
          elif quad=='3':
          
              parabase=float(input("Enter the Base: "))
              paraside=float(input("Enter the Side Length: "))

              pepara=2*(parabase+paraside)

              print("Perimeter: ",pepara)
            
              hinfo=input("Do you Know the Height?(Yes/No): ")

              if hinfo.strip().lower()=='yes':
              
                paraheight=float(input("Enter the Height: "))
                 
                paraarea=parabase*paraheight
               
                print("Area: ",paraarea)

                print(rep3)
                
              elif hinfo.strip().lower()=='no':
                  print("Area Cannot be Calculated Without Height")
                  print(rep3)

              else:
                  print(rep5)


          elif quad=='4':
            
              rhombside=float(input("Enter the Side Length: "))

              perhomb=4*rhombside

              print("Perimeter: ",perhomb)
            
              hinfo1=input("Do you Know the Height or Diagonals?(H -(Height) / D -(Diagonals)) / No: ")

              if hinfo1.strip().lower()=='h':
                
                rhombheight=float(input("Enter the Height: "))
               
                arrhomb=rhombside*rhombheight
               
                print("Area: ",arrhomb)

                print(rep3)
                
              elif hinfo1.strip().lower()=='d':
                
                  diagrhomb1=float(input("Enter the First Diagonal: "))
                  diagrhomb2=float(input("Enter the Second Diagonal: "))
                
                  arrhomb=(diagrhomb1*diagrhomb2)/2

                  print("Area: ",arrhomb)
                
                  print(rep3)

              elif hinfo1.strip().lower()=='no':
                  print(rep3)

              else:
                  print(rep5)

          elif quad=='5':

              trasidep1 = float(input("Enter the first parallel side: "))
              trasidep2 = float(input("Enter the second parallel side: "))
              trasidenp1 = float(input("Enter the first non-parallel side: "))
              trasidenp2 = float(input("Enter the second non-parallel side: "))

              petrap=trasidep1+trasidep2+trasidenp1+trasidenp2

              print("Perimeter: ",petrap)

              hinfo2=input("Do you Know the Height?(Yes/No): ")

              if hinfo2.strip().lower()=='yes':
              
                trapheight=float(input("Enter the Height: "))
               
                artrap=0.5*(trasidep1+trasidep2)*trapheight
               
                print("Area: ",artrap)

                print(rep3)
                
              elif hinfo2.strip().lower()=='no':
                  print(rep3)

              else:
                  print(rep5)


          elif quad=='6':

              kite1=float(input("Enter the Length of First Pair of Equal Sides: "))
              kite2=float(input("Enter the Length of Second Pair of Equal Sides: "))

              pekite=2*(kite1+kite2)
              print("Perimeter: ",pekite)

              hinfo3=input("Do you Know the Height or Diagonals? (H -(Height) / D -(Diagonals) / No): ")

              if hinfo3.strip().lower()=='h':
                
                print("Height Must be Perpendicular to One Equal Side")
                
                kiteheight=float(input("Enter the Height: "))
                
                arkite=kite1*kiteheight
                
                print("Area: ",arkite)
                
                print(rep3)

              elif hinfo3.strip().lower()=='d':
              
                  diagkite1=float(input("Enter the First Diagonal: "))
                  diagkite2=float(input("Enter the Second Diagonal: "))
                
                  arkite1=0.5*diagkite1*diagkite2
                
                  print("Area: ", arkite1)
                
                  print(rep3)

              elif hinfo3.strip().lower()=='no':
                  print(rep3)
  
              else:
                  print(rep5)

      elif dim1=='3':
          print('''Please select the Type of Circular Operation:-

1.Circle.
2.Semicircle.
3.Sector.
4.Segment.
''')

          cir1=input("Enter the Type of Circular Operation: ").strip()
        
          if cir1=='1':
            
            radii1=float(input("Enter the Radius: "))

            circum= 2*math.pi*radii1
            carea=math.pi*radii1*radii1
       
            print("Circumference: ",circum)
            print("Area: ",carea)

            print(rep3)

          elif cir1=='2':
    
              radii2=float(input("Enter the Radius: "))

              scircum=math.pi*radii2+2*radii2
              sarea=0.5*math.pi*radii2*radii2

              print("Perimeter: ",scircum)
              print("Area: ",sarea)
   
              print(rep3)

          elif cir1=='3':
    
              radii3=float(input("Enter the Radius: "))
              ang1=float(input("Enter the Angle: "))

              arclen=2*math.pi*radii3*(ang1/360)
              arsec1=math.pi*radii3*radii3*(ang1/360)

              print("Arc Length: ",arclen)
              print("Area of Sector: ",arsec1)
          
              print(rep3)

          elif cir1=='4':

              radii4 = float(input("Enter the Radius: "))
              ang2=float(input("Enter the Angle: "))

              arsec2=math.pi*radii4*radii4*(ang2/360)
              artri=0.5*radii4*radii4*math.sin(math.radians(ang2))
              arseg=arsec2-artri

              print("Area of Segment: ",arseg)

              print(rep3)

          else:
              print(rep5)

      else:
          print(rep5)

    elif mode3=='2':

        print('''Please select your Figure:-

1.sphere.
2.Hemisphere.
3.Cube.
4.Cuboid.
5.Cone.
6.Cylinder.
7.Pyramid (Square Pyramid).
8.Frustum.
''')

        dim2=input("Enter the Figure Type: ").strip()
        if dim2=='1':
          
          radsph=float(input("Enter the Radius: "))
            
          spvol=(4/3)*math.pi*radsph**3
          spsa=4*math.pi*radsph**2

          print("Volume: ",spvol)
          print("Surface Area: ",spsa)
            
          print(rep3)

        elif dim2=='2':
            
            radhsph=float(input("Enter the Radius: "))
            
            hspvol=(2/3)*math.pi*radhsph**3
            hspcsa=2*math.pi*radhsph**2
            hsptsa=3*math.pi*radhsph**2

            print("Volume: ",hspvol)
            print("Curved Surface Area (CSA): ",hspcsa)
            print("Total Surface Area (TSA): ",hsptsa)
            
            print(rep3)

        elif dim2=='3':

            cuside=float(input("Enter the Side Length: "))
            
            cuvol=cuside**3
            culsa=4*cuside**2
            cutsa=6*cuside**2

            print("Volume: ",cuvol)
            print("Lateral Surface Area (LSA): ",culsa)
            print("Total Surface Area (TSA): ",cutsa)
            
            print(rep3)

        elif dim2=='4':

            lencud=float(input("Enter the Length: "))
            brthcud=float(input("Enter the Breadth: "))
            heightcud=float(input("Enter the Height: "))
            
            cudvol=lencud*brthcud*heightcud
            cudlsa=2*heightcud*(lencud+brthcud)
            cudtsa=2*(lencud*brthcud+brthcud*heightcud+heightcud*lencud)

            print("Volume: ",cudvol)
            print("Lateral Surface Area (LSA): ",cudlsa)
            print("Surface Area (TSA): ",cudtsa)
            
            print(rep3)

        elif dim2=='5':
            
            radcone=float(input("Enter the Radius of Base: "))
            heightcone=float(input("Enter the Height: "))
            
            slant=math.sqrt(heightcone**2+radcone**2)
            conevol=(1/3)*math.pi*radcone**2*heightcone
            conecsa=math.pi*radcone*slant
            conetsa=conecsa+math.pi*radcone**2

            print("Volume: ",conevol)
            print("Curved Surface Area (CSA): ",conecsa)
            print("Total Surface Area (TSA): ",conetsa)
            
            print(rep3)

        elif dim2=='6':
            
            radcyl=float(input("Enter the Radius of Base: "))
            heightcyl=float(input("Enter the Height: "))
            
            cylvol=math.pi*radcyl**2*heightcyl
            cylcsa=2*math.pi*radcyl*heightcyl
            cyltsa=cylcsa+2*math.pi*radcyl**2

            print("Volume: ",cylvol)
            print("Curved Surface Area (CSA): ",cylcsa)
            print("Total Surface Area (TSA): ",cyltsa)
            
            print(rep3)

        elif dim2=='7':
            
            basepyr=float(input("Enter the Base Side Length: "))
            heightpyr=float(input("Enter the Height: "))
            
            slant1=math.sqrt((basepyr/2)**2+heightpyr**2)
            pyrvol=(1/3)*basepyr**2*heightpyr
            pyrlsa=2*basepyr*slant1
            pyrtsa=basepyr**2+pyrlsa

            print("Volume: ",pyrvol)
            print("Lateral Surface Area (LSA): ",pyrlsa)
            print("Total Surface Area (TSA): ",pyrtsa)
            
            print(rep3)

        elif dim2=='8':
            
            frurad1=float(input("Enter the Radius of Larger Base: "))
            frurad2=float(input("Enter the Radius of Smaller Base: "))
            fruheight=float(input("Enter the Height: "))
            
            slant2=math.sqrt(fruheight**2+(frurad1-frurad2)**2)
            fruvol=(1/3)*math.pi*fruheight*(frurad1**2+frurad2**2+frurad1*frurad2)
            frucsa=math.pi*(frurad1+frurad2)*slant2
            frutsa=frucsa+math.pi*(frurad1**2+frurad2**2)
            
            print("Volume: ",fruvol)
            print("Curved Surface Area (CSA): ",frucsa)
            print("Total Surface Area (TSA): ",frutsa)
            
            print(rep3)

        else:
            print(rep5)

    else:
        print(rep5)
    
#Execute Functions
          
if mode=='1':
  basiccalc()

elif mode=='2':
    expops()
    
elif mode=='3':
    factorial()

elif mode=='4':
    trigonometry()
    
elif mode=='5':
    stats()
    
elif mode=='6':
    interests()
     
elif mode=='7':
    multable()
    
elif mode=='8':
    basicgeo()

else:
    print(rep5)
