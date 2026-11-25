def calcular_dobro(numero):
  """Recebe um número e retorna o dobro dele."""
  return numero * 2


# Programa principal
valor = float(input("Digite um número: "))
resultado = calcular_dobro(valor)

print(f"O dobro de {valor} é {resultado}")