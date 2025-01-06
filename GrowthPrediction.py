import numpy as np
import matplotlib.pyplot as plt

# Datos conocidos
dias = [1, 2, 4]
alturas = [5, 10, 20]

# Valores a estimar
dia_interpolar = 3  # Dentro del rango (Interpolación)
dia_extrapolar = 5  # Fuera del rango (Extrapolación)

# Interpolación
altura_interpolada = np.interp(dia_interpolar, dias, alturas)

# Extrapolación (usando una aproximación lineal)
# Extendemos la línea entre los últimos dos puntos
pendiente = (alturas[-1] - alturas[-2]) / (dias[-1] - dias[-2])
altura_extrapolada = alturas[-1] + pendiente * (dia_extrapolar - dias[-1])

# Resultados
print(f"Altura estimada en el día {dia_interpolar} (Interpolación): {altura_interpolada:.2f} cm")
print(f"Altura estimada en el día {dia_extrapolar} (Extrapolación): {altura_extrapolada:.2f} cm")

# Gráfica
plt.plot(dias, alturas, 'bo-', label='Datos conocidos')
plt.plot(dia_interpolar, altura_interpolada, 'go', label='Interpolación')
plt.plot(dia_extrapolar, altura_extrapolada, 'ro', label='Extrapolación')
plt.legend()
plt.xlabel('Día')
plt.ylabel('Altura (cm)')
plt.title('Interpolación vs Extrapolación')
plt.show()