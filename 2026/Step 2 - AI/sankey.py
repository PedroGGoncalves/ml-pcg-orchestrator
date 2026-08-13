import plotly.graph_objects as go

import random

def cor_aleatoria():
    return f"rgba({random.randint(0,255)},{random.randint(0,255)},{random.randint(0,255)},1)"

# =========================
# 1. DADOS (SEU EXEMPLO)
# =========================

dados = {
    "1": {
        "atributos": {"M": 40, "T": 30, "G": 20, "E": 10},
        "usuarios": [
            {"id": 3, "peso": 0.265, "n": 0.51},
            {"id": 6, "peso": 0.165, "n": 0.70}
        ]
    },
    "2": {
        "atributos": {"M": 20, "T": 40, "G": 10, "E": 30},
        "usuarios": [
            {"id": 3, "peso": 0.376, "n": 0.73},
            {"id": 5, "peso": 0.093, "n": 0.30}
        ]
    },
    "3": {
        "atributos": {"M": 30, "T": 10, "G": 40, "E": 20},
        "usuarios": [
            {"id": 3, "peso": 0.307, "n": 0.59},
            {"id": 6, "peso": 0.127, "n": 0.54}
        ]
    },
    "4": {
        "atributos": {"M": 20, "T": 30, "G": 10, "E": 40},
        "usuarios": [
            {"id": 3, "peso": 0.474, "n": 0.92},
            {"id": 6, "peso": 0.159, "n": 0.68}
        ]
    },
    "5": {
        "atributos": {"M": 40, "T": 20, "G": 10, "E": 30},
        "usuarios": [
            {"id": 3, "peso": 0.223, "n": 0.43},
            {"id": 6, "peso": 0.153, "n": 0.65},
            {"id": 7, "peso": 0.135, "n": 0.86}
        ]
    }
}

# =========================
# 2. CONVERTER PARA SANKEY
# =========================

def criar_sankey(dados):
    usuarios = set()
    itens = set()

    source = []
    target = []
    value = []

    # coleta nós
    for item_id, info in dados.items():

        a = info["atributos"]

        item_nome = (
            f"M:{a['M']} "
            f"T:{a['T']} "
            f"G:{a['G']} "
            f"E:{a['E']}"
        )

        itens.add(item_nome)

        for u in info["usuarios"]:
            usuario_nome = f"Usuário {u['id']}"
            usuarios.add(usuario_nome)

    # ordena (IMPORTANTE)
    usuarios = sorted(list(usuarios))
    itens = sorted(list(itens))

    labels = usuarios + itens

    # mapa nome → índice
    index = {nome: i for i, nome in enumerate(labels)}

    # cria links
    for item_id, info in dados.items():
        a = info["atributos"]

        item_nome = (
            f"M:{a['M']} "
            f"T:{a['T']} "
            f"G:{a['G']} "
            f"E:{a['E']}"
        )

        for u in info["usuarios"]:
            usuario_nome = f"Usuário {u['id']}"

            source.append(index[usuario_nome])
            target.append(index[item_nome])
            value.append(u["peso"])  # peso vira espessura

    return labels, source, target, value


# =========================
# 3. PLOT SANKEY
# =========================

def plotar_sankey(labels, source, target, value):

    # separa usuários (primeira metade dos labels)
    usuarios = [label for label in labels if label.startswith("Usuário")]

    # cria cor aleatória por usuário
    def cor_rgb():
        return (
            random.randint(0,255),
            random.randint(0,255),
            random.randint(0,255)
        )

    cores_usuarios = {u: cor_rgb() for u in usuarios}

    # cor dos nós
    node_colors = [
        f"rgba({r},{g},{b},1)" if label in cores_usuarios else "rgba(150,150,150,0.8)"
        for label in labels
        for (r,g,b) in [cores_usuarios.get(label, (150,150,150))]
    ]

    # cor dos links baseada no usuário (source)
    link_colors = [
        f"rgba({r},{g},{b},{0.3 + 0.7*v})"
        for s, v in zip(source, value)
        for (r, g, b) in [cores_usuarios[labels[s]]]
    ]

    fig = go.Figure(data=[go.Sankey(
        arrangement="snap",
        node=dict(
            pad=20,
            thickness=20,
            label=labels,
            color=node_colors
        ),
        link=dict(
            source=source,
            target=target,
            value=value,
            label=[f"{v:.3f}" for v in value],
            color=link_colors
        )
    )])

    fig.update_layout(
        title_text="Fluxo Usuários → Itens (Sankey)",
        font_size=12
    )
    fig.show()

# =========================
# 4. EXECUÇÃO
# =========================
random.seed(42)
labels, source, target, value = criar_sankey(dados)
plotar_sankey(labels, source, target, value)
