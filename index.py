from robolink import Robolink  # Importa el módulo de conexión con RoboDK
from robodk import *    # Importa la librería de funciones matemáticas

# Inicializa la conexión con RoboDK
RDK = Robolink()

# Obtiene el brazo robótico en el espacio de trabajo (asegúrate de que el nombre coincida)
robot = RDK.Item('Nombre_del_Brazo_Robotico')

# Define las posiciones iniciales y finales de las articulaciones
pos_inicial = [90, 90, 0]  # [anguloHombro, anguloCodo, anguloPinza]
pos_final = [120, 45, 90]  # [anguloHombro, anguloCodo, anguloPinza]

# Define la velocidad de movimiento de las articulaciones (en grados por segundo)
velocidad = 30

# Mueve el brazo robótico a la posición inicial
robot.MoveJ(pos_inicial, velocidad)

# Mueve el brazo robótico a la posición final
# robot.MoveJ(pos_final, velocidad)
