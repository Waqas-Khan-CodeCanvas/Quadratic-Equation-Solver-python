# quadratic equation
# ax**2+by+c=0

import cmath
print("General Form :-  ax**2 + bx + c =0")

a=int(input("Enter a (a!=0):"))
b=int(input("Enter b :"))
c=int(input("Enter c :"))

d=(b**2)-(4*a*c)

sol1=(-b-cmath.sqrt(d))/(2*a)
sol2=(-b+cmath.sqrt(d))/(2*a)

print("/n")
print(f"result for equation ,{a}x**2 + {b}x + {c} = 0 are:- /n")
#
if d>0:
    print("type of root :two distinct real roots")
elif d==0:
    print("type of root :two equal real roots")
elif d<0:
    print("type of root :two complex real roots")


print(f"the solution are {sol1} and {sol2}")

