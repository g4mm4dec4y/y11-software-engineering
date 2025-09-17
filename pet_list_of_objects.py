class Pet:
    def __init__(self, name, category, age = 0):
        self.name = name
        self.category = category
        self.age = age
        self.ccard = 'unknown'
        self.vaccinated = False

p1 = Pet('Bonnie', 'Cat', 0)
p2 = Pet('Clyde', 'Dog', 7)
p3 = Pet('Star', 'Rabbit', 4)
#New pet
p4 = Pet(category = 'Parrot', age = 9, name = 'Ruby')

pets = [p1, p2, p3, p4]

#Vaccinate all the pets in the list
for pet in pets:
    pet.vaccinated = True

#Test the first pet to see if the variable has effectively changed
print(p1.vaccinated)