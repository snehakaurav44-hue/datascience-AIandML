days = int(input("enter no. of days:"))

years = days // 365
remaining_days = days % 365
weeks = remaining_days // 7
days_left = remaining_days % 7

print("years=",years)
print("remaining_days=",remaining_days)
print("weeks=",weeks)
print("days=",days)
print("days_left=",days_left)
