import time
import os
from datetime import datetime
import picamera
import subprocess

def enregistrer_video(duree):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    home_dir = os.path.expanduser("~")
    base_path = os.path.join(home_dir, "Desktop", "database")
    os.makedirs(base_path, exist_ok=True)
    
    fichier_h264 = os.path.join(base_path, f"video_{timestamp}.h264")
    fichier_mp4 = os.path.join(base_path, f"video_{timestamp}.mp4")

    with picamera.PiCamera(resolution=(2592, 2592)) as camera:
        camera.start_preview()
        camera.start_recording(fichier_h264)
        print(f"Enregistrement de la vidéo pendant {duree} secondes...")
        time.sleep(duree)
        camera.stop_recording()
        camera.stop_preview()

    print(f"Conversion de {fichier_h264} en {fichier_mp4}...")

    # Conversion h264 -> mp4
    commande_ffmpeg = f"ffmpeg -r 30 -i {fichier_h264} -c:v copy {fichier_mp4}"
    subprocess.run(commande_ffmpeg, shell=True)

    os.remove(fichier_h264)

    print(f"Enregistrement terminé. Vidéo sauvegardée sous {fichier_mp4}")

if __name__ == "__main__":
    duree_video = 15  # durée en secondes
    enregistrer_video(duree_video)
