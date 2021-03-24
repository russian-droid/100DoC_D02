#following Udemy course: 100 days of code by Angela Yu
#tip calculator

print ('\n\n-------WELCOME TO THE TIP CALCULATOR-------')
total = float(input ('What was the total bill?\n'))
persons = int(input ('How many poeple will split the bill?\n'))
tip_percent = int(input ('What percentage tip would you like to give: 10, 12 or 15?\n'))

if tip_percent == 10:
    tip_percent = 0.1
elif tip_percent == 12:
    tip_percent = 0.12
elif tip_percent == 15:
    tip_percent = 0.15
else:
    print ('INCORRECT NUMBER!')

to_pay = total / persons + (tip_percent* total/persons)
to_pay=round(to_pay,2)#round to the second decimal

print('Each person should pay: $' + str(to_pay) + ' (including the tip)')
print(f'Each person should pay: ${to_pay} (including the tip)')


--------------BMI calculator
print ('\n\n-------WELCOME TO THE BMI CALCULATOR-------')
weight = float(input ('enter the weight in kg?\n'))
height = float(input ('enter the height in cm\n'))
BMI = weight / height * height
print(int(BMI))
