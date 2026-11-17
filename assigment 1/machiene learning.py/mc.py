import numpy as np 
x= [34,108,64,88,99,51]
y= [5,17,11,8,14,5]
print(x)
print(y)

# SUM
sox=np.sum(x)
soy=np.sum(y)
print(sox)
print(soy)

# MEAN
s=np.mean(x)
t=np.mean(y)
print(s)
print(t)
for i in x:
 i=(x-s)
print(i)
for f in y:
    f=(y-t)
print(f)

# PRODUCT
product = (i*f)
print(product)

# SQUARE
for j in x:
  j=(x-s)**2
print(j) 
sx=np.sum(i*f)
print(sx)

# SUM/SQUARE
ssq=np.sum(j)
print(ssq)

# SLOPE
#       ∑(xi-x̄)(yi-ȳ)
#  b1= ________________
#         ∑(xi-x̄)²
b1=sx/(ssq)
print(b1)

# INTERCEPT
b0 = ȳ - b1x̄ 

b0 = (t)-(b1*s)
print(b0)

# # RELATION
# r=(b0)+(b1*s)
# print(r)

# COFFICENT OF CORRELATION
print(x)
print(y)
print(sox)
print(soy)
print (sox*soy)
print(sox**2)
print(soy**2)
n=len(self.__x)
r=(n*sox*soy-sox*soy)/np.sqrt((n*sox*x-sox*sox) * (n*soy*y*soy))
print("cofficient of correltion:",r)