#

class PotenciaIndice:
    def __init__(self,numero,potencia):
        self.numero = numero
        self.potencia = potencia
    def Potencia(self):
        listaNumeros = [int(i) for i in str(self.numero)]
        contador = 0
        for i in range(len(listaNumeros)):
            contador = contador + pow(listaNumeros[i],self.potencia)
        return(contador)

class SumaCuadrados(PotenciaIndice):
    def __init__(self):
       PotenciaIndice.__init__(self,589,2)

class SumaCubos(PotenciaIndice):
    def __init__(self):
        PotenciaIndice.__init__(self,589,3)

#Creacion de objetos
Cuadrado = SumaCuadrados()
Cubo = SumaCubos()
#Llamada de metodos
resultado = Cuadrado.Potencia() + Cubo.Potencia()
print(resultado)


