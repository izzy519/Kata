def Solicitud(Cap,Pa,Ps):
    Pa2 = Pa + Ps - Cap
    if Pa2 < 0: 
        print(f"Los {Ps} pasajeros en espera pueden entrar")
    else:
        print(f"no hay espacio para {Pa2} pasajeros")

Cap = int(input("Capacidad del bus "))
Pa = int(input("Pasajeros abordo "))
Ps = int(input("Pasajeros esperando subir "))

Solicitud(Cap,Pa,Ps)