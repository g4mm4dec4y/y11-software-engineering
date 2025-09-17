class Car:
    def __init__(self,make,model,year, for_sale = 'Not for sale', price=None):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.for_sale = for_sale

    def __str__(self):
        return '| Make: '+self.make+' | Model: '+self.model+' | Status: '+self.for_sale+' |'

c1 = Car('Mazda','6',2005)
c2 = Car('Holden', 'Captiva', 2016)
c3 = Car('BMW', 'Series 1', 2004, 'For sale')
c4 = Car('BMW', 'Series 4', 2013, 'For sale')

cars = [c1, c2, c3, c4]

for car in cars:
    print(car)