import metodos
#TODO - Organizar e Limpar o código
#     - Comentar

metodos.getPath()
path = metodos.local

# Se o path for um arquivo, ja seguimos na logica da crypt/decrypt
if metodos.isFile(path):  # é um arquivo ?
    if metodos.isFileCreep(path):  # já esta cryptografado ?
        print("Arquivo ja esta cryptografado, insira a senha para Descreeptografar")
        fernetObj = metodos.criarFernet()
        metodos.decreep(path, fernetObj)
    else:  # Não está cryptografado
        print("Arquivo não Creeptografado, insira a senha para Creeptografar!")
        fernetObj = metodos.criarFernet()
        metodos.creep(path, fernetObj)
else:
    print("Path é um diretorio")
    # primeiro tenho que listar todos os arquivos que estão dentro de todas as pastas
    arquivos, arqCreep = metodos.lerDiretorio(path)
    # ic(arquivos)
    # ic(arqCreep)

    if arquivos == arqCreep:
        verifica = input("Todos os arquivos estão Creeptografados, deseja Descreeptografar (s/n) : ")
        if verifica in ('s','S'):
            fernetObj = metodos.criarFernet()
            for file in arqCreep:
                if metodos.isFile(file):
                    metodos.decreep(file, fernetObj)
    else:
        if len(arqCreep) > 0:
            print("-- AVISO --")
            print("Já existe um(ou mais) arquivo(s) Creeptografado dentro desta pasta (e subpastas)")
            print("Portanto se você usar uma senha diferente agora, você VAI ter problemas no futuro")
            print("Esses arquivos são:")
            for file in arqCreep:
                print(file)
            print(" ")
            print("Você tem 2 opções : ")
            print("(1) Descreeptografar os arquivos e depois Creeptografar todos.")
            print("(2) Creeptografar os outros arquivos que não estão Creeptografados (!!!)")

            verifica = input("Escolha sua opção (1/2) : ")

            if verifica == "1":
                fernetObj = metodos.criarFernet()
                for file in arqCreep:
                    metodos.decreep(file, fernetObj)

                print("Os arquivos Creeptografados, foram Descreeptografados")
                verifica = input("Deseja Creeptografar tudo ? ")
                if verifica in ('s','S'):
                    for file in arquivos:
                        if metodos.isFile(file):
                            metodos.creep(file, fernetObj)

            elif verifica == "2":
                print("Ok, vamos creeptografar")
                fernetObj = metodos.criarFernet()
                for file in arquivos:
                    if metodos.isFile(file):
                        metodos.creep(file, fernetObj)

            else:
                print("??? você não escolheu uma opçõ válida. Tchau")
                quit()

        else:
            print("-- AVISO -- ")
            print(f"Existem {len(arquivos)} arquivos dentro desta pasta e subpastas..")
            verifica = input("Você tem certeza que deseja Creeptografar todos?? s/n : ")
            if verifica in ('s','S'):
                print("Ok, vamos Creeptografa-los")
                fernetObj = metodos.criarFernet()
                for file in arquivos:
                    if metodos.isFile(file):
                        metodos.creep(file, fernetObj)
