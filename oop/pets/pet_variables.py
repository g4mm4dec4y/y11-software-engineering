name = 'Bonnie'
animal_category = 'Cat'
age = 3
vaccinated = True
ccard = '3423 2326 7543 1234'
billing_address = '17 Park Drive, The Shire 2695'
owner_name = 'Alex Ngyuen'
account_balance = 129.95

age += 1
billing_address = billing_address.replace("drive", "street")
vaccinated = not True
prompt = input("Update your credit card details: ")
ccard = ccard.replace("3423 2326 7543 1234", prompt)
owner_name = owner_name.replace("Ngyuen", "Jones")
account_balance = account_balance - 25
