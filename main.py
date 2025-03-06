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
#https://prod.liveshare.vsengsaas.visualstudio.com/join?0B5E853D5291899D4C10B834F53D763F7EA0