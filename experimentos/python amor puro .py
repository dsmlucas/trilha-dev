import sys
import time

CYAN = "\033[36m"
GREEN = "\033[32m"
RESET = "\033[0m"

HIDE_CURSOR = "\033[?25l"
SHOW_CURSOR = "\033[?25h"

BPM = 132
BEAT = 60 / BPM

def printLyrics():
    lines = [
        # COLE A LETRA AQUI, LINHA POR LINHA
        ("[Te adoro em tudo, tudo,tudo]", 4 * BEAT),
        ("[Quero mais que tudo, tudo, tudo]", 3 * BEAT),
        ("[Te amar sem limites]", 5 * BEAT),
        ("[Viver uma grande história]", 4 * BEAT),
    ]

    sys.stdout.write(HIDE_CURSOR)
    sys.stdout.flush()

    for lyric, delay in lines:
        print(CYAN + lyric + RESET)
        time.sleep(delay)

    sys.stdout.write(SHOW_CURSOR)
    sys.stdout.flush()

def main():
    print(GREEN + "--- INÍCIO ---" + RESET)
    printLyrics()
    print(GREEN + "--- FIM ---" + RESET)

if __name__ == "__main__":
    main()
