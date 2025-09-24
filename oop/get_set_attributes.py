class Pet:
    def __init__(self, name, category, breed = None, age = 0):
        self._name = name
        self.__category = category
        self.__breed = breed
        self.age = age
        self.__ccard = 'unknown'
        self.vaccinated = False
        self.weight = 0
    
    def get_weight(self):
#Function get_weight returns the value of the weight attribute
        return self.weight
    
    def set_weight(self, new_weight):
#First component checks that the value of new_weight is actually a number, otherwise returning a message to the user saying that the weight needs to be an integer
        if type(new_weight) == int or type(new_weight) == float:
#Second component checks that the value of weight is a positive number because you can't have negative weight. It similarly returns a message to the user saying that weight needs to be positive.
            if new_weight > 0:
#Upon meeting all parameters, the weight gets set to the new value
                self.weight = new_weight
            else:
                print("Please enter a positive number for weight")
        else:
            print("Please enter a number for weight")
