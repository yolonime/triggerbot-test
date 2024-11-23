#import libs for the auto click

from mss import mss
from ctypes import WinDLL
from keyboard import *





# Obtenir les dimensions de l'écran
user32 = WinDLL("user32", use_last_error=True)
WIDTH, HEIGHT = 1920, 1080  # Valeurs par défaut
print ("Largeur de l'écran:", WIDTH)
print ("Hauteur de l'écran:", HEIGHT)
def click():
    user32.mouse_event(2, 0, 0, 0, 0)
    user32.mouse_event(4, 0,0 ,0, 0)
    

def main():
    print ("Début du programme")
    with mss() as sct:
        while True:
            click()

main()