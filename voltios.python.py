print("Determinar el potencial electrico a 0.5cm de una carga cuyo valor electrico es de 13pC dentro de un campo electrico.")
  
q1 = 12 * 10 ** (-9)  # Valor de la carga eléctrica
r = 0.14  # Distancia de la carga
k = 9 * 10 ** 9  # Valor de la constante de Coulomb

def variable():
  print("La carga electrica es: " + str(q1))

variable()

def variable():
  print("La distancia es: " + str(r))

variable()

def constante():
  print("La constante es: " + str(k))

constante()

voltaje = (k * q1) / r  # Fórmula para calcular el voltaje

print("El potencial eléctrico es: " + str(voltaje))

#MUCHAS GRACIAS!!!!!!