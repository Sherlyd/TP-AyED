import datetime
import time
import random

class Paciente:
    def __init__(self):
        self.nombre = self.generar_nombre()
        self.riesgo = self.generar_riesgo()

    def generar_nombre(self):
        nombres = ['Andrea', 'Antonio', 'Estela', 'Gastón', 'Jorge', 'Leandro', 'Mariela', 'Agustina']
        apellidos = ['Lopez', 'Juarez', 'Rodriguez', 'García', 'Belgrano', 'Perez', 'Colman', 'Mendez']
        nombre_completo = random.choice(nombres) + ' ' + random.choice(apellidos)
        return nombre_completo

    def generar_riesgo(self):
        # 1: crítico, 2: moderado, 3: bajo
        return random.randint(1, 3)

    def get_riesgo(self):
        return self.riesgo

    def __str__(self):
        riesgo_str = '1-crítico' if self.riesgo == 1 else '2-moderado' if self.riesgo == 2 else '3-bajo'
        return f"{self.nombre} -> {riesgo_str}"

class ColaEspera:
    def __init__(self):
        self.pacientes = []

    def agregar(self, paciente):
        self.pacientes.append(paciente)
        self.pacientes.sort(key=lambda x: x[0])  # Ordenar por riesgo (el primer elemento de la tupla)

    def extraer(self):
        if self.pacientes:
            return self.pacientes.pop(0)  # Sacar al paciente más antiguo
        else:
            return None

if __name__ == "__main__":
    n = 10  # Número de pacientes a simular

    # Crear una cola de espera vacía
    cola_de_espera = ColaEspera()

    # Ciclo que gestiona la simulación
    for i in range(n):
        # Fecha y hora de entrada de un paciente
        ahora = datetime.datetime.now()
        fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
        print('*--*--*--*--*--*--*--*--*--*--*--*--*--*--*-\n')
        print(f"{fecha_y_hora}\n")

        # Se crea un paciente un paciente por segundo
        # La criticidad del paciente es aleatoria
        paciente = Paciente()
        # Almacenar el paciente en la cola de prioridad con el nivel de riesgo como clave
        cola_de_espera.agregar((paciente.get_riesgo(), paciente))

        # Atención de paciente en este ciclo
        if random.random() < 0.5:
            # Se atiende al paciente que se encuentra al frente de la cola
            paciente_atendido = cola_de_espera.extraer()
            if paciente_atendido:
                print('*' * 40)
                print('Se atiende el paciente:', paciente_atendido[1])
                print('*' * 40)
        else:
            # Se continúa atendiendo al paciente del ciclo anterior
            pass

        # Mostrar pacientes restantes en la cola de espera
        print("Pacientes en espera:")
        for paciente_en_espera in cola_de_espera.pacientes:
            print(paciente_en_espera[1])

        # Imprimir la cantidad de pacientes que faltan por atender
        print('Pacientes que faltan atenderse:', len(cola_de_espera.pacientes))

        print()
        print('*--*--*--*--*--*--*--*--*--*--*--*--*--*--*-')

        time.sleep(1)

    # Después de atender a todos los pacientes en la simulación inicial, se atienden a los pacientes restantes
    while cola_de_espera.pacientes:
        paciente_atendido = cola_de_espera.extraer()
        if paciente_atendido:
            print('*' * 40)
            print('Se atiende el paciente:', paciente_atendido[1])
            print('*' * 40)

        # Mostrar pacientes restantes en la cola de espera
        print("Pacientes en espera:")
        for paciente_en_espera in cola_de_espera.pacientes:
            print(paciente_en_espera[1])

        # Imprimir la cantidad de pacientes que faltan por atender
        print('Pacientes que faltan atenderse:', len(cola_de_espera.pacientes))

        time.sleep(1)



