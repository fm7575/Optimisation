import json
import os

# Fonction pour charger et analyser un fichier JSON
def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Classe pour interpréter les données
class CityGraph:
    def __init__(self, json_data):
        self.comment = json_data.get("comment", "No comment")
        self.battery_capacity = json_data.get("batteryCapacity", 0)
        self.num_days = json_data.get("numDays", 0)
        self.intersections = json_data.get("intersections", [])
        self.roads = json_data.get("roads", [])
        
        # Dictionnaires pour un accès rapide
        self.intersections_dict = {i['id']: i for i in self.intersections}
        self.adjacency_list = self.build_adjacency_list()

    def build_adjacency_list(self):
        # Construire une liste d'adjacence pour représenter le graphe
        adjacency_list = {i['id']: [] for i in self.intersections}
        for road in self.roads:
            adjacency_list[road["intersectionId1"]].append((road["intersectionId2"], road["length"], road["isOneWay"]))
            if not road["isOneWay"]:
                adjacency_list[road["intersectionId2"]].append((road["intersectionId1"], road["length"], road["isOneWay"]))
        return adjacency_list

    def display_summary(self):
        print(f"Comment: {self.comment}")
        print(f"Battery Capacity: {self.battery_capacity}")
        print(f"Number of Days: {self.num_days}")
        print(f"Number of Intersections: {len(self.intersections)}")
        print(f"Number of Roads: {len(self.roads)}")
        print("\nAdjacency List:")
        for key, neighbors in self.adjacency_list.items():
            print(f"  Intersection {key}: {neighbors}")

# Fonction principale pour traiter tous les fichiers JSON
def process_datasets(dataset_folder):
    # Lister tous les fichiers JSON dans le dossier datasets
    for file_name in os.listdir(dataset_folder):
        if file_name.endswith('.json'):
            file_path = os.path.join(dataset_folder, file_name)
            print(f"\n--- Traitement du fichier : {file_name} ---")
            city_data = load_json(file_path)
            city_graph = CityGraph(city_data)
            city_graph.display_summary()

# Exemple d'utilisation
if __name__ == "__main__":
    # Chemin vers le premier fichier JSON
    file_path = os.path.join("starter_kit", "datasets", "1_example.json")
    
    # Charger et interpréter les données
    city_data = load_json(file_path)
    city_graph = CityGraph(city_data)
    city_graph.display_summary()
