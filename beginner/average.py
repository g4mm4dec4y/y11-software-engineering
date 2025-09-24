counter = 0
values = []

while counter <998:
    counter = counter + 1
    number = input("Enter a number: ")
    if number:
        values.append(int(number))
    else: break   
 

total = sum(values)
amount = len(values)
average = total / amount
print ("There were", amount, "numbers inputted, the average of which is ", average)


