
try:
    age = int(input("Hur gammal är du?"))
    height = int(input("Hur lång är du i cm?"))

    if age >= 6:
        print("Du är tillräckligt gammal")
    elif age < 6:
        print("Du är för ung")

    if height >= 140:
        print("Du är tillräckligt lång")
    elif height < 140:
        print("Du är inte tillräckligt lång")

except:
    print("Error")

try:
    name = input("Skriv ditt namn") #Standard input av "input" är string
    age = input("Skriv din ålder") #Standard input av "input" är string
    print("Välkommen", name)
    print("Du är", age, "år gammal")

except:
    print("Error")


try:
    vikt = int(input("Hur mycket väger du i kg?"))
    längd = int(input("Hur lång är du i cm?"))
    längd2 = längd / 100
    längd3 = längd2 ** 2
    bmi = vikt//längd3
    print("Din bmi är ", bmi)

except:
    print("Error")


try:
    radie = int(input("Vad är radien?"))
    cirkel_area = radie * radie * 3.14
    print("Arean på cirkeln är ", cirkel_area, "cm^2")
except:
    print("Error")

try:
    import random
    dice = random.randint(1,6)
    print("Tärningen slog", dice)

    kast = int(input("Hur många tärningare"))

    for i in range(kast):
        print("kast", i+1, "Blev", random.randint(1,6))

except:
    print("Error")