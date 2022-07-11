import pyautogui
import time
import keyboard
import win32api, win32con

print("|##################################################|")
print("|          Boas-vindas ao AurumtailBot!            |")
print("|          Por favor, verifique se tudo            |")
print("|          está de acordo com o guia.              |")
print("|                                                  |")
print("|    Para encerrar o programa, feche está janela.  |")
print("|##################################################|")

print("\nO programa logo iniciará, minimize esta tela antes dele prosseguir...")

time.sleep(7)

def click(x, y):
    win32api.SetCursor(x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


print("\nPrograma iniciado!")

Combate = False
Barragem = False
Ouro = False
Testes = 0

### FARMAR MANTIS

while keyboard.is_pressed("q") == False:
    while Combate == False:
        Mantis = False
        start = time.time()
        while time.time() - start < 2:
            if pyautogui.locateOnScreen('Images-PTBR\\Mantis_Body.png', confidence=0.7) != None:
                Mantis = True
                if Mantis == True:
                    start = 2
            else:
                print("Mantis não localizada.")

        if Mantis == True:
    #        walk_direction("d")
            print("Localizado!")
            start = time.time()
            while time.time() - start < 1.5: # Mantém o comando por 2 segundos.
                pyautogui.keyDown("right")
            pyautogui.keyUp("right")
            print("Combate Iniciado!")
            Combate = True
        else:
#            print("Mantis não localizada!")
            contador_2 = 0
            pyautogui.press('esc') # Abre o menu
            time.sleep(0.2)
            pyautogui.press('enter') # Abre Inventário
            time.sleep(0.2)
            pyautogui.press('right') # Vai para Consumíveis
            time.sleep(0.2)
            btn_sin = pyautogui.locateOnScreen('Images-PTBR\\Sino_de_Monstro.png', confidence=0.7)
            btn_sin_e = pyautogui.center(btn_sin)
            pyautogui.click(btn_sin_e.x, btn_sin_e.y)
            print("Sino de monstro alcançado.")
            # Tem um problema, se estiver na outra página o sino, ele dá dois enters e quebra tudo.
            while contador_2 != 2:
                pyautogui.press('enter')
                time.sleep(0.2)
                contador_2 += 1

    if pyautogui.locateOnScreen('Images-PTBR\\Iniciar_Combate.png', confidence=0.7) != None:
            pyautogui.press('enter')
            time.sleep(3)
            Barragem = True

    while Barragem == True:
        if pyautogui.locateOnScreen('Images-PTBR\\Barragem_de_Gemas.png', confidence=0.7) != None:
                    btn = pyautogui.locateOnScreen('Images-PTBR\\Barragem_de_Gemas.png', confidence=0.7)
                    btn_e = pyautogui.center(btn)
                    time.sleep(0.3)
                    print("Clicado na Barragem de Gemas")
                    pyautogui.click(btn_e.x, btn_e.y)
                    pyautogui.press('enter')
                    pyautogui.press('enter')
                    time.sleep(4)
                    pyautogui.press('enter')
                    Barragem = False
                    print("Combate Feito!")
                    Ouro = True
        else:
            print("Barragem não localizada.")

    if Ouro == True:
        if pyautogui.locateOnScreen('Images-PTBR\\Bonus_Ouro.png', confidence=0.5) != None:
                    contador = 0
                    while contador != 4:
                        pyautogui.press('enter')
                        time.sleep(0.2)
                        contador += 1
                    Combate = False
                    Ouro = False
                    Testes = Testes + 1
                    print(Testes)
        else:
                print("Ainda localizando...")