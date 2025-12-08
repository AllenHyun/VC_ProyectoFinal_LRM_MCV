import socket
import json
import keyboard
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = {
    "move_x": None,
    "jump": 0,
    "shoot": 0
}


while True:
    data = {
        "move_x": None,
        "jump": 0,
        "shoot": 0
    }
    pressed = False

    if keyboard.is_pressed('a'):
        data["move_x"] = ["izquierda", 5]
        pressed = True
    elif keyboard.is_pressed('d'):
        data["move_x"] = ["derecha", 5]
        pressed = True

    if keyboard.is_pressed('space'):
        data["jump"] = 1
        pressed = True

    if keyboard.is_pressed('ctrl'):
        data["shoot"] = 1
        pressed = True

    if pressed is True:
        payload = json.dumps(data).encode('utf-8')
        sock.sendto(payload, ("127.0.0.1", 6005))
        time.sleep(0.1)
        print("Enviado:", payload)
        

    if keyboard.is_pressed('esc'):
        break