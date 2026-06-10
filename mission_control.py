missao = "Sentinela"
equipe = "Equipe Ômega"

dados_missao = [
[74, 22, 55, 69, 93],
[37, 88, 77, 21, 10],
[39, 15, 36, 74, 82],
[85, 27, 74, 37, 36],
[46, 21, 16, 94, 15],
[67, 79, 48, 46, 97]
]

areas_monitoradas = [
"Temperatura interna",
"Comunicação com a base",
"Sistema de energia",
"Suporte de oxigênio",
"Estabilidade operacional"
]

def analisar_temperatura(valor):
    if valor < 18:
        return "ATENÇÃO", 1
    elif valor <= 30:
        return "NORMAL", 0
    elif valor <= 35:
        return "ATENÇÃO", 1
    else:
        return "CRÍTICO", 2

def analisar_comunicacao(valor):
    if valor < 30:
        return "CRÍTICO", 2
    elif valor < 60:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0

def analisar_bateria(valor):
    if valor < 20:
        return "CRÍTICO", 2
    elif valor < 50:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0

def analisar_oxigenio(valor):
    if valor < 80:
        return "CRÍTICO", 2
    elif valor < 90:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0

def analisar_estabilidade(valor):
    if valor < 40:
        return "CRÍTICO", 2
    elif valor < 70:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0

def classificar_ciclo(risco):
    if risco <= 2:
        return "MISSÃO ESTÁVEL"
    elif risco <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"

riscos_ciclos = []
pontuacao_areas = [0, 0, 0, 0, 0]

print("=" * 60)
print("MISSION CONTROL AI")
print("=" * 60)
print("Missão:", missao)
print("Equipe:", equipe)
print("Quantidade de ciclos:", len(dados_missao))
print("=" * 60)

for i, ciclo in enumerate(dados_missao):

    temperatura, comunicacao, bateria, oxigenio, estabilidade = ciclo

classificacoes = [
    analisar_temperatura(temperatura),
    analisar_comunicacao(comunicacao),
    analisar_bateria(bateria),
    analisar_oxigenio(oxigenio),
    analisar_estabilidade(estabilidade)
]

risco = 0

for j, item in enumerate(classificacoes):
    risco += item[1]
    pontuacao_areas[j] += item[1]

riscos_ciclos.append(risco)

print(f"\nCICLO {i+1}")
print("-" * 40)
print("Temperatura:", temperatura, "°C")
print("Comunicação:", comunicacao, "%")
print("Bateria:", bateria, "%")
print("Oxigênio:", oxigenio, "%")
print("Estabilidade:", estabilidade, "%")
print("Pontuação de risco:", risco)
print("Classificação:", classificar_ciclo(risco))

print("\n" + "=" * 60)
print("RELATÓRIO FINAL")
print("=" * 60)

media_temp = sum(l[0] for l in dados_missao) / len(dados_missao)
media_com = sum(l[1] for l in dados_missao) / len(dados_missao)
media_bat = sum(l[2] for l in dados_missao) / len(dados_missao)
media_oxi = sum(l[3] for l in dados_missao) / len(dados_missao)
media_est = sum(l[4] for l in dados_missao) / len(dados_missao)

print("Média de temperatura:", round(media_temp, 2))
print("Média de comunicação:", round(media_com, 2))
print("Média de bateria:", round(media_bat, 2))
print("Média de oxigênio:", round(media_oxi, 2))
print("Média de estabilidade:", round(media_est, 2))

maior_risco = max(riscos_ciclos)
ciclo_critico = riscos_ciclos.index(maior_risco) + 1

print("Ciclo mais crítico:", ciclo_critico)
print("Maior pontuação de risco:", maior_risco)

if riscos_ciclos[-1] > riscos_ciclos[0]:
    tendencia = "A missão apresentou tendência de piora."
elif riscos_ciclos[-1] < riscos_ciclos[0]:
    tendencia = "A missão apresentou tendência de melhora."
else:
    tendencia = "A missão permaneceu estável."

print("Tendência:", tendencia)

print("\nPontuação acumulada por área:")

for i in range(len(areas_monitoradas)):
    print(areas_monitoradas[i], "-", pontuacao_areas[i], "pontos")

indice_area = pontuacao_areas.index(max(pontuacao_areas))

print("\nÁrea mais afetada:")
print(areas_monitoradas[indice_area])

media_risco = sum(riscos_ciclos) / len(riscos_ciclos)

print("\nClassificação final da missão:")

if media_risco <= 2:
    print("MISSÃO ESTÁVEL")
elif media_risco <= 5:
    print("MISSÃO EM ATENÇÃO")
else:
    print("MISSÃO CRÍTICA")
