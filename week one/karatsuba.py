'''
Author: Tafseer Ahmed
Date: 5/30/2017
Language: Python 3.6.0 :: Anaconda 4.3.1 (64-bit)
'''

def kar(x, y):
    nx=len(str(x))
    ny=len(str(y))
    if nx==1 or ny==1:
        return int(x)*int(y)
    p=10**(int(nx/2))
    q=10**(int(ny/2))
    a=int(x/p)
    b=int(x%p)
    c=int(y/q)
    d=int(y%q)
    return ( 10**((nx+ny)/2) *(kar(a,c)) + ( kar(a,d)*10**(nx/2) + kar(b,c)*10**(ny/2) + kar(b,d) ))

p=3141592653589793238462643383279502884197169399375105820974944592

q=2718281828459045235360287471352662497757247093699959574966967627
print(kar(int(p),int(q)))    
