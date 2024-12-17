import json
import os
import heapq
 
class CityGraph:
    def __init__(self, json_data):
        self.battery_capacity = json_data["batteryCapacity"]
        self.num_days = json_data["numDays"]
        self.intersections = json_data["intersections"]
        self.roads = json_data["roads"]
        self.graph = self.build_adjacency_list()
        
    def build_adjacency_list(self):
        """ Construire une liste d'adjacence avec gestion des sens uniques """
        adjacency_list = {i['id']: [] for i in self.intersections}
        for road in self.roads:
            adjacency_list[road["intersectionId1"]].append((road["intersectionId2"], road["length"], road["isOneWay"]))
            if not road["isOneWay"]:
                adjacency_list[road["intersectionId2"]].append((road["intersectionId1"], road["length"], road["isOneWay"]))
        return adjacency_list
 
    def greedy_traversal(self, start_point):
        visited_edges = set()
        total_distance = 0  # Initialisation de la distance totale
        itinerary = [start_point]
        current_point = start_point
        current_battery = self.battery_capacity
 
        print("\n--- Début du parcours ---")
        while current_battery > 0:
            next_edge = self.find_next_edge(current_point, visited_edges, current_battery)
            if not next_edge:
                print(" Batterie épuisée ou aucune route disponible.")
                break
 
            length, next_point = next_edge
            # Ajouter la route dans visited_edges avec sens
            visited_edges.add((current_point, next_point))
            print(f" Parcours : {current_point} -> {next_point}, Distance : {length}")
            itinerary.append(next_point)
            current_point = next_point
            current_battery -= length
            total_distance += length  # Mise à jour de la distance totale
 
        print(f"\nDistance totale parcourue : {total_distance}")
        self.save_solution(start_point, itinerary, "solution.json")
        return total_distance
 
    def find_next_edge(self, current_point, visited_edges, current_battery):
        """ Trouver la prochaine route la plus courte, en respectant les sens uniques """
        edges = []
        for neighbor, length, is_one_way in self.graph[current_point]:
            if (current_point, neighbor) not in visited_edges and length <= current_battery:
                heapq.heappush(edges, (length, neighbor))
        return heapq.heappop(edges) if edges else None
 
    def save_solution(self, start_point, itinerary, output_file):
        """ Sauvegarder la solution sous forme JSON """
        solution = {
            "chargeStationId": start_point,
            "itinerary": itinerary
        }
        with open(output_file, 'w') as file:
            json.dump(solution, file, indent=4)
        print(f"\nSolution sauvegardée dans {output_file}")
 
# Fonction pour charger les données JSON
def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
 
# Exécution principale
if __name__ == "__main__":
    file_path = os.path.join("starter_kit", "datasets", "1_example.json")
    city_data = load_json(file_path)
    city_graph = CityGraph(city_data)
 
    start_point = 0  # Point de recharge initial
    city_graph.greedy_traversal(start_point)