import os
from datetime import datetime
from picamera2 import Picamera2

def enregistrer_video(duree):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    home_dir = os.path.expanduser("~")
    base_path = os.path.join(home_dir, "Desktop", "database")
    os.makedirs(base_path, exist_ok=True)
    
    fichier = os.path.join(base_path, f"video_{timestamp}.mp4")

    picam2 = Picamera2()
    video_config = picam2.create_video_configuration(main={"size": (2592, 2592)})

    print(f"Enregistrement de la vidéo pendant {duree} secondes...")

    # Start the camera with the video configuration
    picam2.configure(video_config)
    picam2.start()

    # Record the video
    picam2.start_recording(fichier)
    picam2.wait_recording(duree)
    picam2.stop_recording()

    print(f"Enregistrement terminé. Vidéo sauvegardée sous {fichier}")

if __name__ == "__main__":
    duree_video = 15  # durée en secondes
    enregistrer_video(duree_video)