import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.ai_map_osm import RouteAI_OSM

def executar_rota():
    # Inicializa o planejador de rotas na região desejada
    planejador = RouteAI_OSM("São Paulo, Brazil")

    # Pontos de passagem (latitude, longitude)
    locais = [
        (-23.609903123319242, -46.768615411386975),  # Unifecaf Taboão
        (-23.590971, -46.654684),  # Parque Ibirapuera
        (-23.562124, -46.655645),  # Museu próximo
    ]

    caminho_completo = []
    distancia_acumulada = 0.0

    print(f"Iniciando cálculo da rota. Total de pontos: {len(locais)}\n")

    # Processa cada trecho entre pontos consecutivos
    for indice in range(len(locais) - 1):
        ponto_atual = locais[indice]
        proximo_ponto = locais[indice + 1]

        rota, distancia = planejador.find_route(ponto_atual, proximo_ponto, algorithm="astar")

        # Evita duplicar o último nó da rota anterior
        if caminho_completo:
            caminho_completo += rota[1:]
        else:
            caminho_completo = rota[:]

        distancia_acumulada += distancia

        print(f"Trecho {indice + 1} concluído: {round(distancia / 1000, 2)} km")

    print("\nResumo da rota:")
    print(f"Distância total percorrida: {round(distancia_acumulada / 1000, 2)} km")
    print(f"Quantidade total de nós no caminho: {len(caminho_completo)}")

    # Exibe o mapa com o trajeto final
    planejador.plot_route(caminho_completo)


if __name__ == "__main__":
    executar_rota()
