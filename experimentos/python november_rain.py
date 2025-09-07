import sys
import time

CYAN = "\033[36m"
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"

# Esconder/mostrar cursor
HIDE_CURSOR = "\033[?25l"
SHOW_CURSOR = "\033[?25h"

def printLyrics():
    lines = [
        ("When I look into your eyes", 3.5),
        ("I can see a love restrained", 4.0),
        ("But darlin' when I hold you", 3.8),
        ("Don't you know I feel the same?", 2.0),
        ("Nothin' lasts forever", 2.80),
        ("And we both know hearts can change", 4.5),
        ("And it's hard to hold a candle", 3.8),
        ("In the cold November rain", 6.0),
    ]

    # Esconde cursor
    sys.stdout.write(HIDE_CURSOR)
    sys.stdout.flush()

    for lyric, delay in lines:
        print(CYAN + lyric + RESET)
        time.sleep(delay)

    # Mostra cursor de volta
    sys.stdout.write(SHOW_CURSOR)
    sys.stdout.flush()

def main():
    print(GREEN + "--- INICIANDO LETRA SINCRONIZADA: NOVEMBER RAIN ---" + RESET)
    printLyrics()
    print(RED + "--- FIM DA LETRA ---" + RESET)

if __name__ == "__main__":
    main()
