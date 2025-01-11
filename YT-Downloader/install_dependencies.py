# install_dependencies.py
import subprocess
import sys

def instalar_dependencias():
    try:
        # Actualizar pip primero
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        
        # Instalar requerimientos desde requirements.txt
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Dependencias instaladas correctamente!")
    except subprocess.CalledProcessError as e:
        print(f"Error instalando dependencias: {e}")
        sys.exit(1)

if __name__ == "__main__":
    instalar_dependencias()