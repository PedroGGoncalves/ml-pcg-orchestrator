import matplotlib.pyplot as plt

# ==========================================================
# DADOS
# ==========================================================

# Número de camadas
camadas_modelos = [
    1, 2, 1, 1, 2,
    2, 1, 2, 1, 2,
    1, 2, 1, 1
]

# Dropout
dropout_modelos = [
    0.0, 0.0, 0.1, 0.0, 0.0,
    0.2, 0.1, 0.2, 0.1, 0.0,
    0.0, 0.0, 0.3, 0.0
]

# Learning rate
lr_modelos = [
    1e-3, 1e-4, 1e-3, 1e-3, 1e-4,
    1e-3, 1e-4, 5e-4, 5e-4, 1e-3,
    1e-3, 1e-4, 1e-3, 1e-4
]

# ==========================================================
# FUNÇÃO AUXILIAR
# ==========================================================

def calcular_porcentagens(lista, valores_possiveis):

    contagem = {v: 0 for v in valores_possiveis}

    for item in lista:
        if item in contagem:
            contagem[item] += 1

    total = len(lista)

    porcentagens = {
        v: (contagem[v] / total) * 100
        for v in valores_possiveis
    }

    return porcentagens

# ==========================================================
# PORCENTAGENS
# ==========================================================

camadas_possiveis = [1, 2, 3]
dropouts_possiveis = [0.0, 0.1, 0.2, 0.3]
lrs_possiveis = [1e-3, 5e-4, 1e-4, 1e-5]

porcentagens_camadas = calcular_porcentagens(
    camadas_modelos,
    camadas_possiveis
)

porcentagens_dropout = calcular_porcentagens(
    dropout_modelos,
    dropouts_possiveis
)

porcentagens_lr = calcular_porcentagens(
    lr_modelos,
    lrs_possiveis
)

# ==========================================================
# FIGURA
# ==========================================================

fig, ax = plt.subplots(figsize=(12, 6))

# ==========================================================
# CAMADAS
# ==========================================================

cores_camadas = {
    1: 'blue',
    2: 'green',
    3: 'gray'
}

left = 0

for camada in camadas_possiveis:

    valor = porcentagens_camadas[camada]

    if valor > 0:

        ax.barh(
            'Camadas',
            valor,
            left=left,
            color=cores_camadas[camada],
            label=f'{camada} camada(s)'
        )

        ax.text(
            left + valor/2,
            0,
            f'{valor:.0f}%',
            ha='center',
            va='center',
            fontsize=10,
            color='white',
            fontweight='bold'
        )

        left += valor

# ==========================================================
# DROPOUT
# ==========================================================

cores_dropout = {
    0.0: 'red',
    0.1: 'orange',
    0.2: 'purple',
    0.3: 'brown'
}

left = 0

for dropout in dropouts_possiveis:

    valor = porcentagens_dropout[dropout]

    if valor > 0:

        ax.barh(
            'Dropout',
            valor,
            left=left,
            color=cores_dropout[dropout],
            label=f'Dropout {dropout}'
        )

        ax.text(
            left + valor/2,
            1,
            f'{valor:.0f}%',
            ha='center',
            va='center',
            fontsize=10,
            color='white',
            fontweight='bold'
        )

        left += valor

# ==========================================================
# LEARNING RATE
# ==========================================================

cores_lr = {
    1e-3: 'cyan',
    5e-4: 'magenta',
    1e-4: 'lime',
    1e-5: 'black'
}

left = 0

for lr in lrs_possiveis:

    valor = porcentagens_lr[lr]

    if valor > 0:

        ax.barh(
            'Learning Rate',
            valor,
            left=left,
            color=cores_lr[lr],
            label=f'LR {lr}'
        )

        ax.text(
            left + valor/2,
            2,
            f'{valor:.0f}%',
            ha='center',
            va='center',
            fontsize=10,
            color='white',
            fontweight='bold'
        )

        left += valor

# ==========================================================
# CONFIGURAÇÕES
# ==========================================================

ax.set_xlim(0, 100)

ax.set_xlabel('Porcentagem (%)', fontsize=12)

ax.set_title(
    'Distribuição de Camadas, Dropout e Learning Rate',
    fontsize=14
)

# remover legendas duplicadas
handles, labels = ax.get_legend_handles_labels()

unique = dict(zip(labels, handles))

ax.legend(
    unique.values(),
    unique.keys(),
    bbox_to_anchor=(1.02, 1),
    loc='upper left'
)

plt.tight_layout()

plt.show()
