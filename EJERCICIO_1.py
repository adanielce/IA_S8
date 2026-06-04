
esta_lloviendo = True  # Hecho 1
hace_frio = False      # Hecho 2
es_de_noche = True     # Hecho 3

# INTERFAZ DE USUARIO
print("Recomendaciones")

# BASE DE CONOCIMIENTOS y MOTOR DE INFERENCIA
# Regla 1: Si llueve -> paraguas
if esta_lloviendo:
    print("Conclusión 1: Lleva paraguas.")

# Regla 2: Si hace frío -> abrigo, si no -> sin abrigo
if hace_frio:
    print("Conclusión 2: Lleva abrigo.")
else:
    print("Conclusión 2: No necesitas abrigo.")

# Regla 3: Si es de noche Y llueve -> cuidado al conducir
if es_de_noche and esta_lloviendo:
    print("Conclusión 3: Ten cuidado al conducir, hay poca visibilidad.")

