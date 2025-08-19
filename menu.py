import calculadora

opcao = input("Selecione uma opção:\n1-Somar\n2-Subtrair\n3-Multiplicar\n4-Dividir\n0-Sair")

if opcao == "1":
     a = int(input("Informe o primeiro número: "))
     b = int(input("Informe o segundo número: "))

     soma = calculadora.somar(a, b)
     print(f"{a} + {b} = {soma}")