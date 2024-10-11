import numpy as np
c=np.array([[1,1,-4],[0,1,3]])
d=np.array([[3,1,4],[-2,0,5]])
c1=np.array([2*c+5*d])
c2=np.array([c-3*d])
print(c1,c2)