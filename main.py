import json
import os
import igraph as ig

class CityGraph:
    def __init__(self, json_data):
        self.battery_capacity = json_data["batteryCapacity"]
        self.num_days = json_data["numDays"]
        self.intersections = json_data["intersections"]
        self.roads = json_data["roads"]
        self.graph, self.edge_weights = self.build_graph()
        self.total_edges = len(self.graph.es)  # Nombre total d'arêtes

    def build_graph(self):
        """ Construire le graphe avec les intersections et les routes """
        graph = ig.Graph(directed=True)  # Graphe dirigé
        vertices = [i['id'] for i in self.intersections]
        graph.add_vertices(vertices)

        edge_list = []
        edge_weights = []

        for road in self.roads:
            edge_list.append((road["intersectionId1"], road["intersectionId2"]))
            edge_weights.append(road["length"])
            if not road["isOneWay"]:
                edge_list.append((road["intersectionId2"], road["intersectionId1"]))
                edge_weights.append(road["length"])

        graph.add_edges(edge_list)
        graph.es["weight"] = edge_weights
        return graph, edge_weights

    def greedy_traversal(self, start_point):
        visited_edges = set()
        total_distance = 0
        itinerary = [start_point]
        current_point = start_point
        current_battery = self.battery_capacity
        day = 1

        print("\n--- Début du parcours ---")
        while day <= self.num_days:
            # Vérifier si toutes les routes ont été parcourues
            if len(visited_edges) >= self.total_edges:
                print(" Toutes les routes ont été parcourues. Arrêt de l'algorithme.")
                break

            next_edge = self.find_next_edge(current_point, visited_edges, current_battery)
            
            if not next_edge:  # Retour au point de recharge
                if current_point == start_point:
                    print(f" Fin du jour {day}.")
                    day += 1
                    current_battery = self.battery_capacity
                    continue

                distance_to_recharge = self.shortest_path(current_point, start_point)
                total_distance += distance_to_recharge
                itinerary.append(start_point)
                print(f" Retour au point de recharge depuis {current_point}, Distance : {distance_to_recharge}")
                current_battery = self.battery_capacity
                current_point = start_point
                day += 1
                continue

            next_point, length = next_edge
            visited_edges.add((current_point, next_point))
            itinerary.append(next_point)
            print(f" Parcours : {current_point} -> {next_point}, Distance : {length}")
            current_point = next_point
            current_battery -= length
            total_distance += length

        print(f"\nDistance totale parcourue : {total_distance}")
        self.save_solution(itinerary, "solution.json")

    def find_next_edge(self, current_point, visited_edges, current_battery):
        """ Trouver la prochaine route valide avec la batterie restante """
        edges = []
        for neighbor in self.graph.neighbors(current_point, mode="out"):
            edge_id = self.graph.get_eid(current_point, neighbor)
            length = self.graph.es[edge_id]["weight"]
            if (current_point, neighbor) not in visited_edges and length <= current_battery:
                edges.append((neighbor, length))

        return min(edges, key=lambda x: x[1]) if edges else None

    def shortest_path(self, source, target):
        """ Calculer le plus court chemin entre deux points avec iGraph """
        path = self.graph.get_shortest_paths(source, to=target, weights="weight", output="epath")
        if path[0]:  # Si un chemin existe
            distance = sum(self.graph.es[edge]["weight"] for edge in path[0])
            return distance
        return float('inf')  # Si aucun chemin n'existe

    def save_solution(self, itinerary, output_file):
        """ Sauvegarder la solution sous forme JSON """
        solution = {
            "chargeStationId": itinerary[0],
            "itinerary": itinerary
        }
        with open(output_file, 'w') as file:
            json.dump(solution, file, indent=4)
        print(f"\nSolution sauvegardée dans {output_file}")

# Fonction pour charger les données JSON
def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

if __name__ == "__main__":
    # Correction du chemin pour le fichier JSON
    file_path = os.path.join("starter_kit", "datasets", "1_example.json")
    city_data = load_json(file_path)
    city_graph = CityGraph(city_data)
    city_graph.greedy_traversal(start_point=0)