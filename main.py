from postac import Gracz
from event import Event #IMPORT EVENTÓW
import pgzrun
from pgzero.screen import Screen
from pgzero.builtins import Actor, keyboard

WIDTH = 800
HEIGHT = 600
keys: keyboard
screen: Screen
gracz = Gracz(keys)
event= Event() #INICJALIZACJA KLASY

#mapa kolorowa, to tylko nakładka 
color_map = Actor('map1a', pos = (400,300), achor = (0, 0)) #pos=(0, 60) coś tu się psuje

def draw():
    screen.fill((0, 0, 0))
    color_map.draw()
    event.draw()  # RYSOWANIE EVENTÓW
    gracz.draw(screen)





def on_key_down(key):
    gracz.on_key_down(key)


def on_key_up(key):
    gracz.on_key_up(key)

def updatebyevent(): #sprawdzanie kolizji na bieżąco
    if gracz.move_pressed(): #jeżeli jest naciśnięty jakiś klawisz
        event.kolizja(gracz.gracz)


def update():
    gracz.update()
    updatebyevent()


pgzrun.go()

