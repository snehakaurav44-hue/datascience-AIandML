calls = int(input("enter the number of calls:"))

bill = 250

if calls > 100:
    extra_calls = calls - 100
    bill = bill + (extra_calls * 1.25)


print("total bill",bill)