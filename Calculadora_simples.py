# funções
def adicao(a, b):
  return a + b
def subtracao(a, b):
  return a - b
def multiplicacao(a, b):
  return a * b
def divisao(a, b):
  if b != 0:
    return a / b
  else:
    return "Não é possivel dividir por zero"

print("Selecione a operação: ")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

escolha = input("Digite a opção: ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if ecolha == '1':
  print("Resultado:", adicao(num1, num2))
elif escolha == '2':
  print("Resultado:", subtracao(num1, num2))
elif escolha == '3':
  print("Resultado:", multiplicacao(num1, num2))
elif escolha == '4':
  print("Resultado:", divisao(num1, num2))
else:
  print("Escolha inválida")
