from itertools import product, permutations

# Datos iniciales
tropas = {
    "Infantería": {"fuerza": 1, "costo": 1},
    "Caballería": {"fuerza": 3, "costo": 3},
    "Artillería": {"fuerza": 5, "costo": 5},
}
territorios = [
    {"nombre": "Territorio 1", "defensa": 10, "tipo": "plano"},
    {"nombre": "Territorio 2", "defensa": 15, "tipo": "montañoso"},
    {"nombre": "Territorio 3", "defensa": 12, "tipo": "plano"},
]
puntos_totales = 20

# Generar combinaciones válidas de tropas
def generar_combinaciones(tropas, puntos_totales):
    combinaciones_validas = []
    for inf in range(1, puntos_totales + 1):
        for cab in range(1, (puntos_totales // tropas["Caballería"]["costo"]) + 1):
            for art in range(1, (puntos_totales // tropas["Artillería"]["costo"]) + 1):
                costo_total = (inf * tropas["Infantería"]["costo"] +
                               cab * tropas["Caballería"]["costo"] +
                               art * tropas["Artillería"]["costo"])
                if costo_total <= puntos_totales:
                    combinaciones_validas.append({"Infantería": inf, "Caballería": cab, "Artillería": art})
    return combinaciones_validas

# Generar permutaciones del orden de ataque
def generar_permutaciones(territorios):
    return list(permutations(territorios))

# Evaluar combinaciones de tropas contra territorios
def evaluar_combinaciones(combinaciones, ordenes, tropas):
    resultados = []
    for combinacion in combinaciones:
        fuerza_total = (combinacion["Infantería"] * tropas["Infantería"]["fuerza"] +
                        combinacion["Caballería"] * tropas["Caballería"]["fuerza"] +
                        combinacion["Artillería"] * tropas["Artillería"]["fuerza"])
        for orden in ordenes:
            defensa_acumulada = 0
            territorios_conquistados = []
            for territorio in orden:
                defensa_acumulada += territorio["defensa"]
                if fuerza_total >= defensa_acumulada:
                    territorios_conquistados.append(territorio["nombre"])
                else:
                    break  # Detener si no podemos conquistar más territorios
            resultados.append({
                "tropas": combinacion,
                "orden": [t["nombre"] for t in orden],
                "fuerza_total": fuerza_total,
                "territorios_conquistados": territorios_conquistados,
                "defensa_acumulada": defensa_acumulada,
            })
    return resultados

# Bonus: Restringir a atacar primero territorios más débiles
def ordenar_territorios_por_defensa(territorios):
    return sorted(territorios, key=lambda t: t["defensa"])

# Bonus: Estrategias según tipo de terreno
def ajustar_tropas_por_terreno(territorios, combinacion):
    estrategia = []
    for territorio in territorios:
        if territorio["tipo"] == "plano":
            estrategia.append({"territorio": territorio["nombre"], "recomendación": "Más caballería"})
        elif territorio["tipo"] == "montañoso":
            estrategia.append({"territorio": territorio["nombre"], "recomendación": "Más artillería"})
    return estrategia

# Bonus: Optimizar recursos
def seleccionar_mejor_resultado(resultados):
    if not resultados:
        return None
    return max(resultados, key=lambda r: len(r["territorios_conquistados"]))

# Main
if __name__ == "__main__":
    # Generar combinaciones y permutaciones
    combinaciones = generar_combinaciones(tropas, puntos_totales)
    ordenes_ataque = generar_permutaciones(territorios)

    # Evaluar combinaciones
    resultados = evaluar_combinaciones(combinaciones, ordenes_ataque, tropas)

    # Ordenar territorios por defensa para priorizar los más débiles
    territorios_ordenados = ordenar_territorios_por_defensa(territorios)

    # Mostrar estrategias según tipo de terreno
    estrategias = ajustar_tropas_por_terreno(territorios, combinaciones)

    # Seleccionar el mejor resultado
    mejor_resultado = seleccionar_mejor_resultado(resultados)

    # Imprimir resultados
    print("Combinaciones de tropas válidas:")
    for c in combinaciones:
        print(c)
    print("\nÓrdenes de ataque posibles:")
    for orden in ordenes_ataque:
        print([t["nombre"] for t in orden])
    print("\nResultados de las evaluaciones:")
    for resultado in resultados:
        print(f"Tropas: {resultado['tropas']}, Orden: {resultado['orden']}, "
              f"Fuerza Total: {resultado['fuerza_total']}, Territorios Conquistados: {resultado['territorios_conquistados']}")
    print("\nEstrategias por tipo de terreno:")
    for estrategia in estrategias:
        print(f"Territorio: {estrategia['territorio']}, Recomendación: {estrategia['recomendación']}")
    print("\nMejor resultado:")
    if mejor_resultado:
        print(f"Tropas: {mejor_resultado['tropas']}, Orden: {mejor_resultado['orden']}, "
              f"Fuerza Total: {mejor_resultado['fuerza_total']}, Territorios Conquistados: {mejor_resultado['territorios_conquistados']}")
    else:
        print("No se encontró una combinación óptima.")




























