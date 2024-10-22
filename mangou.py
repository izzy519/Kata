def Mangos(MangosBuyed,PricePmango):
    FreeMangos = MangosBuyed // 3
    TotalMangos = FreeMangos + MangosBuyed
    RealPricePmango = MangosBuyed * PricePmango / TotalMangos
    return RealPricePmango

MangosBuyed = int(input("Mangos comprados "))
PricePmango = float(input("Precio por mango "))

mangos2 = Mangos(MangosBuyed,PricePmango)

print (mangos2)