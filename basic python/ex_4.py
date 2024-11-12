# Definindo uma função simples
def saudacao():
    print("Olá, Mundo!")


# Chamando a função
saudacao()


# Função com parâmetros
def saudacao(nome):
    print(f"Olá, {nome}!")


saudacao("Caio")


# Função com retorno
def saudacao(nome):
    return f"Olá, {nome}!"


# Armazenando o valor retornado
mensagem = saudacao("Maria")
print(mensagem)


# Função com múltiplos parâmetros
def soma(a, b):
    return a + b


# Chamando a função com múltiplos argumentos
resultado = soma(10, 5)
print(resultado)
