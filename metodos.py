import getpass
import os
from math import log2
from os.path import getsize, join

from cryptography.fernet import Fernet
from icecream import ic

_suffixes = ['bytes', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']
local = ""
modo = ""
CHAVE = "NC90NHjuPsg3u9ZdN9ObD95Rf4Yazxg1EqCI_52c-BE="
chaveFinal = ""


def criarFernet():
    """Função que pega a senha e cria o objeto Fernet que vai cryptografar e descryptografar"""
    global CHAVE, chaveFinal
    senha1 = getpass.getpass("Digite a senha : ")
    senha2 = getpass.getpass("Digite a senha novamente : ")
    if senha1 == senha2:
        chaveFinal = CHAVE + senha1
        fern = Fernet(chaveFinal)
        return fern


def getPath():
    """Função que pede o PATH do arquivo ou diretorio"""
    global local
    local = input("PATH -> ")


def isFile(path):
    """Função que verifica se o path é um arquivo ou diretorio"""
    return os.path.isfile(path)


def isFileCreep(path):
    """Função que verifica se o arquivo já está Creeptografado"""
    path = path +"\n"
    with open(".imacreep", "r") as imacreep:
        linhas = imacreep.readlines()
        if path in linhas:
            return True

    return False


def creep(arquivo, fernetObjeto):
    """Funçao que Creeptografa o arquivo"""
    # Creeptografia
    with open(arquivo, "r") as arqMestre:
        content = (arqMestre.read()).encode("utf-8")
        crypt = fernetObjeto.encrypt(bytes(content))  # .encode('utf-8')))
        # ic(crypt)

    # Escreve o arquivo Creeptografado
    with open(arquivo, "wb") as arquivoCreep:
        arquivoCreep.write(crypt)

    # Adiciona o arquivo Creeptografado ao log .imacreep
    with open(".imacreep", "a") as imacreep:
        imacreep.write(arquivo+"\n")


def decreep(arquivo, fernetObjeto):
    """Função que descriptografa o arquivo"""
    with open(arquivo, "rb") as arq:
        resultado = arq.read()
        resB = resultado.decode("utf-8")
        content = (fernetObjeto.decrypt(resB).decode("utf-8"))

    with open(arquivo, "w") as arqFinal:
        arqFinal.write(content)

    retiraArquivoImacreep(arquivo)


def retiraArquivoImacreep(arquivo):
    """Função que retira o arquivo que foi descriptografado da lista de log (.imacreep)"""
    arquivoBarraN = arquivo+"\n"
    with open(".imacreep", "r") as imacreep:
        files = imacreep.readlines()
        result = ""
        for f in files:
            if arquivoBarraN not in f:
                result = f"{result}{f}"

    with open(".imacreep", "w") as imacreep:
        imacreep.write(result)


def file_size(size):
    ''' Função para converter os bytes para leitura humana '''
    order = int(log2(size) / 10) if size else 0
    return '{:.4g} {}'.format(size / (1 << (order * 10)), _suffixes[order])


def lerDiretorio(caminho):
    arquivos = []
    arqCreep = []
    tamanhoTotal = 0
    # Iterar a pasta e buscar os arquivos do diretorio
    for dirpath, dirnames, filenames in os.walk(caminho):
        for file in filenames:
            tam = os.path.getsize(join(dirpath, file))
            local = os.path.join(dirpath, file)
            arquivos.append(local)
            # ic(local)
            tamanhoTotal += tam
            if isFileCreep(local):
                arqCreep.append(local)

            # print(f"{local} ", end=" ")
            # print(" " * (66 - len(local)), end=" ")
            # print(f"; Tamanho: {file_size(tam)}")
    print("  - - -   ")
    print(f"Qtde de arquivos : {len(arquivos)}")
    print(f"Tamanho Total : {file_size(tamanhoTotal)} ")
    return [arquivos, arqCreep]
