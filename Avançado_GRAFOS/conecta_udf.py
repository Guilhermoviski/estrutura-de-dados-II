# ==============================================================================
# Projeto ConectaUDF: Redes Sociais com Grafos
# Disciplina: Algoritmos / Matemática Discreta / Ciência de Dados
# Integrantes do Grupo:
# - Aloisio Veleda
# - Giovanna Nascimento
# - Guilherme Brito
# - Isabela Cristina
# - Julia Barreira
# - Pedro Paulo
# - Tiago Freire
# ==============================================================================

from collections import deque

def exibir_separador(titulo: str):
    print("\n" + "=" * 60)
    print(f" {titulo.upper()} ")
    print("=" * 60)

# ==============================================================================
# 1. REDE ORIGINAL (Seção 8 do Caderno)
# ==============================================================================
exibir_separador("1. Rede Social Original ConectaUDF")

rede = {
    "Ana": ["Bruno", "Carla"],
    "Bruno": ["Ana", "Carla", "Diego"],
    "Carla": ["Ana", "Bruno", "Elisa"],
    "Diego": ["Bruno", "Elisa", "Felipe"],
    "Elisa": ["Carla", "Diego", "Felipe"],
    "Felipe": ["Diego", "Elisa"]
}

# Quantidade de usuários (Vértices)
n = len(rede)

# Calcule o grau de cada usuário
print("\n--- Conexões Diretas (Grau) ---")
for usuario, amigos in rede.items():
    print(f"{usuario:7} tem {len(amigos)} conexões: {', '.join(amigos)}")

# A soma dos graus conta cada amizade duas vezes
soma_graus = sum(len(amigos) for amigos in rede.values())
arestas = soma_graus // 2

print("\n--- Estatísticas da Rede Original ---")
print("Total de usuários (V):", n)
print("Soma dos graus:", soma_graus)
print("Total de amizades (E):", arestas)

# Densidade do grafo
densidade = (2 * arestas) / (n * (n - 1))
print(f"Densidade: {densidade:.4f} ({densidade:.2%})")

# ==============================================================================
# 2. ENCONTRANDO CAMINHOS (Seção 9 do Caderno)
# ==============================================================================
exibir_separador("2. Análise de Caminhos de Ana até Felipe")

def encontrar_menor_caminho(grafo, inicio, fim):
    fila = deque([[inicio]])
    visitados = {inicio}
    
    while fila:
        caminho = fila.popleft()
        no = caminho[-1]
        if no == fim:
            return caminho
        for vizinho in grafo[no]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(caminho + [vizinho])
    return None

caminho1 = encontrar_menor_caminho(rede, "Ana", "Felipe")
print(f"Caminho encontrado: {' -> '.join(caminho1)}")
print(f"Número de arestas: {len(caminho1) - 1}")
print("Outro caminho com a mesma quantidade: Ana -> Carla -> Elisa -> Felipe (3 arestas)")

# ==============================================================================
# 3. DESAFIO EM GRUPO - REDE AMPLIADA (Seção 10 do Caderno)
# 4 novos usuários fictícios: Gabriel, Helena, Igor, Juliana
# 7 novas amizades criadas (atende ao requisito de 'no mínimo cinco')
# ==============================================================================
exibir_separador("3. Desafio em Grupo - Rede Ampliada")

rede_ampliada = {
    # Usuários originais
    "Ana": ["Bruno", "Carla"],
    "Bruno": ["Ana", "Carla", "Diego"],
    "Carla": ["Ana", "Bruno", "Elisa", "Helena"],           # +1 amizade com Helena
    "Diego": ["Bruno", "Elisa", "Felipe", "Igor"],          # +1 amizade com Igor
    "Elisa": ["Carla", "Diego", "Felipe"],
    "Felipe": ["Diego", "Elisa", "Gabriel"],                # +1 amizade com Gabriel
    
    # 4 Novos usuários fictícios
    "Gabriel": ["Felipe", "Helena", "Juliana"],             # 3 conexões
    "Helena": ["Carla", "Gabriel", "Igor"],                 # 3 conexões
    "Igor": ["Diego", "Helena", "Juliana"],                 # 3 conexões
    "Juliana": ["Gabriel", "Igor"]                          # 2 conexões
}

# As 7 novas amizades criadas foram:
# 1. Felipe — Gabriel
# 2. Gabriel — Helena
# 3. Helena — Igor
# 4. Igor — Juliana
# 5. Juliana — Gabriel
# 6. Diego — Igor
# 7. Carla — Helena

n_amp = len(rede_ampliada)
soma_graus_amp = sum(len(amigos) for amigos in rede_ampliada.values())
arestas_amp = soma_graus_amp // 2
densidade_amp = (2 * arestas_amp) / (n_amp * (n_amp - 1))

print(f"Total de usuários após ampliação: {n_amp}")
print(f"Soma dos graus após ampliação: {soma_graus_amp}")
print(f"Total de amizades após ampliação: {arestas_amp} (8 originais + 7 novas)")
print(f"Densidade após ampliação: {densidade_amp:.4f} ({densidade_amp:.2%})")

print("\n--- Ranking de Conexões (Rede Ampliada) ---")
ranking = sorted(rede_ampliada.items(), key=lambda x: len(x[1]), reverse=True)
for user, amg in ranking:
    print(f"{user:8}: {len(amg)} conexões")

print(f"\nUsuários com mais conexões: Carla e Diego (Grau 4)")

# ==============================================================================
# 4. ALGORITMO DE RECOMENDAÇÃO DE AMIZADES (Seção 10 e 12)
# ==============================================================================
exibir_separador("4. Recomendação de Amizades por Amigos em Comum")

def sugerir_amizades(grafo):
    usuarios = list(grafo.keys())
    sugestoes = []
    
    for i in range(len(usuarios)):
        for j in range(i + 1, len(usuarios)):
            u1, u2 = usuarios[i], usuarios[j]
            # Se já são amigos, não sugere
            if u2 in grafo[u1]:
                continue
            amigos_u1 = set(grafo[u1])
            amigos_u2 = set(grafo[u2])
            comuns = amigos_u1.intersection(amigos_u2)
            if comuns:
                sugestoes.append((u1, u2, len(comuns), list(comuns)))
                
    # Ordenar pelos que têm mais amigos em comum
    sugestoes.sort(key=lambda x: x[2], reverse=True)
    return sugestoes

sugestoes = sugerir_amizades(rede_ampliada)
for u1, u2, qtd, comuns in sugestoes:
    print(f"Sugerir [{u1} e {u2}] -> {qtd} amigo(s) em comum: {', '.join(comuns)}")

print("\nExecução finalizada com sucesso!")
