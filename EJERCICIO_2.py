reglas = [
    {
        'id': 1, # Regla 1
        'condiciones': {'tiene_plumas': True, 'vuela': True},
        'conclusion': 'Es un Ave'
    },
    {
        'id': 2, # Regla 2
        'condiciones': {'tiene_pelaje': True, 'ladra': True},
        'conclusion': 'Es un Perro'
    },
    {
        'id': 3, # Regla 3
        'condiciones': {'vive_en_agua': True, 'tiene_escamas': True},
        'conclusion': 'Es un Pez'
    }
]

hechos = {
    'tiene_plumas': True,   # Hecho 1
    'vuela': True,          # Hecho 2
    'tiene_pelaje': False,  # Hecho 3
    'ladra': False,         # Hecho 4
    'vive_en_agua': False,  # Hecho 5
    'tiene_escamas': False  # Hecho 6
}

#INTERFAZ DE USUARIO
print("\n Diagnóstico")

#MOTOR DE INFERENCIA
for regla in reglas:
    se_cumple = True
    for clave, valor_necesario in regla['condiciones'].items():
        if hechos.get(clave) != valor_necesario:
            se_cumple = False
            break
            
    if se_cumple:
        #MÓDULO DE EXPLICACIÓN
        print(f"Regla {regla['id']} activada -> {regla['conclusion']}")