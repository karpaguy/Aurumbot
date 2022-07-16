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

time.sleep(2)

def Cursor():
    win32api.SetCursorPos((10,10))

def click(ps_x, ps_y):
    win32api.SetCursorPos((ps_x, ps_y))
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def menu_open():
    pyautogui.press('esc')
    time.sleep(0.3)
    pyautogui.press('enter')
    time.sleep(0.3)
    pyautogui.press('right')


print("\nPrograma iniciado!")

Combate = False
Barragem = False
Ouro = False
Testes = 0
cxy = False


### LOCALIZAR POSIÇÃO DO SINO DE MONSTRO

menu_open()

while cxy == False:
    if pyautogui.locateOnScreen('assets\\Images-PTBR\\SinoBorder.png', confidence=0.90) != None:
        print('Achei')
        blx, bly = pyautogui.locateCenterOnScreen('assets\\Images-PTBR\\SinoBorder.png', confidence=0.85)
        cxy = True
    else:
        pyautogui.press('down')
        print('Ainda localizando...')

print(blx)
print(bly)

# Fechar o menu
pyautogui.press('esc')
pyautogui.press('esc')

### FARMAR MANTIS

while keyboard.is_pressed("q") == False:
    while Combate == False:
        Mantis = False
        start = time.time()
        while time.time() - start < 2:
            if pyautogui.locateOnScreen('assets\\Images-PTBR\\Mantis_Body.png' or 'assets\\Images-PTBR\\Mantis_Body_Alt.png' , confidence=0.7) != None:
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
        else: # Utiliza um sino de monstro.
            print("Pegando sino!")
            menu_open()
            print(blx)
            print(bly)
            click(blx, bly)
            time.sleep(0.2)
            pyautogui.press('enter')

    if pyautogui.locateOnScreen('assets\\Images-PTBR\\Iniciar_Combate.png', confidence=0.7) != None:
            pyautogui.press('enter')
            time.sleep(0.5)
            Barragem = True

    while Barragem == True:
        if pyautogui.locateOnScreen('assets\\Images-PTBR\\Barragem_de_Gemas.png', confidence=0.95) != None:
                    btnx, btny = pyautogui.locateCenterOnScreen('assets\\Images-PTBR\\Barragem_de_Gemas.png', confidence=0.95)
                    time.sleep(0.3)
                    print("Clicado na Barragem de Gemas")
                    click(btnx, btny)
                    pyautogui.press('enter')
                    pyautogui.press('enter')
                    time.sleep(3.8)
                    pyautogui.press('enter')
                    Barragem = False
                    print("Combate Feito!")
                    Ouro = True
        else:
            print("Barragem não localizada.")

    if Ouro == True:
        if pyautogui.locateOnScreen('assets\\Images-PTBR\\Bonus_Ouro.png', confidence=0.5) != None:
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

print("Não há mais sinos restantes ou o programa falhou.")

print('Hic')