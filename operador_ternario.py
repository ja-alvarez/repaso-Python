edad = 17
print('Eres mayor de edad' if edad >= 18 else 'Eres menor de edad!')

edad = 25
if('Eres mayor de edad' if edad >= 18 else 'Eres menor de edad!') == 'Eres mayor de edad':
    print(True)
else: 
    print(False)

edad = 5
print(True if edad >= 18 else False)