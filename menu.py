import calculadora

def menu():

     opcao = input("1-Somar\n2-Subtrair\n3-Multiplicar\n4-Dividir\n0-Sair\n\nSelecione uma opção: ")

     if opcao == "1":
          a = int(input("Informe o primeiro número: "))
          b = int(input("Informe o segundo número: "))

          soma = calculadora.somar(a, b)
          print(f"{a} + {b} = {soma}")
     elif opcao == "2":
          a = int(input("Informe o primeiro número: "))
          b = int(input("Informe o segundo número: "))

          subtracao = calculadora.subtrair(a, b)
          print(f"{a} - {b} = {subtracao}")