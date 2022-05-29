import keyboard
import pyautogui as pag
from pynput import mouse
def on_click(x, y, button, pressed):
    if pressed and tumbler == True and button == mouse.Button.left:
        pag.moveRel(0, 100, 2)
listener = mouse.Listener(on_click=on_click)
listener.start()
tumbler = False
while True:
    keyboard.wait("v")
    if tumbler == False:
        tumbler = True
        print("Макросы работают")
    else:
        tumbler = False
        print("Макросы не работают")
