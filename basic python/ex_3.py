# Error handling

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(e)

# typeError
try:
    result = "10" + 5
except TypeError as e:
    print("Erro de tipo:", e)

try:
    int("abc")
except ValueError as e:
    print("Erro de valor:", e)

try:
    print(variavel_inexistente)
except NameError as e:
    print("Erro de nome:", e)

try:
    my_list = [1, 2, 3]
    print(my_list[4])
except IndexError as e:
    print("Erro de índice:", e)

try:
    my_dict = {"key": "value"}
    print(my_dict["invalid_key"])
except KeyError as e:
    print("Erro de chave:", e)

try:
    with open("arquivo_inexistente.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print("Erro de arquivo não encontrado:", e)

try:
    import modulo_inexistente
except ImportError as e:
    print("Erro de importação:", e)


class Exemplo:
    def __init__(self):
        self.atributo = "valor"


try:
    obj = Exemplo()
    print(obj.atributo_inexistente)
except AttributeError as e:
    print("Erro de atributo:", e)
