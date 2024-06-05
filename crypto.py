import os
import sys

modos = {"d": "Descriptografar",
         "c": "Cryptografar"}

modo = ""
caminho = ""
chave = ""

#Metodo (multi OS) para limpar o console
def clear():
    os.system('cls' if os.name=="nt" else "clear")
    titulo()

#Metodo que vai definir o modo de execução, Cryptografar ou Descryptografar
def escolherModo(tipo):
    global modo

    if tipo == "-d":
        modo = "d"
        print(f"Modo : {modos[modo]}" )
        return
    elif tipo == "-c":
        modo = "c"
        print(f"Modo : {modos[modo]}" )
        return
    
    opcao1 = input("(D)escriptografar , (C)riptografar , (S)air ? : ").lower()

    if opcao1 == "s" or opcao1 == "q":
        print("Saindo")
        sys.exit()
    elif opcao1 != "d" and opcao1 != "c":
        clear()
        print("Opção inválida ótario, tente novamente!")
        return escolherModo("")

    modo = opcao1

    print(f"Modo : {modos[modo]}" )
    return

#Metodo que vai escolher o Local (Arquivo ou Pasta) a ser trabalhado
def escolherLocal():
    global caminho
    caminho = input(f"Escolha o arquivo ou pasta para {modos[modo]} : ")

    try:
        print(os.listdir(caminho))
        os.chdir(caminho)
        print(os.listdir)
        f = []
        for (dirpath, dirnames, filenames) in os.walk(caminho):
            print(f"dirpath : {dirpath}, dirnames : {dirnames} ; files {filenames}")
    except (FileNotFoundError):
        print("Arquivo ou Diretório não existe!")
        return escolherLocal()
    except:
        print("Deu erro parsa")
        return escolherLocal()
    


#Metodo que imprime um "titulo" no console
def titulo():
    print(" ")
    print("▄▀▄▄▄▄   ▄▀▀▄▀▀▀▄  ▄▀▀▄ ▀▀▄  ▄▀▀▄▀▀▀▄  ▄▀▀▀█▀▀▄  ▄▀▀▀▀▄  ")
    print("█ █    ▌ █   █   █ █   ▀▄ ▄▀ █   █   █ █    █  ▐ █      █ ")
    print("▐ █      ▐  █▀▀█▀  ▐     █   ▐  █▀▀▀▀  ▐   █     █      █ ")
    print("  █       ▄▀    █        █      █         █      ▀▄    ▄▀ ")
    print(" ▄▀▄▄▄▄▀ █     █       ▄▀     ▄▀        ▄▀         ▀▀▀▀   ")
    print("█     ▐  ▐     ▐       █     █         █                  ")
    print("▐                      ▐     ▐         ▐                  ")
    print(" ")
    print(" ")


if __name__ == "__main__":
    clear() # Limpa o console

    #Verifica se algum argumento foi passado na inicialização
    tipo = str(sys.argv[1]) if len(sys.argv) > 1 else ""
    escolherModo(tipo)

    #Escolher pasta ou arquivo
    escolherLocal()