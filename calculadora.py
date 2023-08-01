def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero!"

print("Calculadora Simples")
print("-------------------")

while True:
    print("Selecione uma operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

    opcao = input("Digite o número da operação desejada: ")

    if opcao == "0":
        print("Encerrando a calculadora.")
        break

    if opcao not in ["1", "2", "3", "4"]:
        print("Opção inválida! Por favor, selecione uma opção válida.")
        continue

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == "1":
        resultado = soma(num1, num2)
        print("Resultado: ", resultado)
    elif opcao == "2":
        resultado = subtracao(num1, num2)
        print("Resultado: ", resultado)
    elif opcao == "3":
        resultado = multiplicacao(num1, num2)
        print("Resultado: ", resultado)
    elif opcao == "4":
        resultado = divisao(num1, num2)
        print("Resultado: ", resultado)

    print("-------------------")
