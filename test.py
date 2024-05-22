from picamera2 import Picamera2

def enregistrer_video(duree):
    picam2 = Picamera2()
    picam2.start_and_record_video("video.mp4", duration=duree)
    
if __name__ == "__main__":
    duree_video = 15  # durée en secondes
    enregistrer_video(duree_video)
