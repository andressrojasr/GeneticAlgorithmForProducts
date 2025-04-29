import random
import controller.products as p

def extract_column(rows, index, default=0):
    return [row[index] if row[index] is not None else default for row in rows]

def fitness_int(chrom, volumes, marg, V_max, alpha):
    total_vol = sum(q * v for q, v in zip(chrom, volumes))
    total_val = sum(q * m for q, m in zip(chrom, marg))
    if total_vol <= V_max:
        return total_val
    return total_val - alpha * (total_vol - V_max)

# Inicializa con enteros
def inicializa_poblacion_int(P, max_q_list):
    return [
        [random.randint(0, max_q_list[i]) for i in range(len(max_q_list))]
        for _ in range(P)
    ]

# Selección, cruce y mutación sencillos para enteros
def seleccion_torneo(pop, fits, k=3):
    aspir = random.sample(list(zip(pop, fits)), k)
    return max(aspir, key=lambda x: x[1])[0]

def cruce_int(p1, p2, p_cross=0.8):
    if random.random() < p_cross:
        punto = random.randrange(1, len(p1))
        return p1[:punto] + p2[punto:], p2[:punto] + p1[punto:]
    return p1.copy(), p2.copy()

def mutacion_int(chrom, max_q_list, p_mut=0.02):
    new = []
    for q, qmax in zip(chrom, max_q_list):
        if random.random() < p_mut:
            # cambia a un valor aleatorio dentro del rango
            new.append(random.randint(0, qmax))
        else:
            new.append(q)
    return new

def initializeGenetic_int(p_cross, p_mut, P, G_max, V_max, alpha, idCategory, productos):
    print(f"Productos encontrados: {productos}")

    ids    = extract_column(productos, 'id')
    volumes = extract_column(productos, 'volumen', default=0)
    marg    = extract_column(productos, 'ganancia', default=0)
    N = len(volumes)
    # Máximos por producto para no superar solo con uno
    max_q = [int(V_max // v) if v > 0 else 0 for v in volumes]
    pobl = inicializa_poblacion_int(P, max_q)
    best, best_fit = None, float('-inf')

    for gen in range(G_max):
        fits = [fitness_int(ind, volumes, marg, V_max, alpha) for ind in pobl]
        # guarda el mejor
        idx = max(range(len(fits)), key=lambda i: fits[i])
        if fits[idx] > best_fit:
            best_fit, best = fits[idx], pobl[idx]
        # nueva generación
        nueva = []
        while len(nueva) < P:
            p1 = seleccion_torneo(pobl, fits)
            p2 = seleccion_torneo(pobl, fits)
            h1, h2 = cruce_int(p1, p2, p_cross)
            nueva.append(mutacion_int(h1, max_q, p_mut))
            nueva.append(mutacion_int(h2, max_q, p_mut))
        pobl = nueva[:P]
    
    print("Mejor gananica:" ,best_fit)
    print("Mejor combinacion:" , best)

    return best, best_fit, ids