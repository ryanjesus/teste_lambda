preco = 5


# função normal
def calcular_imposto(preco):
    return preco * 0.3


print(calcular_imposto(preco))

# mesma função com lambda
calcular_imposto2 = lambda x: x * 0.3
print(calcular_imposto2(preco))

### Tá, mas qual a diferença?
# Quando você aplica essa função dentro de outros métodos do Python. Aí sim existe vantagem.

# Ex: temos agora uma lista de preços.

precos = [100, 500, 10, 25]

impostos = list(map(lambda x: x*0.3, precos))
print(impostos)

# link tutorial lambda
#http://www.dsc.ufcg.edu.br/~pet/jornal/maio2013/materias/tutoriais.html#:~:text=Em%20Python%2C%20existe%20um%20conceito,se%20comportar%C3%A1%20como%20uma%20fun%C3%A7%C3%A3o.
#https://www.youtube.com/watch?v=xmMXULd0dxc