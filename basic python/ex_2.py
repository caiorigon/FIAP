# Exemplo de condicional
idade = 20
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# Exemplo de loop for
for i in range(5):
    print(i)

# Exemplo de loop while
variavel = "0"
while variavel != 5:
    try:
        variavel = int(input("Digite 5 para sair: "))
    except ValueError as e:
        variavel = 0

print("Operação finalizada.")
