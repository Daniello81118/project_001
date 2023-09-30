import math

def operacoes_trigonometricas():
    print("Operações Trigonométricas:")
    print("1. Seno")
    print("2. Cosseno")
    print("3. Tangente")
    
    escolha = input("Digite 1/2/3: ")
    angulo = float(input("Digite o ângulo em graus: "))

    if escolha == '1':
        resultado = math.sin(math.radians(angulo))
        print(f"Seno({angulo}°) = {resultado}")
    elif escolha == '2':
        resultado = math.cos(math.radians(angulo))
        print(f"Cosseno({angulo}°) = {resultado}")
    elif escolha == '3':
        resultado = math.tan(math.radians(angulo))
        print(f"Tangente({angulo}°) = {resultado}")
    else:
        print("Escolha inválida")

def operacoes_raiz_e_potencia():
    print("Operações de Raiz Quadrada e Potência:")
    print("1. Raiz Quadrada")
    print("2. Potência")
    
    escolha = input("Digite 1/2: ")

    if escolha == '1':
        numero = float(input("Digite um número: "))
        resultado = math.sqrt(numero)
        print(f"Raiz Quadrada de {numero} = {resultado}")
    elif escolha == '2':
        base = float(input("Digite a base: "))
        expoente = float(input("Digite o expoente: "))
        resultado = math.pow(base, expoente)
        print(f"{base}^{expoente} = {resultado}")
    else:
        print("Escolha inválida")

while True:
    print("\nSelecione a operação:")
    print("1. Operações Trigonométricas")
    print("2. Operações de Raiz Quadrada e Potência")
    print("3. Sair")

    escolha = input("Digite 1/2/3: ")

    if escolha == '1':
        operacoes_trigonometricas()
    elif escolha == '2':
        operacoes_raiz_e_potencia()
    elif escolha == '3':
        print("Encerrando a calculadora.")
        break
    else:
        print("Escolha inválida")
      
