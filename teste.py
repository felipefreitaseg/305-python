# class Pessoa:
#     def __init__(self, nome):
#         self.nome = nome

#     def __str__(self):
#         return self.nome

# ninja = Pessoa('Raianey')
# print(ninja)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# class animalEstimacao():
#     def __init__(self, nome, especie, dono):
#         self.nome = nome
#         self.especie = especie
#         self.dono = dono

#     def __str__(self):
#         return self.nome

# import animal_estimacao as animal

# Zabelita = animal.animalEstimacao('Zabelita','Capivara','Taina')
# Bob = animal.animalEstimacao('Bob','quati','Taina')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# dono = animalEstimacao('Taina')
# especie = animalEstimacao('Capivara')
# nome = animalEstimacao('Zebelita')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def soma(self):
        return self.a + self.b

    def subtrai(self):
        return self.a - self.b

    def multiplica(self):
        return self.a * self.b
    
    def dividi(self):
        return self.a / self.b

teste = Calculadora(128,2)
print("Soma: ", teste.soma())
print("Subtracao: ", teste.subtrai())
    
