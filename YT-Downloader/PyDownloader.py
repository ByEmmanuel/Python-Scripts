import yt_dlp
from pathlib import Path
import os

def descargar_video(url):
    # Obtener la ruta de la carpeta "Descargas"
    ruta_descargas = Path(os.path.expanduser('~/Downloads'))

    # Verificar si la carpeta existe; si no, crearla
    if not ruta_descargas.exists():
        print("Creando carpeta 'Descargas'...")
        ruta_descargas.mkdir(parents=True, exist_ok=True)

    opciones = {
        'format': 'best',  
        'outtmpl': str(ruta_descargas / '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegVideoRemuxer',
            'preferedformat': 'mp4',  
        }],
        'merge_output_format': 'mp4',
        'ignoreerrors': True,
        'verbose': True  # Para ver más información durante la descarga
    }
    
    try:
        with yt_dlp.YoutubeDL(opciones) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            print(f"Archivo guardado como: {filename}")
    except Exception as e:
        print(f"Error al descargar el video: {str(e)}")

if __name__ == "__main__":
    enlace = input("Introduce el enlace de YouTube: ")
    descargar_video(enlace)