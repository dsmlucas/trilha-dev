import sys
from rich import print 
from time import sleep

def printLyrics():
    lines = [
        ("I wanna da-", 6.06), #1
        ("I wanna dance in the lights", 0.5), #2
        ("I wanna ro-", 0.7), #3
        ("I wanna rock your body", 8.68), #4
        ("I wanna go", 0.8), #5
        ("I wanna go for a ride", 0.68), #6
        ("Hop in the music and", 0.7), #7
        ("Rock your body", 0.8), #8
        ("Rock that body", 0.869), #9
        ("come on, come on", 0.35), #10
        ("Rock that body", 0.5), #11
        ("(Rock your body)", 0.3), #12
        ("Rock that body", 0.49), #13
        ("come on, come on", 0.35), #14
        ("Rock that body", 0.8), #15
    ]

    for lyric, delay in lines:
        print(f"[bold cyan]{lyric}[/bold cyan]")
        sleep(delay)

def main():
    print("[bold green]--- INICIANDO LETRA SINCRONIZADA ---[/bold green]\n")
    printLyrics()
    print("\n[bold red]--- FIM DA LETRA ---[/bold red]")
 
if __name__ == "__main__":
    main()

print("[bold red]Erro![/bold red] Algo deu errado!")
print("[green]Tudo certo![/green]")
