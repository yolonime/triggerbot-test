import numpy as np
from mss import mss
from ctypes import WinDLL
import keyboard
import time

# Obtenir les dimensions de l'écran
user32 = WinDLL("user32", use_last_error=True)
WIDTH, HEIGHT = 1920, 1080  # Valeurs par défaut
print ("Largeur de l'écran:", WIDTH)
print ("Hauteur de l'écran:", HEIGHT)

# Définir une zone de capture de 1x1 pixel au centre de l'écran
CENTER_PIXEL = {
    "top": int(HEIGHT / 2),
    "left": int(WIDTH / 2),
    "width": 1,
    "height": 1
}

def tir():
    user32.mouse_event(2, 0, 0, 0, 0)
    user32.mouse_event(4, 0, 0 ,0, 0)
    print("tir")

# recupere la couleure du pixel central lorsque la touche "ctrl"st appuyée
def trigger():
    with mss() as sct:
        # Capture un seul pixel au centre de l'écran
        img = np.array(sct.grab(CENTER_PIXEL))[:, :, :3]  # Récupère uniquement les valeurs RGB
    return img  # Couleur du pixel unique au centre

def main():
    print ("Début du programme")
    while True:
        #attendre que la touche "a" soit appuyée
        if keyboard.is_pressed('a'):
            #recupere la couleur du pixel central
            pixel_color = trigger()
            print(pixel_color)
            while keyboard.is_pressed('a'):
                new_pixel_color = trigger()
                if not np.array_equal(new_pixel_color, pixel_color):
                    tir()
                    time.sleep(0.5)
                    
            
        else:
            pass
        
        
            
            
main()

