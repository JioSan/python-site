import random
import os
print("Русская рулетка")
bullets = random.randint(1, 7)
bullet = random.randint(1, 7)

while True:
    print("Вы готовы? Да/Нет")
    answer = input()
    if answer == "Да":
        if bullets == bullet:
            print("")
            break
        else:
            print("Вы победили!")
            break
    else:
        break
#https://prod.liveshare.vsengsaas.visualstudio.com/join?7E47BCA9C3A218D4414B7956B62977FA7503
