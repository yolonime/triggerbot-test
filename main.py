import numpy as np
from mss import mss
from ctypes import WinDLL
import time

# Obtenir les dimensions de l'écran
user32 = WinDLL("user32", use_last_error=True)
WIDTH, HEIGHT = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

# Définir une zone de capture de 1x1 pixel au centre de l'écran
CENTER_PIXEL = {
    "top": int(HEIGHT / 2),
    "left": int(WIDTH / 2),
    "width": 1,
    "height": 1
}

def main():
    with mss() as sct:
        while True:
            # Capture un seul pixel au centre de l'écran
            img = np.array(sct.grab(CENTER_PIXEL))[:, :, :3]  # Récupère uniquement les valeurs RGB

            # Le pixel capturé est la couleur du centre
            pixel_color = img[0, 0]  # Couleur du pixel unique au centre

            # Affiche la couleur du pixel au centre de l'écran
            print("Couleur du pixel central:", pixel_color)

            time.sleep(0.1)  # Légère pause pour réduire l'utilisation du processeur

main()
