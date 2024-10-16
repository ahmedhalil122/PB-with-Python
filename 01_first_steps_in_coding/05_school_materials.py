pens = int(input())*5.80
markers = int(input())*7.20
cleaning_liquid = int(input())*1.20
discount_amount = int(input())/100

total_materials_cost = pens+markers+cleaning_liquid

print(total_materials_cost-(total_materials_cost*discount_amount))