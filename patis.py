import os
import sys
from os.path import join, getsize 
from math import log2

_suffixes = ['bytes', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']

def file_size(size):
    # Determine binary order in steps of size 10
    # (coerce to int, // still returns a float)
    order = int(log2(size) / 10) if size else 0

    # Format file size
    # (.4g results in rounded numbers for exact matches
    # and maximum 3 decimals, and should never resort
    # to exponent values)
    return '{:.4g} {}'.format(size / (1 << (order * 10)), _suffixes[order])

caminho = "/home/lao/secure"
tamanho = 0
diretorios = 0
arquivos = 0

if os.path.isfile(caminho):
    print("é arquivo")
else:
    print("é diretorio")

    for (dirpath, dirnames, filenames) in os.walk(caminho):
        for file in filenames:
            arquivos+=1
            tam = getsize(join(dirpath, file))
            local = join(dirpath, file)
            tamanho += tam
            print(f"Arquivo : {local} ", end=" ")
            print(" "*(66-len(local)), end=" ")
            print(f"; Tamanho: {file_size(tam)}")
        # print(f"dirpath : {dirpath}, dirnames : {dirnames} ; files {filenames}")

    print("  - - -   ")
    print(f"Tamanho Total : {file_size(tamanho)} ")
    print(f"Qtde de arquivos : {arquivos}")
    
    
    print("  - - -   ")
    for item in os.walk(caminho):
        print(item)

print("  - - -   ")


# for root, dirs, files in os.walk('/home/lao/secure'):
#     print(root, "consumes ") 
#     print(sum(getsize(join(root, name)) for name in files), end=" ") 
#     print("bytes in", len(files), "non-directory files") 
#     if 'CVS' in dirs:
#         dirs.remove('CVS') # don't visit CVS directories