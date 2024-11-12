# manipulação de arquivos
# escrever
with open("basic python\\arquivo.txt", "w") as file:
    file.write("Olá, mundo!")

# ler
with open("basic python\\arquivo.txt", "r") as file:
    conteudo = file.read()
    print(conteudo)  # Olá, mundo!


import math

print(math.sqrt(16))  # 4.0
