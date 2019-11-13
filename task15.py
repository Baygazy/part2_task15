my_old = int(input('Твой возраст?: '))
if my_old % 2 != 0:
    for number in range(1, my_old+1):
        if number % 2 != 0:
            print(number)

else:
    for number in range(1, my_old+1):
        if number % 2 == 0:
            print(number)