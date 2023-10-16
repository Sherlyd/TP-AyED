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
        self.pacientes.sort(reverse=True)  # Ordenar de mayor a menor riesgo

    def extraer(self):
        if self.pacientes:
            return self.pacientes.pop(0)  # Cambiado a pop(0) para sacar al paciente más antiguo
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
        paciente_atendido = cola_de_espera.extraer()
        if paciente_atendido:
            # Se atiende al paciente más crítico
            paciente_atendido = paciente_atendido[1]
            print('*' * 40)
            print(str(paciente_atendido))
            print('*' * 40)

        print()
        print('*--*--*--*--*--*--*--*--*--*--*--*--*--*--*-')

        time.sleep(1)



