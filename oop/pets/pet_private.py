class Pet:
    def __init__(self, name, category, breed = None, age = 0):
        self._name = name
        self.__category = category
        #The breed attribute is already here with a double underscore, maning it is private
        self.__breed = breed
        self.age = age
        self.__ccard = 'unknown'
        self.vaccinated = False

    def have_birthday(self):
        self.age += 1

    def __str__(self):
        payment_status = 'unregistered'
        if len(self.__ccard) == 19:
            payment_status = 'registered'

        my_status = 'Name: ' + self._name +'\nCategory: ' + self.__category + '\nAge: ' + str(self.age) +'\nPayment status: ' + payment_status + '\nVaccinated: '+ str(self.vaccinated)
        return my_status

p1 = Pet(name = 'Bonnie', category = 'Cat', age = 10)
#Attempting to change the category of p1 to dog
p1.__category = "dog"
print(p1)
#The print statement returns the initial Cat value instead of the dog value I attempted to change it to
