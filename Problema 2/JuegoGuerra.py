import random

# Definición de la clase Carta
class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo

    def __str__(self):
        return f"{self.valor}{self.palo}"

# Definición de la clase Cola (estructura de datos de cola)
class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            return None

    def tamano(self):
        return len(self.items)

# Definición de la clase Mazo
class Mazo:
    def __init__(self):
        self.cartas = []

    def crear_mazo(self):
        try:
            valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
            palos = ['\u2660', '\u2663', '\u2665', '\u2666']
            self.cartas = [Carta(valor, palo) for valor in valores for palo in palos]
        except Exception as e:
            print("Error al crear el mazo:", str(e))

    def mezclar(self):
        try:
            random.shuffle(self.cartas)
        except Exception as e:
            print("Error al mezclar el mazo:", str(e))

# Definición de la clase Jugador
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = Cola()

    def agregar_cartas_al_final(self, cartas):
        for carta in cartas:
            self.mano.encolar(carta)

# Definición de la clase JuegoGuerra
class JuegoGuerra:
    def __init__(self, jugador1, jugador2):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.mazo = Mazo()
        try:
            self.mazo.crear_mazo()
            self.mazo.mezclar()
        except Exception as e:
            print("Error al iniciar el juego:", str(e))
        
        self.turno = 0

    def imprimir_mano(self, carta1, carta2):
        print("=" * 80)
        print(f"Turno: {self.turno}")
        print(f"Jugador 1:")
        for _ in range(self.jugador1.mano.tamano()):
            print("-X", end=' ')
        print("\nJugador 2:")
        for _ in range(self.jugador2.mano.tamano()):
            print("-X", end=' ')
        print(f"\nCartas comparadas: {str(carta1)} vs {str(carta2)}")

    def comparar_cartas(self, carta1, carta2):
        valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        try:
            valor1 = valores.index(carta1.valor)
            valor2 = valores.index(carta2.valor)
            return valor1 - valor2
        except ValueError:
            print("Error al comparar cartas. Valor no encontrado.")
            return 0

    def mostrar_cartas_enfrentadas(self, carta1, carta2, tributo):
        espacio = " " * 6
        if tributo:  # Verificar si hay cartas en tributo (guerra)
            linea_jugador1 = " ".join(f"{carta.valor}{carta.palo}" for carta in tributo[:2])
            print("\n" + espacio + linea_jugador1 + "-X -X -X -X -X -X ")

    def jugar_ronda(self):
        try:
            self.turno += 1

            if self.jugador1.mano.esta_vacia():
                print("¡Jugador 1 se ha quedado sin cartas!")
                print("¡Jugador 2 gana la partida!")
                return
            elif self.jugador2.mano.esta_vacia():
                print("¡Jugador 2 se ha quedado sin cartas!")
                print("¡Jugador 1 gana la partida!")
                return

            carta1 = self.jugador1.mano.desencolar()
            carta2 = self.jugador2.mano.desencolar()

            resultado = self.comparar_cartas(carta1, carta2)

            self.imprimir_mano(carta1, carta2)
            self.mostrar_cartas_enfrentadas(carta1, carta2, [])

            if resultado > 0:
                self.jugador1.agregar_cartas_al_final([carta1, carta2])
                print(f"Jugador 1 gana la ronda.")
            elif resultado < 0:
                self.jugador2.agregar_cartas_al_final([carta2, carta1])
                print(f"Jugador 2 gana la ronda.")
            else:
                print("\n" + " " * 8 + "***GUERRA***")
                tributo = []
                for _ in range(3):  # Cambio a 3 para cada jugador
                    if not self.jugador1.mano.esta_vacia():
                        tributo.append(self.jugador1.mano.desencolar())
                    if not self.jugador2.mano.esta_vacia():
                        tributo.append(self.jugador2.mano.desencolar())

                if len(tributo) < 6:
                    # No hay suficientes cartas para una guerra completa
                    print("No hay suficientes cartas para una guerra completa.")
                    print("¡Jugador 2 gana la partida!")
                    return

                mesa = [carta1, carta2] + tributo

                self.imprimir_mano(carta1, carta2)
                self.mostrar_cartas_enfrentadas(None, None, mesa)

                carta1_volteada = self.jugador1.mano.desencolar() if not self.jugador1.mano.esta_vacia() else None
                carta2_volteada = self.jugador2.mano.desencolar() if not self.jugador2.mano.esta_vacia() else None

                if carta1_volteada and carta2_volteada:
                    resultado = self.comparar_cartas(carta1_volteada, carta2_volteada)

                    self.imprimir_mano(carta1_volteada, carta2_volteada)
                    self.mostrar_cartas_enfrentadas(carta1_volteada, carta2_volteada, [])

                    if resultado > 0:
                        guerra_resultado = [carta1, carta2] + tributo + [carta1_volteada, carta2_volteada]
                        self.jugador1.agregar_cartas_al_final(guerra_resultado)
                        print(f"Jugador 1 gana la guerra.")
                    else:
                        guerra_resultado = [carta2, carta1] + tributo + [carta2_volteada, carta1_volteada]
                        self.jugador2.agregar_cartas_al_final(guerra_resultado)
                        print(f"Jugador 2 gana la guerra.")
                else:
                    tributo.extend(mesa)
                    self.jugador1.agregar_cartas_al_final([carta1] + tributo + [carta2])
                    print(f"Jugador 1 gana la guerra por falta de cartas.")
        except Exception as e:
            print("Error al jugar la ronda:", str(e))

    def jugar(self, max_turnos):
        try:
            while not self.jugador1.mano.esta_vacia() and not self.jugador2.mano.esta_vacia() and self.turno < max_turnos:
                self.jugar_ronda()

            print("=" * 80)
            if self.turno == max_turnos:
                print("¡Empate! Se ha alcanzado el máximo de turnos.")
            elif not self.jugador1.mano.esta_vacia():
                print("¡Jugador 1 gana la partida!")
            else:
                print("¡Jugador 2 gana la partida!")
        except Exception as e:
            print("Error al jugar la partida:", str(e))

# Crear dos jugadores
try:
    jugador1 = Jugador("Jugador 1")
    jugador2 = Jugador("Jugador 2")
except Exception as e:
    print("Error al crear los jugadores:", str(e))
    exit(1)

# Crear el juego de Guerra
try:
    juego = JuegoGuerra(jugador1, jugador2)
except Exception as e:
    print("Error al crear el juego:", str(e))
    exit(1)

# Repartir cartas
mazo = Mazo()
try:
    mazo.crear_mazo()
    mazo.mezclar()
except Exception as e:
    print("Error al crear o mezclar el mazo:", str(e))
    exit(1)

# Repartir las cartas a cada jugador
try:
    for i in range(0, len(mazo.cartas), 4):
        for j in range(3):
            juego.jugador1.mano.encolar(mazo.cartas[i + j])

        for j in range(3, 4):
            juego.jugador2.mano.encolar(mazo.cartas[i + j])
except Exception as e:
    print("Error al repartir las cartas:", str(e))
    exit(1)

# Jugar la partida con un máximo de 1000 turnos.
try:
    juego.jugar(max_turnos=1000)
except Exception as e:
    print("Error al jugar la partida:", str(e))
