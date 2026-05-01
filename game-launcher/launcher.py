import datetime
import subprocess
import os

# Obtener fecha actual
hoy = datetime.datetime.now()

# Rutas de los ejecutables (ajústalas si hace falta)
ruta_normal = os.path.join(os.getcwd(), "FiveNightsatFreddys4.exe")
ruta_halloween = os.path.join(os.getcwd(), "HalloweenEdition.exe")

# Comprobar si es Halloween (31 de octubre)
if hoy.month == 10 and hoy.day == 31:
    subprocess.Popen(ruta_halloween)
else:
    subprocess.Popen(ruta_normal)