import json
import os
import heapq

class CityGraph:
    def __init__(self, json_data):
        self.battery_capacity = json_data["batteryCapacity"]
        self.num_days = json_data["numDays"]
        self.intersections = json_data["intersections"]
        self.roads = json_data["roads"]

        # Construire une liste d'adjacence
        self.graph = self.build_adjacency_list()
    
    def build_adjacency_list(self):
        adjacency_list = {i['id']: [] for i in self.intersections}
        for road in self.roads:
            adjacency_list[road["intersectionId1"]].append((road["intersectionId2"], road["length"], road["isOneWay"]))
            if not road["isOneWay"]:
                adjacency_list[road["intersectionId2"]].append((road["intersectionId1"], road["length"], road["isOneWay"]))
        return adjacency_list

    def greedy_traversal(self, start_point):
        visited_edges = set()  # Suivi des routes parcourues
        total_distance = 0

        for day in range(1, self.num_days + 1):
            print(f"\n--- Jour {day} ---")
            current_battery = self.battery_capacity
            current_point = start_point
            daily_distance = 0

            while current_battery > 0:
                next_edge = self.find_next_edge(current_point, visited_edges, current_battery)
                if not next_edge:  # Si aucune route valide n'est trouvée
                    print(f" Batterie faible ou aucune route disponible - Retour au point de recharge.")
                    daily_distance += self.return_to_recharge(current_point, start_point)
                    break

                length, next_point = next_edge  # Longueur d'abord
                # Ajouter la route visitée dans les deux sens si elle n'est pas à sens unique
                visited_edges.add((current_point, next_point))
                if not self.is_one_way(current_point, next_point):
                    visited_edges.add((next_point, current_point))

                print(f" Parcours : {current_point} -> {next_point}, Distance : {length}")
                current_point = next_point
                current_battery -= length
                daily_distance += length

            # Retour au point de recharge
            if current_point != start_point:
                print(f" Retour au point de recharge.")
                daily_distance += self.return_to_recharge(current_point, start_point)

            print(f" Distance totale pour le jour {day}: {daily_distance}")
            total_distance += daily_distance  # Ajouter la distance du jour au total

        print(f"\nDistance totale parcourue : {total_distance}")
        return total_distance


    def is_one_way(self, start, end):
        """ Vérifie si une route est à sens unique """
        for neighbor, length, is_one_way in self.graph[start]:
            if neighbor == end:
                return is_one_way
        return False



    def find_next_edge(self, current_point, visited_edges, current_battery):
        """ Trouver la route disponible la plus courte non visitée """
        edges = []
        for neighbor, length, _ in self.graph[current_point]:
            if (current_point, neighbor) not in visited_edges and length <= current_battery:
                heapq.heappush(edges, (length, neighbor))  # Ajouter la longueur en premier pour prioriser
        return heapq.heappop(edges) if edges else None


    def return_to_recharge(self, current_point, start_point):
        """ Retourner au point de recharge """
        recharge_distance = self.shortest_distance(current_point, start_point)
        print(f" Retour : {current_point} -> {start_point}, Distance : {recharge_distance}")
        return recharge_distance


    def shortest_distance(self, source, target):
        """ Trouver la distance la plus courte entre deux points """
        visited = set()
        distances = {node: float('inf') for node in self.graph}
        distances[source] = 0
        heap = [(0, source)]

        while heap:
            current_distance, current_node = heapq.heappop(heap)
            if current_node in visited:
                continue
            visited.add(current_node)

            for neighbor, length, _ in self.graph[current_node]:
                if distances[current_node] + length < distances[neighbor]:
                    distances[neighbor] = distances[current_node] + length
                    heapq.heappush(heap, (distances[neighbor], neighbor))

        return distances[target]

# Charger les données JSON
def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Exécution principale
if __name__ == "__main__":
    file_path = os.path.join("starter_kit", "datasets", "1_example.json")
    city_data = load_json(file_path)
    city_graph = CityGraph(city_data)

    start_point = 0  # Le point de recharge initial (par exemple l'intersection 0)
    city_graph.greedy_traversal(start_point)
