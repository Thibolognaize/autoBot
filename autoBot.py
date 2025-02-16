import pyautogui 
import time
import keyboard  # Ajout du module keyboard

screenWidth, screenHeight = pyautogui.size()

def spamDiscord(targetName: str, message: str):
    # Minimiser toutes les fenêtres
    pyautogui.hotkey('win', 'd')
    time.sleep(0.5)
    
    # Déplacer la souris vers les coordonnées Discord
    pyautogui.moveTo(1435, 1413)
    time.sleep(0.5)

    # Cliquer pour ouvrir Discord
    pyautogui.click()
    time.sleep(0.5)
    
    # Ouvrir la recherche
    pyautogui.hotkey('ctrl', 'k')
    time.sleep(0.5)
    
    # Écrire le nom et valider
    pyautogui.write(targetName)
    time.sleep(0.5)
    pyautogui.press('enter')

    # Rentrer dans le chat
    pyautogui.moveTo(939, 1339)
    pyautogui.leftClick()
    time.sleep(0.2)

    counter = 76
    print("Programme en cours d'exécution. Appuyez sur 'q' pour arrêter.")
    
    while counter > 0:
        # Vérifier si 'q' est pressé
        if keyboard.is_pressed('q'):
            print("\nProgramme arrêté par l'utilisateur")
            return  # Sortir de la fonction
            
        pyautogui.write(message)
        pyautogui.press('enter')
        time.sleep(0.2)
        pyautogui.press('enter')
        counter -= 1

spamDiscord("Blacki77", "Eh oui c'est moi")