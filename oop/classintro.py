class Pet:

    def __init__(self, name, category, age):
        self.name = name
        self.category = category
        self.age = age

    vaccinated = False
    ccard = "unknown"
    billing_address = "unknown"
    owner_name = "unknown"
    account_balance = 0
        
pet1 = Pet("Bonnie", "Cat", 3)

print(pet1.vaccinated)

pet2 = Pet("Foxy", "Dog")
