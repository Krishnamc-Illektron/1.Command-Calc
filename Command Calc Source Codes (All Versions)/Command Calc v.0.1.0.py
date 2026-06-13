
#Python Calc

def calc(o):
   if o=='+':
     print("Addition:",a+b)
   elif o=='-':
       print("Subtraction:",a-b)
   elif o=='x':
       print("Multiplication:",a*b)
   elif o=='/':
       print("Division:",a/b)
   elif o=='//':
       print("Floor Division:",a//b)
   elif o=='mod':
       print("Modulus:",a%b)
   elif o=='exp':
       print("Exponential:",a**b)
   else:
       print ("invalid")
       
#Main Program
txt1='''for Operations,

Addition:'+'           Subtraction:'-'
Multiplication:'x'     Division:'/'
Floor Division:'//'    Modulus:'mod'
Exponential:'exp'
'''

print(txt1)

a=int(input("Enter A:"))
o=input("Operation:")
b=int(input("Enter B:"))
calc(o)
