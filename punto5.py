temperatura_enF = int(input("Por favor ingresar la temperatura actual en Farenheit "))

def conversion_temperatura (temperatura_enF):
    return (temperatura_enF - 32) / 1.8

temperatura_enC = conversion_temperatura (temperatura_enF)
print(f'La temperatura en ºC es: {temperatura_enC}')