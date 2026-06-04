#NTERFAZ DE USUARIO (Entrada de datos)
def solicitar_datos():
    print("\n Evaluar solicitudes de Préstamos")
    ingreso = float(input("Cuál es su ingreso mensual? ")) # Hecho 1 
    deuda = float(input("Cuál es su deuda actual? "))      # Hecho 2 
    
    return {'ingreso': ingreso, 'deuda': deuda}

#MOTOR DE INFERENCIA 
def evaluar_credito(hechos):
    conclusiones = []
    explicaciones = [] #MÓDULO DE EXPLICACIÓN
    
    # Regla 1: Si ingreso > 1000 -> Pre-aprobado
    if hechos['ingreso'] > 1000:
        conclusiones.append("Pre-aprobado")
        explicaciones.append(f"Porque su ingreso ({hechos['ingreso']}) es mayor a 1000.")
        
    # Regla 2: Si deuda < 500 -> Bajo riesgo
    if hechos['deuda'] < 500:
        conclusiones.append("Bajo riesgo")
        explicaciones.append(f"Porque su deuda ({hechos['deuda']}) es menor a 500.")
        
    return conclusiones, explicaciones

datos_usuario = solicitar_datos()
resultados, razones = evaluar_credito(datos_usuario)

#INTERFAZ DE USUARIO (Salida de datos)
print("\n--- RESULTADO -")
print(f"Hechos ingresados: {datos_usuario}")

if resultados:
    print(f"Conclusiones: {', '.join(resultados)}")
    
    #MÓDULO DE EXPLICACIÓN (Trazabilidad)
    print("\n--- DEMOSTRACIÓN  ")
    for razon in razones:
        print(f"- {razon}")
else:
    print("Crédito rechazado.")