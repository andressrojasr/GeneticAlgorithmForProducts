import random
import controller.products as p


def extract_column(rows, index, default=0):
    return [row[index] if row[index] is not None else default for row in rows]

# Datos de ejemplo (volúmenes en unidades cúbicas)
# volumes = [0.5, 1.2, 0.8, 2.0, 0.3, 0.6]
# frec =     [100, 200, 100, 200,  10,  10]
# marg =     [ 30,  10,  15,  20,  15,   6]
# V_max = 5.0    # Capacidad máxima de volumen
# alpha = 10.0   # Penalización por exceso de volumen

# Función de fitness ajustada a volumen
def fitness(chromosome, volumes, frec, marg, V_max, alpha):
    total_vol = sum(g * v for g, v in zip(chromosome, volumes))
    total_val = sum(g * f * m for g, f, m in zip(chromosome, frec, marg))
    if total_vol <= V_max:
        return total_val
    else:
        # Penaliza la solución si excede la capacidad de volumen
        return total_val - alpha * (total_vol - V_max)

# Inicialización de población
def inicializa_poblacion(P, N):
    poblacion = [[random.randint(0,1) for _ in range(N)] for _ in range(P)]
    return poblacion

# Selección por torneo
def seleccion_torneo(pop, fits, k=3):
    aspirantes = random.sample(list(zip(pop, fits)), k)
    return max(aspirantes, key=lambda x: x[1])[0]

# Cruce de un punto
def cruce(p1, p2, p_cross=0.8):
    if random.random() < p_cross:
        punto = random.randrange(1, len(p1))
        return p1[:punto] + p2[punto:], p2[:punto] + p1[punto:]
    return p1[:], p2[:]

# Mutación de bits
def mutacion(chromo, p_mut=0.02):
    return [1-g if random.random()<p_mut else g for g in chromo]

def initializeGenetic(p_cross, p_mut, P, G_max, V_max, alpha):
    productos = p.getProducts()
    volumes = extract_column(productos, 2, default=0)  # volúmenes (columna índice 4)
    print ("Volúmenes:", volumes)
    frec    = extract_column(productos, 3, default=0)  # frecuencia o precio (columna índice 2)
    print ("Frecuencias:", frec)
    marg    = extract_column(productos, 4, default=0)  # margen (columna índice 3)
    print ("Margenes:", marg)
    N = len(volumes)  # número de productos
    # Evolución de la población
    pobl = inicializa_poblacion(P, N)
    best, best_fit = None, float('-inf')

    for gen in range(G_max):
        fits = [fitness(ind, volumes, frec, marg, V_max, alpha) for ind in pobl]
        # Guardar el mejor individuo
        idx = fits.index(max(fits))
        if fits[idx] > best_fit:
            best_fit, best = fits[idx], pobl[idx]
        # Crear nueva generación
        nueva = []
        while len(nueva) < P:
            padre1 = seleccion_torneo(pobl, fits)
            padre2 = seleccion_torneo(pobl, fits)
            h1, h2 = cruce(padre1, padre2, p_cross)
            nueva += [mutacion(h1, p_mut), mutacion(h2, p_mut)]
        pobl = nueva[:P]

    return best, best_fit
        # # Resultados finales
        # print("Mejor ganancia:", best_fit)
        # print("Mejor combinación:", best)

# print(initializeGenetic(0.8, 0.02, 50, 200, 5.0, 10.0)) 
# P número de individuos, G número de generaciones
# y N número de genes (volúmenes)
# p_cross, p_mut = 0.8, 0.02
# P, G_max = 50, 200
# N = len(volumes)

