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
            print("Вы сдохли!")
            os.remove("//main.py")
            break
        else:
            print("Вы победили!")
            break
    else:
        break