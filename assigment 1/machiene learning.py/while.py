  
# i = 1
# while i <= n:
#     print(i)
#     i += 1
# i=1
# n=int(input("enter any number:"))
# while(i<=5):
#     t=n*i
#     print(n,"x",i,"=",t)
#     i=i+1

# i=1
# n=int(input("enter no:"))
# while(n>0):
#     r=n%10
#     print(r,end=" ")
#     n=n//10

# i=1
# while(i<=6):
#  j=1
#  while(j<=i):
#      print(j,end="")
#      j=j+1
#  i=i+1
#  print()    

# i=1
# while(i<=4):
#  j=2
#  while(j<=8):
#    print(j,end="")
#    j=j+2
#  print()
#  i=i+1 

# i=5
# while(i>=1):
#  j=1
#  while(j<=i):
#     print(j,end="")
#     j=j+1
#  print()
#  i=i-1  

for i in range(0,6):
  for j in range(5,i,-1):
    print(j,end="")
  print()  
