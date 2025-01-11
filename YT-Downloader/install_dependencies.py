# install_dependencies.py
import subprocess
import sys
import os

def instalar_dependencias(opcion):
    try:
        if opcion == 1:
            # Instalar requerimientos desde requirements.txt
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
            print("Dependencias instaladas correctamente!")
        elif opcion == 2:
            # Instalar requerimientos desde requirements.txt para IOS (iSH Shell)
                     # Obtener la ruta del directorio actual
            dir_actual = os.path.dirname(os.path.abspath(__file__))
            requirements_path = os.path.join(dir_actual, "requirements.txt")
            
            # Usar pip3 explícitamente
            print("Actualizando pip...")
            subprocess.check_call(["pip3", "install", "--upgrade", "pip"])
            
            print(f"Instalando dependencias desde: {requirements_path}")
            subprocess.check_call(["pip3", "install", "-r", requirements_path])
            print("Dependencias instaladas correctamente!")
        else:
            print("Opción no válida")
            sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Error instalando dependencias: {e}")
        sys.exit(1)

if __name__ == "__main__":
    opcionUsr = int(input("¿Qué desea hacer?\n1. Instalar dependencias MAC \n2. Instalar dependencias IOS (iSH Shell) \n"))
    print(opcionUsr)
    instalar_dependencias()