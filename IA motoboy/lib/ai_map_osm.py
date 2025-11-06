import osmnx as ox
import networkx as nx

class RouteAI_OSM:
    def __init__(self, city_name="São Paulo, Brazil"):
        print(f"Baixando mapa de {city_name} ...")
        self.graph = ox.graph_from_place(city_name, network_type="drive")
        self.graph = ox.add_edge_speeds(self.graph)
        self.graph = ox.add_edge_travel_times(self.graph)
        print("Mapa carregado com sucesso.")

    def find_route(self, start, end, algorithm="astar"):
        print(f"Calculando rota de {start} até {end} ...")
        orig_node = ox.distance.nearest_nodes(self.graph, X=start[1], Y=start[0])
        dest_node = ox.distance.nearest_nodes(self.graph, X=end[1], Y=end[0])

        if algorithm.lower() == "dijkstra":
            route = nx.shortest_path(self.graph, orig_node, dest_node, weight="length")
        else:
            route = nx.astar_path(self.graph, orig_node, dest_node, weight="length")

        length = nx.path_weight(self.graph, route, weight="length")

        print(f"Rota encontrada ({round(length/1000, 2)} km)")
        return route, length

    def plot_route(self, route):
        ox.plot_graph_route(self.graph, route, route_linewidth=4, node_size=0, bgcolor='white')