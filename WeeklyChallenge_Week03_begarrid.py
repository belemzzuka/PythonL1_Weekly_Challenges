print("##################### Expense Calculator #####################")
monthly_income = float(input("Monthly income:"))
monthly_purchases = input("Monthly purchases:")
concepts = []
amounts = []
total = 0
for number in range(int(monthly_purchases)):
    concept = input("Concept:")
    concepts.append(concept)
    amount = float(input("Amount:"))
    amounts.append(amount)
    total += amount
print("*********************** Expense Report ***********************")
for number in range(int(monthly_purchases)):
    concepts_length = len(concepts[number])
    amounts_length = len(str(amounts[number]))
    dots = 62 - concepts_length - amounts_length
    print(f'{concepts[number]}{"." * dots}{amounts[number]}')
print("--------------------------------------------------------------")
total_left = str(monthly_income-total)
left_length = len(total_left)
spacing = 62 - left_length - 10
print(f'Money left{" " * spacing}{total_left}')