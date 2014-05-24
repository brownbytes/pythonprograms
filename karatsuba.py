####
'''
name: durga
algorithm : karatsuba multiplication

recursive algorithm

x,y are 2 numbers of len n to be multiplied
x = 1234 ; y = 5678
a =12 , b = 34 ; c = 56 , d = 78

x = 10^(n/2)*a + b => 1200+34 = 1234
y = 10^(n/2)*c + d => 5600+78 = 5678

 (quotient *dividor + reminder)

   a = x/(10**n/2))
   b = x%(10**n/2))

   c = y/(10**n/2))
   b = y%(10**n/2))


x can be partioned to a & b ,by divding x by 10^(len(x)/2) ; quotient = a , reminder = b

thus x * y = (10^(n/2)*a + b) * (10^(n/2)*c + d)
            = 10^n*ac + 10^(n/2)(ad + bc) + bd
            = 10^n*ac + 10^(n/2)((a+b)(c+d)-ad-bd) + bd

this process can be repeated till a basecase is met. such as x,y being single digits and no futher breakdown can work.
this algorithm also stands for divide and conquer methods .
'''
####

import math

product = 0
def mult(x,y): # inputs for the function
    global product
    n = int(len(str(x)))
    if n > 1:
        a = x/10**(n/2)
        b = x%10**(n/2)
        c = y/10**(n/2)
        d = y%10**(n/2)
        ac = mult(a,c)
        bd = mult(b,d)
        abcd = mult((a+b),(c+d)) - ac - bd       
        product = 10**(n) * ac + 10**(n/2)*abcd + bd

    elif n == 1:
        product = x * y

    return product
    
print mult(1234,5678)
    

           
