import sys
import time

# Cores ANSI
CYAN = "\033[36m"
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"

# Códigos para esconder/mostrar o cursor
HIDE_CURSOR = "\033[?25l"
SHOW_CURSOR = "\033[?25h"

def printLyrics():
    lines = [
        ("Ainda não dance como se não fosse minha (minha, minha, minha)", 4.0),
        ("Ainda não dance como se não fosse minha", 3.0),
        ("Eu sei que o problema sou eu, amor, eu sei que a culpa é minha", 4.5),
        ("Mas, por favor, ainda não dance como se não fosse minha", 4.0),
        ("Eu sabia, ia ser nossa última dança (nossa última dança)", 5.0),
        ("Foi embora sem eu ver, igual a minha infância", 4.0),
        ("Só me liga quando ela quer transa", 3.0),
        ("Deu saudade, então ela me chama", 3.5),
        # Continue com outras partes conforme desejar
        ("Então, pela última vez eu te digo, garota", 4.5),
        ("Dance, dance", 2.0),
        ("Só não dance como se não fosse minha (minha, minha, minha)", 4.0),
        ("Ainda não dance como se não fosse minha", 3.0),
    ]

    # Esconde o cursor
    sys.stdout.write(HIDE_CURSOR)
    sys.stdout.flush()

    for lyric, delay in lines:
        print(CYAN + lyric + RESET)
        time.sleep(delay)

    # Mostra o cursor de volta
    sys.stdout.write(SHOW_CURSOR)
    sys.stdout.flush()

def main():
    print(GREEN + "--- INICIANDO A ÚLTIMA DANÇA (KARAOKÊ) ---" + RESET)
    printLyrics()
    print(RED + "--- FIM DA LETRA ---" + RESET)

if __name__ == "__main__":
    main()

