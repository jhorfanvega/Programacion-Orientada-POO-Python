class Calculadora:
    def __init__(self,n1,n2):
        self.suma = n1 + n2
operacion =  Calculadora(100,4444)
print(f'el resultado es: {operacion.suma}')