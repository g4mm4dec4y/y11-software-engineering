class Pet:
    def __init__(self, name, category, age = 0):
        self.name = name
        self.category = category
        self.age = age
        self.ccard = 'unknown'
        self.vaccinated = False
        self.account_balance = 0
    
    def have_birthday(self):
        self.age += 1

#Sets the vaccination attribute to be true to signify that the pet is now vaccinated
    def vaccinate(self):
        self.vaccinated = True

#Function simply sets the balance to equal 0, thus clearing any previous values
    def clear_balance(self):
        self.account_balance = 0

#Function check what kind of animal the pet is and accordingly multiplies the age to get the human age
    def human_age(self):
        if self.category == "dog":
            print("Human age:", self.age*7)
        if self.category == "cat":
            print("Human age:", self.age*6)

#Establishing a pet for testing purposes
p1 = Pet("Piper", "dog", 3)

#This tests whether the human age function returns a correct value, which it does.
Pet.human_age(p1)
