import matplotlib.pyplot as plt
import numpy as np

# ==========================================================
# DADOS: 1º MELHOR e 2º MELHOR por fase
# ==========================================================

fases = ['Fase 1', 'Fase 2', 'Fase 3', 'Fase 4']

# 1º melhor otimizador por fase (para cada arquitetura)
FNN_1o  = ['Adam', 'SGD', 'Adam', 'Adam']
FNN_2o  = ['SGD', 'Adam', 'SGD', 'SGD']

LSTM_1o  = ['RMSprop', 'SGD', 'SGD', 'SGD']
LSTM_2o  = ['SGD', 'Adam', 'Adam', 'Adam']

LSTM_FNN_1o  = ['SGD', 'Adam', 'Adam', 'SGD']
LSTM_FNN_2o  = ['Adam', 'RMSprop', 'SGD', 'Adam']

LSTM_CNN_1o  = ['SGD', 'Adam', 'Adam', 'SGD']
LSTM_CNN_2o  = ['Adam', 'RMSprop', 'SGD', 'Adam']

CNN_1o  = ['Adam', 'RMSprop', 'RMSprop', 'SGD']
CNN_2o  = ['SGD', 'Adam', 'Adam', 'Adam']

RNN_1o  = ['SGD', 'SGD', 'SGD', 'SGD']
RNN_2o  = ['Adam', 'Adam', 'Adam', 'Adam']

GRU_1o  = ['SGD', 'Adam', 'RMSprop', 'SGD']
GRU_2o  = ['Adam', 'SGD', 'SGD', 'Adam']


GRU_CNN_1o  = ['SGD', 'Adam', 'RMSprop', 'SGD']
GRU_CNN_2o  = ['Adam', 'SGD', 'SGD', 'Adam']

GRU_MLP_1o  = ['RMSprop', 'Adam', 'Adam', 'SGD']
GRU_MLP_2o  = ['Adam', 'SGD', 'SGD', 'Adam']

GRU_RNN_1o  = ['SGD', 'SGD', 'SGD', 'SGD']
GRU_RNN_2o  = ['RMSprop', 'RMSprop', 'SGD', 'Adam']

LSTM_RNN_1o  = ['SGD', 'SGD', 'SGD', 'SGD']
LSTM_RNN_2o  = ['Adam', 'Adam', 'Adam', 'Adam']

TCN_1o  = ['Adam', 'Adam', 'Adam', 'Adam']
TCN_2o  = ['RMSprop', 'SGD', 'SGD', 'SGD']

TCN_LSTM_1o  = ['SGD', 'SGD', 'SGD', 'SGD']
TCN_LSTM_2o  = ['RMSprop', 'RMSprop', 'Adam', 'Adam']

TCN_GRU_1o  = ['SGD', 'RMSprop', 'SGD', 'SGD']
TCN_GRU_2o  = ['RMSprop', 'SGD', 'Adam', 'Adam']

# ==========================================================
# CALCULAR PORCENTAGENS
# ==========================================================

arquiteturas_1o = [
    FNN_1o, CNN_1o, RNN_1o, GRU_1o, LSTM_1o,
    LSTM_FNN_1o, LSTM_CNN_1o, GRU_CNN_1o, GRU_MLP_1o,
    GRU_RNN_1o, LSTM_RNN_1o, TCN_1o, TCN_LSTM_1o, TCN_GRU_1o
]

arquiteturas_2o = [
    FNN_2o, CNN_2o, RNN_2o, GRU_2o, LSTM_2o,
    LSTM_FNN_2o, LSTM_CNN_2o, GRU_CNN_2o, GRU_MLP_2o,
    GRU_RNN_2o, LSTM_RNN_2o, TCN_2o, TCN_LSTM_2o, TCN_GRU_2o
]
otimizadores = ['SGD', 'Adam', 'RMSprop']
cores = {
    'SGD': 'blue',
    'Adam': 'green',
    'RMSprop': 'gray'
}

def calcular_porcentagens(dados):
    total_por_fase = [0]*len(fases)
    contagem = {opt: [0]*len(fases) for opt in otimizadores}
    
    for fase_i in range(len(fases)):
        for arquitetura in dados:
            opt = arquitetura[fase_i]
            total_por_fase[fase_i] += 1
            if opt in contagem:
                contagem[opt][fase_i] += 1
    
    porcentagens = {}
    for opt in otimizadores:
        porcentagens[opt] = [c/total_por_fase[fase_i]*100 if total_por_fase[fase_i]>0 else 0 
                              for fase_i, c in enumerate(contagem[opt])]
    return porcentagens

porcentagens_1o = calcular_porcentagens(arquiteturas_1o)
porcentagens_2o = calcular_porcentagens(arquiteturas_2o)

# ==========================================================
# PLOTAR: BARRAS LADO A LADO POR FASE
# ==========================================================

fig, ax = plt.subplots(figsize=(12, 6))

x = np.arange(len(fases))  # posições das fases
width = 0.35  # largura de cada barra

# Barras do 1º melhor (esquerda)
bottom1 = np.zeros(len(fases))
for opt in otimizadores:
    valores = porcentagens_1o[opt]
    if sum(valores) > 0:
        ax.bar(x - width/2, valores, width, bottom=bottom1, label=f'1º - {opt}', color=cores[opt], alpha=0.7)
        bottom1 += np.array(valores)

# Barras do 2º melhor (direita)
bottom2 = np.zeros(len(fases))
for opt in otimizadores:
    valores = porcentagens_2o[opt]
    if sum(valores) > 0:
        ax.bar(x + width/2, valores, width, bottom=bottom2, label=f'2º - {opt}', color=cores[opt], alpha=0.5, edgecolor='black', linewidth=1)
        bottom2 += np.array(valores)

ax.set_ylabel('Porcentagem (%)', fontsize=12)
ax.set_xlabel('Fase', fontsize=12)
ax.set_title('Distribuição dos Otimizadores: 1º Melhor vs 2º Melhor', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(fases)
ax.set_ylim(0, 100)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()
