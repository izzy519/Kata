def hero (Bullets, Dragons):
    if Dragons == 0:
        return True
    elif Bullets / Dragons >= 2:
        return True
    else:
        return False

bullets = int(input("munición "))
Dragons = int(input("dragones "))

if hero (bullets,Dragons) == True:
    print("El heroe sobrevive ")
else:
    print("El heroe Muere ")

