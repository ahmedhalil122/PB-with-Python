amount_deposited = int(input())
term_of_deposit = int(input())
annual_interest_rate = float(input())

accured_interest = amount_deposited*(annual_interest_rate/100)
interest_per_month = accured_interest/12
total = amount_deposited+(term_of_deposit*interest_per_month)
print(total)