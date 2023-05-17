import pandas as pd
import itertools

def generar_tabla_verdad(variables):
    combinaciones = list(itertools.product([True, False], repeat=len(variables)))
    df = pd.DataFrame(combinaciones, columns=variables)
    return df

def evaluar_expresion(expresion, valores):
    for var, val in valores.items():
        expresion = expresion.replace(var, str(val))

    resultado = eval(expresion)
    return resultado

def mostrar_tabla_operacion_logica(operacion):
    expresion = operacion.replace("<->", "==").replace("->", ">=").replace("^", "and").replace("v", "or").replace("¬", "not")
    tabla = generar_tabla_verdad(['A', 'B'])
    valores = {'A': tabla['A'], 'B': tabla['B']}
    resultado = [evaluar_expresion(expresion, {'A': a, 'B': b}) for a, b in zip(valores['A'], valores['B'])]
    tabla['Resultado'] = resultado
    tabla.rename(columns={'Resultado': operacion}, inplace=True)
    print(f"\nTabla de la operación lógica {operacion}:")
    print(tabla)

mostrar_tabla_operacion_logica('A ^ B')
mostrar_tabla_operacion_logica('A v B')
mostrar_tabla_operacion_logica('¬ A')
mostrar_tabla_operacion_logica('A <-> B')
mostrar_tabla_operacion_logica('A -> B')

num_variables = int(input("Ingrese el número de variables: "))
variables = []
for i in range(num_variables):
    nombre = input(f"Ingrese el nombre de la variable {i+1}: ")
    variables.append(nombre)

tabla_verdad = generar_tabla_verdad(variables)
print("\nTabla de verdad:")
print(tabla_verdad)

expresion = input("Ingrese la expresión lógica: ")
expresion = expresion.replace("<->", "==").replace("->", ">=").replace("^", "&").replace("v", "|").replace("¬", "~")

columnas = list(tabla_verdad.columns)
if len(variables) > len(columnas):
    raise ValueError("El número de variables ingresado es mayor que la cantidad de columnas de la tabla de verdad.")

filas_tabla_completa = []
for index, row in tabla_verdad.iterrows():
    valores = row.to_dict()
    partes_expresion = []
    for var in variables:
        parte = f"{var} = {valores[var]}"
        partes_expresion.append(valores[var])

    resultado = evaluar_expresion(expresion, valores)
    partes_expresion.append(resultado)
    filas_tabla_completa.append(partes_expresion)

tabla_completa = pd.DataFrame(filas_tabla_completa, columns=columnas + [expresion])

print("\nTabla de verdad completa:")
print(tabla_completa)
