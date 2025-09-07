import sys
import time

CYAN = "\033[36m"
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"

# Códigos para esconder/mostrar cursor
HIDE_CURSOR = "\033[?25l"
SHOW_CURSOR = "\033[?25h"

def printLyrics():
    lines = [
    ("I wanna da-", 1.10),
    ("I wanna dance in the lights", 1.70),
    ("I wanna ro-", 1.33),
    ("I wanna rock your body", 2.40),
    ("I wanna go", 2.6),
    ("I wanna go for a ride", 1.30),
    ("Hop in the music and", 1.90),
    ("Rock your body", 1.60),
    ("Rock that body", 1.60),
    ("come on, come on", 1.60),
    ("Rock that body", 2.00),
    ("(Rock your body)", 2.00),
    ("Rock that body", 1.80),
    ("Come on, come on", 1.70),
    ("Rock that body", 1.80),
]

    # Esconder cursor
    sys.stdout.write(HIDE_CURSOR)
    
    sys.stdout.flush()

    for lyric, delay in lines:
        print(CYAN + lyric + RESET)
        time.sleep(delay)

    # Mostrar cursor de volta
    sys.stdout.write(SHOW_CURSOR)
    sys.stdout.flush()

def main():
    print(GREEN + "--- INICIANDO LETRA SINCRONIZADA ---" + RESET)
    printLyrics()
    print(RED + "--- FIM DA LETRA ---" + RESET)
 
if __name__ == "__main__":
    main()
