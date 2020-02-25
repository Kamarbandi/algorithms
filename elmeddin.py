import random
reqem = random.randint(0, 100)

def checkIt(prompt):
    counter = 0

    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if value == reqem:
            counter += 1
            print(f'* Tebrikler!!! Siz ' + str(counter) + ' cehd ile qalib oldunuz *')
            break
        elif value < reqem:
            counter += 1
            print('-- Coxalt --')
            continue
        elif value > reqem:
            counter += 1
            print('-- Azalt -- ')
            continue

        elif value < 0:
            counter += 1
            print("Sorry, your response must not be negative.")
            continue

    return value

checkIt(' 0 ile 100 arasi reqem secin')