from pygame import image, Color

moveimage = image.load() #tutaj wstawimy plik

def check_move_point(gracz):
    move_x, move_y = 0, 0
    if gracz.keys_active["right"]:
        move_x = 1
    if gracz.keys_active["up"]:
        move_y = -1
    if gracz.keys_active["left"]:
        move_x = -1
    if gracz.keys_active["down"]:
        move_x = 1

    if moveimage.get_at((int(gracz.x+move_x), int(gracz.y+move_y-80)))  != Color("black"):
        return False
    return True
