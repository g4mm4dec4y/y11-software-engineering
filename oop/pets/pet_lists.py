pet_name = ["Pet name: Foxy", "Pet name: Moxy", "Pet name: Roxy"]
species = ["Species: Dog", "Species: Cat", "Species: Parrot"]
age = ["Age: 8", "Age: 9", "Age: 10"]
vaccination_status = ["Vaccination Status: False", "Vaccination Status: False", "Vaccination Status: True"]

data = [pet_name, species, age, vaccination_status]

#The following block adds a new pet according to entered information.
def new_pet (name, type, years, vaccine):
    pet_name.append(name)
    species.append(type)
    age.append(years)
    vaccination_status.append(vaccine)

#The following block replaces "unvaccinated" with "vaccinated" thus vaccinating a pet
def vaccination (refnumber):
    vaccination_status[refnumber] = "Vaccination Status: True"

#Calls on function to add the new pet to all the lists
new_pet("Pet name: Hootie", "Species: Blowfish", "Age: 34", "Vaccination status: Unknown")

#This block removes a specific pet determined by a reference number
def remove_pet(refnumber):
    for list in data:
        del list[refnumber]

remove_pet(1)

num = int(input("Reference number: "))
vaccination(num)

print(data)
