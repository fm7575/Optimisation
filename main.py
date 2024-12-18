import json
from collections import defaultdict
import heapq

def load_data(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def build_graph(roads):
    graph = defaultdict(list)
    for r in roads:
        u = r["intersectionId1"]
        v = r["intersectionId2"]
        length = r["length"]
        if r["isOneWay"]:
            graph[u].append((v, length))
        else:
            graph[u].append((v, length))
            graph[v].append((u, length))
    return graph

def hierholzer_arcs(graph, start=0):
    """
    Retourne la liste des arcs (u,v,length) dans l'ordre Eulerien.
    """
    # Créer une copie du graph pour retirer les arcs au fur et à mesure
    adj = {u:[] for u in graph}
    for u in graph:
        for (v,length) in graph[u]:
            adj[u].append((v,length))

    # Algorithme de Hierholzer
    stack = [(start, None)]
    path = []  # contiendra les arcs sous forme (u,v,length)
    while stack:
        u, arcinfo = stack[-1]
        if adj[u]:
            (v,length) = adj[u].pop()
            stack.append((v,(u,v,length)))
        else:
            stack.pop()
            if arcinfo is not None:
                path.append(arcinfo)
    # path contient les arcs en ordre inversé de découverte, inverser
    path.reverse()
    return path

def dijkstra(graph, start):
    dist = {}
    for node in graph.keys():
        dist[node] = float('inf')
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d,u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for (v,length) in graph[u]:
            nd = d + length
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap,(nd,v))
    return dist

def can_return_to_charge(graph, current, charge_station, remaining_battery):
    dist = dijkstra(graph, current)
    return dist.get(charge_station, float('inf')) <= remaining_battery

def segment_itinerary(euler_arcs, graph, batteryCapacity, numDays, charge_station):
    """
    euler_arcs est une liste d'arcs (u,v,length) représentant le parcours Eulerien.
    On va la parcourir et segmenter en journées.
    """
    final_itinerary = []
    current_day = 1
    current_battery = batteryCapacity
    
    if not euler_arcs:
        # Pas d'arcs, itinéraire trivial
        if final_itinerary[-1] != charge_station:
            final_itinerary.append(charge_station)

        return charge_station, final_itinerary

    # L'itinéraire commence au premier arc
    # Le premier nœud est l'origine du premier arc
    current_pos = euler_arcs[0][0]
    final_itinerary.append(current_pos)

    total_arcs = len(euler_arcs)
    arcs_done = 0

    for (u,v,length) in euler_arcs:
        # On est censé partir de u, current_pos doit être u
        if u != current_pos:
            # Incohérence, mais supposons que non
            pass
        
        # Vérifier si on a assez de batterie
        if length > current_battery:
            # Pas assez de batterie pour ce segment
            if current_day < numDays:
                # Rentrer au charge station
                dist = dijkstra(graph, current_pos)
                if dist[charge_station] <= current_battery:
                    # On rentre
                    # Pas de code pour reconstruire le chemin exact ici (amélioration possible)
                    if final_itinerary[-1] != charge_station:
                        final_itinerary.append(charge_station)

                    current_day += 1
                    current_battery = batteryCapacity
                    current_pos = charge_station
                else:
                    # Impossible de rentrer -> échec (cas non géré)
                    # On continue quand même (non optimal)
                    pass
            else:
                # Dernier jour, on arrête ici
                break

        # Avant d'avancer, vérifier si on pourra ensuite rentrer plus tard (si pas dernier jour)
        future_battery = current_battery - length
        if current_day < numDays:
            if not can_return_to_charge(graph, v, charge_station, future_battery):
                # On ne pourra pas rentrer plus tard, donc on rentre maintenant
                dist = dijkstra(graph, current_pos)
                if dist[charge_station] <= current_battery:
                    if final_itinerary[-1] != charge_station:
                        final_itinerary.append(charge_station)

                    current_day += 1
                    current_battery = batteryCapacity
                    current_pos = charge_station
                    # Maintenant on avance
                    future_battery = batteryCapacity - length
                else:
                    # Pas de solution parfaite, on continue
                    pass

        # Avancer
        final_itinerary.append(v)
        current_pos = v
        current_battery = future_battery
        arcs_done += 1

        # Si c'est le dernier jour et qu'on a tout parcouru, on s'arrête
        if arcs_done == total_arcs and current_day == numDays:
            break

    return charge_station, final_itinerary

if __name__ == "__main__":
    input_file = "starter_kit/datasets/2_pacman.json"
    data = load_data(input_file)
    batteryCapacity = data["batteryCapacity"]
    numDays = data["numDays"]
    roads = data["roads"]
    charge_station = 0

    graph = build_graph(roads)
    euler_arcs = hierholzer_arcs(graph, start=charge_station)
    charge_station_id, final_itinerary = segment_itinerary(euler_arcs, graph, batteryCapacity, numDays, charge_station)

    output = {
        "chargeStationId": charge_station_id,
        "itinerary": final_itinerary
    }

    with open("output2.json", "w") as f:
        json.dump(output, f, indent=4)
