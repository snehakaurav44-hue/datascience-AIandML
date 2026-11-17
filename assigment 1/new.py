r=float(input("enter rate:"))
q=float(input("enter quantity:"))
amt=r*q
print("amount:",amt)
if(amt>=100000):
    dis=20
elif(amt>=500000 and amt<=999999):
    dis=10
else:
    dis=5
print("discount:",dis,"%")
disamt=amt*dis/100
print("discount amount:",disamt)
na=amt-disamt
print("net amount:",na)
