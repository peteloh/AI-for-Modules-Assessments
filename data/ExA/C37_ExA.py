import numpy as np
#import the function we need
a=np.matrix([[0,0 ,0, 0, 0, 0, 0, 0],[0,2, 0, 0, 0, 0, 2, 0],[0 ,0 ,3 ,0, 0 ,3 ,0 ,0],[0 ,0, 0, 4, 4, 0, 0, 0],[0 ,0 ,0 ,5 ,5 ,0 ,0 ,0 ],[0 ,0, 6, 0, 0, 6, 0, 0],[0 ,7 ,0 ,0 ,0 ,0 ,7 ,0],[8 ,0, 0, 0, 0, 0 ,0, 8]]);
b=np.matrix([[0,2,3,4,5,6,7,8]]);
d=np.transpose(a)
#calculate (A - traverseA)first to avoid mistakes
e=a-d
c=np.dot(b,e)
print(c)
#print the answer