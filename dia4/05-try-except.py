# Manejo de excepciones
# division = 10 / 0

# Bloque try: Sirve para ejecutar el codigo
try:
    division = 10 / 5
    print(division)
    
# Bloque except: Sirve para capturar las excepciones
except ZeroDivisionError as error:
    print(error)
except Exception as error:
    print(error)

# Bloque finally: Se ejecutará siempre al final
finally:
    print('Finalizado')