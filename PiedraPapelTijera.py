nombre1 = input("¿Como se llamara el jugador 1?: ")
nombre2 = input("¿Como se llamara el jugador 2?: ")

puntaje_jugador1 = 0
puntaje_jugador2 = 0

while puntaje_jugador1 < 2 and puntaje_jugador2 < 2:
    Jugador1 = input("¡Hola " +nombre1+ "! ¿Que eliges? ¿Piedra, Papel o Tijera?: ").lower()
    Jugador2 = input("¡Hola " +nombre2+ "! ¿Que eliges? ¿Piedra, Papel o Tijera?: ").lower()

    condicion1 = Jugador1 == "piedra" and Jugador2 == "tijera"
    condicion2 = Jugador1 == "papel" and Jugador2 == "piedra"
    condicion3 = Jugador1 == "tijera" and Jugador2 == "papel"

    if Jugador1 == Jugador2:
        print("¡Ha sido un empate!")
    elif condicion1 or condicion2 or condicion3:
        print ("¡Ha ganado: ", nombre1,"!")
        puntaje_jugador1 += 1
    else:
        print("¡ Ha ganado: ", nombre2,"!")
        puntaje_jugador2 += 1

if puntaje_jugador1 == 2:
    print("¡" +nombre1+ "ha ganado el mejor de 3!")
else:
    print("¡" +nombre2+ "ha ganado el mejor de 3!")