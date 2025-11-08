## IA Map inteligente de Rotas 

Este projeto tem como objetivo otimizar rotas de entrega para a empresa fictícia **Sabor Express**, utilizando **Inteligência Artificial** e **modelagem de grafos** para reduzir tempo de entrega, minimizar custos e melhorar a eficiência operacional.

---

## 🧠 Abordagem Adotada

A solução representa a cidade como um **grafo**, onde:
- **Nós (vertices):** cruzamentos, pontos de entrega ou bairros
- **Arestas:** ruas que conectam os locais
- **Pesos:** distância ou tempo estimado para percorrer cada rua

O sistema utiliza dados do **OpenStreetMap (OSM)** via `OSMnx` para carregar o mapa real da cidade e `NetworkX` para manipulação do grafo.  
A rota é calculada ponto-a-ponto e exibida sobre o mapa.

---

## 🔍 Algoritmos Utilizados

| Algoritmo | Finalidade |
|----------|------------|
| **A\*** (A-Star) | Escolha principal para calcular o menor caminho usando heurística |
| **Dijkstra** | Alternativa para rotas sem heurística |
| **K-Means (planejado)** | Agrupamento de entregas próximas para criar zonas de entrega |
| **Haversine** | Cálculo de distância geográfica entre coordenadas |

---
## 🧾 Exemplo de Saída do Programa




```bash Baixando mapa de São Paulo, Brazil ... 


Mapa carregado com sucesso.

Iniciando cálculo da rota.
Total de pontos: 3


🔹 Calculando rota de (-23.609903123319242, -46.768615411386975)  até (-23.590971, -46.654684) ...

✅ Rota encontrada (14.35 km)
Trecho 1 concluído: 14.35 km


🔹 Calculando rota de (-23.590971, -46.654684) até (-23.562124, -46.655645) ...

✅ Rota encontrada (5.4 km)
Trecho 2 concluído: 5.4 km 

📌 Resumo da Rota
-----------------------------------------
Distância total percorrida: 19.75 km
Quantidade total de nós no caminho: 219

```
---

## 🗺️ Diagrama da Rota Calculada

A rota abaixo mostra o fluxo do trajeto gerado pelo algoritmo **A\***:

```mermaid
 graph TD 
    A["📍 Unifecaf Taboão da Serra"] -->|14.35 km| B["🌳 Parque Ibirapuera"]
    B -->|5.4 km| C["🏛️ Museu Próximo ao Ibirapuera"]

   Estética
    classDef ponto fill:#ffffff,stroke:#333,stroke-width:1px,border-radius:4px;
    class A,B,C ponto;

 ```
   <img width="1171" height="425" alt="mapa vscode" src="https://github.com/user-attachments/assets/ea62ca93-8467-4158-97bc-0e97ab3096c0" />
<img width="1530" height="647" alt="mapa google" src="https://github.com/user-attachments/assets/6d144774-67fe-4f9d-a8a8-31d24fac7f14" />

