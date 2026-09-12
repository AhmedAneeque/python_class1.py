<<<<<<< HEAD
import math
a,b,c=map(int,(input("Enter value of a,b and c :").split()))
d=b**2-4*a*c
print(f"Determinant={d}")
if d>0 :
    r1=(-b+math.sqrt(d))/(2*a)
    r2=(-b-math.sqrt(d))/(2*a)
elif d==0:
    r1=r2=-b/(2*a)
else:
    real=-b/(2*a)
    imag=math.sqrt(-d)/(2*a)
    r1 = complex(real, imag)
    r2 = complex(real, -imag)

    

=======
import math
a,b,c=map(int,(input("Enter value of a,b and c :").split()))
d=b**2-4*a*c
print(f"Determinant={d}")
if d>0 :
    r1=(-b+math.sqrt(d))/(2*a)
    r2=(-b-math.sqrt(d))/(2*a)
elif d==0:
    r1=r2=-b/(2*a)
else:
    real=-b/(2*a)
    imag=math.sqrt(-d)/(2*a)
    r1 = complex(real, imag)
    r2 = complex(real, -imag)

    

>>>>>>> d9ee51f0cc5c114ccd731eff574942c21419d1af
print(f"Roots are {r1}and {r2}")