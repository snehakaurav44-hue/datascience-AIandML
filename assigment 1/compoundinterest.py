p = float(input("enter pricipal:"))
t = float(input("enter time:"))
r = float(input("enter rate:"))

a = p*(1+r/100)**t

ci = (a-p)

print("compound interest=",ci)