import numpy as np
from mss import mss
from ctypes import WinDLL
from keyboard import *





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

def main():
    print ("Début du programme")
    with mss() as sct:
        while True:
            # Capture un seul pixel au centre de l'écran
            img = np.array(sct.grab(CENTER_PIXEL))[:, :, :3]  # Récupère uniquement les valeurs RGB
            #print("Couleur du pixel central:", img)
            # Le pixel capturé est la couleur du centre
            pixel_color = img[0, 0]  # Couleur du pixel unique au centre
            #if np.array_equal(pixel_color, [106, 219, 75]): 
            #IF COULEUR VIOLETTE AVEC DE LA TOLERANCE
            if np.all(np.abs(pixel_color - [250, 100, 250]) < 70):
                
                # La souris se déplace au centre de l'écran
                    # user32.SetCursorPos(int(WIDTH / 2), int(HEIGHT / 2))
                    # print("La couleur du pixel central est [75, 219, 106]")
                # simule un clic de espace

                #print("Clic de souris")
                try :
                    press_and_release('p')
                    
                except Exception as e:
                    print(e)


                #appuyer sur la touche "espace" avec user 32 et keybd_event
                
                



main()