import pygame

title="Chessino"
version = 1.0
voices = ["sofy", "lucho"]
voice = voices[0]
keys= {
    "menu": pygame.K_RETURN,
    "white": pygame.K_q,
    "whiteRead": pygame.K_a,
    "black": pygame.K_w,
    "blackRead": pygame.K_s,
}

# buttons arduino:
# debe indeicarse el pin de conexión.
# si es None no está asignado.
buttons  = {
    "menu": 8,
    "white": 7,
    "whiteRead": 4,
    "black": 6,
    "blackRead": 5,
}
# si no está conectado un display arduino, poner en False para que utilice print en consola.
display = True
logs = True
