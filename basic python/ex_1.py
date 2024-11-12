# hello world!
print("hello world!")

# Declarando variáveis
numero = 42
nome = "João"
salario = 2500.50

# Imprimindo as variáveis
print(numero)
print(nome)
print(salario)

a = 10
b = 20
soma = a + b
concatenacao = "olá" + " " + "Você."
print(soma)
print(concatenacao)

# Tamanho da string
frase = "Uma Frase Qualquer"
tamanho = len(frase)

print("tamanho da string:", tamanho)

# Transformando em maiúsculas
maiusculas = frase.upper()
minuscula = frase.lower()

print("Maiúsculas:", maiusculas, minuscula)

# Substituindo palavras na string
nova_frase = frase.replace("Frase", "mensagem")
print("Nova frase:", nova_frase)

# lista
frutas = ["maçã", "banana", "cereja"]
frutas.append("laranja")
print(frutas)

# ferramentes de criacao de lista e for
quadrados = [x**2 for x in range(10)]
print(quadrados)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# conjunto, remove entradas repetidas
conjunto = {1, 2, 3, 4, 4}
print(conjunto)  # {1, 2, 3, 4}

# dicionarios, chave: valor
aluno = [
    {"nome": "João", "idade": 20, "curso": "Engenharia"},
    {"qq": "coisa", "foo": "bar", 1: 2},
]
print(aluno[0]["nome"])  # João
print(aluno[1]["foo"])  # João
