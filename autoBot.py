import pyautogui 
import time

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.

def spamDiscord(targetName: str, message: str):
    # Déplacer la souris vers les coordonnées Discord
    pyautogui.moveTo(1289, 1628)
    time.sleep(0.5)
    
    # Minimiser toutes les fenêtres
    pyautogui.hotkey('win', 'd')
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
    pyautogui.moveTo(1066, 1510)
    pyautogui.leftClick()
    time.sleep(0.2)

    counter = 76
    while(counter > 0):
        pyautogui.write(message)
        pyautogui.press('enter')
        time.sleep(0.2)
        pyautogui.press('enter')
        counter -= 1


def getPos():
    try:
        while True:
            time.sleep(5)
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
            return positionStr
    except KeyboardInterrupt:
        print('\n')


spamDiscord("Thomas", "Es-tu sisra ? 😘")