def CatDog(humanYears):
    CatYears = humanYears * 4 + 16
    DogYears = humanYears * 5 + 16
    return CatYears, DogYears

humanYears = int(input("Años humanos "))

CatYears, DogYears = CatDog(humanYears)


print(f"tu gato tiene {CatYears} años de edad y tu perro tiene {DogYears} de edad ")