from Simulacao import Simulacao
from classes.strategies.EstrategiaFelipe import EstrategiaFelipe
from classes.strategies.EstrategiaTotalmenteAleatoria import EstrategiaTotalmenteAleatoria

estrategias = (EstrategiaTotalmenteAleatoria(),
               EstrategiaFelipe(),
               EstrategiaTotalmenteAleatoria(),
               EstrategiaTotalmenteAleatoria())
resultados: dict[str, int] = dict()
simulacao = Simulacao(estrategias)
estado_final = simulacao.rodar_simulacao()
for jogador in estado_final.jogadores:
    resultados[jogador.nome] = int(jogador.vencedor)
for i in range(99):
    simulacao = Simulacao(estrategias)
    estado_final = simulacao.rodar_simulacao()
    for jogador in estado_final.jogadores:
        resultados[jogador.nome] += int(jogador.vencedor)
print()
for jogador, resultado in resultados.items():
    print(f'{jogador} - Vitórias: {resultado}')
