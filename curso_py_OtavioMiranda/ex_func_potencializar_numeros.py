# Cire um função que Duplica, triplica e quadruplica
# o numero recebido como parâmetro.


def cria_multiplicador(multiplicador):  # utilizando Closure para criar uma função que cria uma ou mais funções para solucionar o problema em caso de N numeros
    def multiplicar(n):
        return n * multiplicador
    return multiplicar

duplicar = cria_multiplicador(2)
triplicar = cria_multiplicador(3)
quadruplicar = cria_multiplicador(4)

print(duplicar(3))
print(triplicar(3))
print(quadruplicar(3))