def calcular_dobro(numero):
  """Recebe um número e retorna o dobro dele."""
  return numero * 2


def calcular_triplo(numero):
  """Recebe um número e retorna o triplo dele."""
  return numero * 3


def calcular_quadrado(numero):
  """Recebe um número e retorna o quadrado dele."""
  return numero**2


# Programa principal
valor = float(input("Digite um número: "))

dobro = calcular_dobro(valor)
triplo = calcular_triplo(valor)
quadrado = calcular_quadrado(valor)

print(f"O dobro de {valor} é {dobro}")
print(f"O triplo de {valor} é {triplo}")
print(f"O quadrado de {valor} é {quadrado}")