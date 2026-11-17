customer_no = input("enter customer number:")
units_consumed = float(input("enter units consumed:"))

if units_consumed <= 200:
    bill_amount = units_consumed * 0.5

elif units_consumed <= 400:
    bill_amount = 100 + (units_consumed - 200) * 0.65

elif units_consumed <= 600:
    bill_amount = 230 + (units_consumed - 400) * 0.8

else:
    bill_amount =  230 + (200 * 0.8) + (units_consumed - 600) * 0.8

    print("customer number:", customer_no)
    print("bill amount:", bill_amount)