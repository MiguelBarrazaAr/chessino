import pygame

title="Chessino"
version = 1.0
voice = "sofy"
keys= {
    "start": pygame.K_RETURN,
    "white": pygame.K_q,
    "whiteRead": pygame.K_a,
    "black": pygame.K_w,
    "blackRead": pygame.K_s,
}

# buttons arduino:
# debe indeicarse el pin de conexión.
# si es None no está asignado.
buttons  = {
    "start": None,
    "white": None,
    "whiteRead": None,
    "black": None,
    "blackRead": None,
}
