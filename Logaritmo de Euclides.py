def euclides(num1, num2, resultado=1):
    if num1 < num2:
        num1, num2 = num2, num1
    resto = num1 % num2
    if resto == 0:
        return (num2, resultado)
    else:
        return euclides(num2, resto, resultado+1)

num1 = 120
num2 = 156
comunDivisor, residuos = euclides(num1, num2)
print("El comun divisor de {} y {} es {}".format(num1, num2, comunDivisor))
print("Se ha encontrado  {}  residuos".format( residuos))