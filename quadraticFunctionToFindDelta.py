import math
print ('For quadratic function ax2+bx+c=0')
a = int(input("give a   "))
b = int(input("give b   "))
c = int(input("give c   "))
delta = int((b*b)-(4*a*c))
if delta > 0:
    x1 = (-b + math.sqrt(delta) / (2*a))
    x2 = (+b + math.sqrt(delta) / (2*a))
    print(('first result x1 = '), x1, ('second resultx2 = '), x2, )
elif delta == 0:
    x0 = -b / (2*a)
    print('there is one result x0 = '), x0
    
else:
    print(('no result in reason the delta is negative '), delta)
    
    
