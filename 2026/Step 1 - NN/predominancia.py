import matplotlib.pyplot as plt
import numpy as np

# ==========================================================
# VOCÊ SÓ MUDA ESTES VETORES
# ==========================================================

fases = ['Fase 1', 'Fase 2', 'Fase 3', 'Fase 4']

# Para CADA ARQUITETURA, o otimizador vencedor em cada fase
FNN  = ['Adam', 'SGD', 'SGD', 'SGD']
CNN  = ['SGD', 'Adam', 'SGD', 'SGD']
RNN  = ['SGD', 'SGD', 'Adam', 'SGD']
GRU  = ['SGD', 'SGD', 'SGD', 'Adam']
LSTM = ['Adam', 'SGD', 'SGD', 'SGD']
TCN  = ['-', 'Adam', 'Adam', 'Adam']      # '-' = não testado

# Lista de todas as arquiteturas
arquiteturas = [FNN, CNN, RNN, GRU, LSTM, TCN]
nomes_arquiteturas = ['FNN', 'CNN', 'RNN', 'GRU', 'LSTM', 'TCN']

# ==========================================================
# CALCULAR PORCENTAGEM POR FASE
# ==========================================================

otimizadores = ['SGD', 'Adam', 'RMSprop']
total_por_fase = [0] * len(fases)
contagem_por_fase_otimizador = {opt: [0]*len(fases) for opt in otimizadores}

for fase_idx in range(len(fases)):
    for arquitetura in arquiteturas:
        opt = arquitetura[fase_idx]
        if opt != '-':
            total_por_fase[fase_idx] += 1
            if opt in contagem_por_fase_otimizador:
                contagem_por_fase_otimizador[opt][fase_idx] += 1

# Converter para porcentagem
porcentagens = {}
for opt in otimizadores:
    porcentagens[opt] = [ (c/total_por_fase[fase_idx]*100) if total_por_fase[fase_idx] > 0 else 0 
                          for fase_idx, c in enumerate(contagem_por_fase_otimizador[opt]) ]

# ==========================================================
# PLOTAR
# ==========================================================

cores = {'SGD': 'blue', 'Adam': 'green', 'RMSprop': 'red'}
fig, ax = plt.subplots(figsize=(10, 6))

bottom = np.zeros(len(fases))
for opt in otimizadores:
    valores = porcentagens[opt]
    if sum(valores) > 0:
        ax.bar(fases, valores, bottom=bottom, label=opt, color=cores[opt], alpha=0.7)
        bottom += np.array(valores)

ax.set_ylabel('Porcentagem (%)', fontsize=12)
ax.set_xlabel('Fase', fontsize=12)
ax.set_title('Distribuição dos Otimizadores por Fase (%)', fontsize=14)
ax.legend()
ax.set_ylim(0, 100)

# Adicionar valores nas barras
for i, fase in enumerate(fases):
    y = 0
    for opt in otimizadores:
        valor = porcentagens[opt][i]
        if valor > 5:
            ax.text(i, y + valor/2, f'{valor:.0f}%', ha='center', va='center', fontsize=9)
        y += valor

plt.tight_layout()
plt.show()

# Mostrar também a contagem
print("\n=== CONTAGEM BRUTA POR FASE ===")
for i, fase in enumerate(fases):
    print(f"\n{fase}: Total de {total_por_fase[i]} modelos")
    for opt in otimizadores:
        print(f"  {opt}: {contagem_por_fase_otimizador[opt][i]} ({porcentagens[opt][i]:.0f}%)")
