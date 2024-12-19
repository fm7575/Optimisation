import json
from collections import defaultdict
import heapq
import math

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
            graph[u].append((v,length))
        else:
            # bidirectionnel
            graph[u].append((v,length))
            graph[v].append((u,length))
    return graph

def compute_in_out_degrees(graph):
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    nodes = set(graph.keys())
    for u in graph:
        for (v,length) in graph[u]:
            out_degree[u]+=1
            in_degree[v]+=1
            nodes.add(u)
            nodes.add(v)
    for n in nodes:
        if n not in in_degree:
            in_degree[n]=0
        if n not in out_degree:
            out_degree[n]=0
    return in_degree, out_degree

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph.keys()}
    dist[start] = 0
    heap = [(0,start)]
    while heap:
        d,u = heapq.heappop(heap)
        if d>dist[u]:
            continue
        for (v,length) in graph[u]:
            nd = d+length
            if nd<dist[v]:
                dist[v]=nd
                heapq.heappush(heap,(nd,v))
    return dist

def dijkstra_with_path(graph, start):
    dist = {node: float('inf') for node in graph.keys()}
    prev = {node: None for node in graph.keys()}
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d,u = heapq.heappop(heap)
        if d>dist[u]:
            continue
        for (v,length) in graph[u]:
            nd = d+length
            if nd<dist[v]:
                dist[v]=nd
                prev[v]=u
                heapq.heappush(heap,(nd,v))
    return dist, prev

def reconstruct_path(prev, start, end):
    if start == end:
        return [start]
    if prev[end] is None and end != start:
        return []
    path = []
    cur = end
    while cur is not None:
        path.append(cur)
        cur = prev[cur]
    path.reverse()
    return path

def is_eulerian(in_degree, out_degree):
    # Vérifie si in_degree(n) == out_degree(n) pour tous n
    for n in set(list(in_degree.keys())+list(out_degree.keys())):
        if in_degree[n] != out_degree[n]:
            return False
    return True

def all_pairs_shortest_paths(graph):
    # On exécute Dijkstra pour chaque nœud
    dist_all = {}
    for n in graph.keys():
        dist_all[n] = dijkstra(graph,n)
    return dist_all

def min_weight_perfect_matching(cost_matrix):
    # Algorithme hongrois pour le perfect matching minimum sur un bipartite complet
    N = len(cost_matrix)
    u = [0]*(N+1)
    v = [0]*(N+1)
    p = [0]*(N+1)
    way = [0]*(N+1)
    for i in range(1,N+1):
        p[0]=i
        j0=0
        minv=[math.inf]*(N+1)
        used=[False]*(N+1)
        while True:
            used[j0]=True
            i0=p[j0]; j1=0
            delta=math.inf
            for j in range(1,N+1):
                if not used[j]:
                    cur=cost_matrix[i0-1][j-1]-u[i0]-v[j]
                    if cur<minv[j]:
                        minv[j]=cur; way[j]=j0
                    if minv[j]<delta:
                        delta=minv[j]; j1=j
            for j in range(N+1):
                if used[j]:
                    u[p[j]]+=delta; v[j]-=delta
                else:
                    minv[j]-=delta
            j0=j1
            if p[j0]==0:
                break
        while True:
            j1=way[j0]
            p[j0]=p[j1]
            j0=j1
            if j0==0:
                break
    match=[0]*(N+1)
    for j in range(1,N+1):
        match[p[j]]=j
    return [m-1 for m in match[1:]]

def eulerize_graph(graph):
    in_degree, out_degree = compute_in_out_degrees(graph)
    if is_eulerian(in_degree, out_degree):
        return graph

    # Identifier les surplus
    surplus_out=[]
    surplus_in=[]
    nodes = set(in_degree.keys()).union(set(out_degree.keys()))
    for n in nodes:
        diff = out_degree[n]-in_degree[n]
        if diff>0:
            for _ in range(diff):
                surplus_out.append(n)
        elif diff<0:
            for _ in range(-diff):
                surplus_in.append(n)
    # On suppose surplus_out et surplus_in de même taille
    dist_all = all_pairs_shortest_paths(graph)
    N = len(surplus_out)
    cost_matrix = [[dist_all[o][i] for i in surplus_in] for o in surplus_out]
    match = min_weight_perfect_matching(cost_matrix)

    # On doit dupliquer les arcs du plus court chemin entre surplus_out[i] et surplus_in[match[i]]
    def reconstruct_shortest_path(graph, start, end):
        # Refaire un dijkstra_with_path pour un chemin précis
        dist, prev = dijkstra_with_path(graph, start)
        if dist[end]==float('inf'):
            return []
        path_nodes = reconstruct_path(prev,start,end)
        # Convertir en arcs
        path_arcs = []
        # Pour chaque edge successif du path:
        for a in range(len(path_nodes)-1):
            x=path_nodes[a]
            y=path_nodes[a+1]
            # Chercher longueur arc x->y
            length_xy=None
            for (w,ll) in graph[x]:
                if w==y:
                    length_xy=ll; break
            if length_xy is None:
                # Pas trouvé, anormal si le chemin existe
                return []
            path_arcs.append((x,y,length_xy))
        return path_arcs

    for i, o_node in enumerate(surplus_out):
        i_node = surplus_in[match[i]]
        path_arcs = reconstruct_shortest_path(graph, o_node, i_node)
        # Ajouter ces arcs au graph
        for (x,y,l) in path_arcs:
            graph[x].append((y,l))

    return graph

def hierholzer_arcs(graph, start=0):
    adj = {u: adj_list[:] for u, adj_list in graph.items()}
    stack = [(start,None)]
    path=[]
    while stack:
        u, arcinfo = stack[-1]
        if adj[u]:
            (v,l)=adj[u].pop()
            stack.append((v,(u,v,l)))
        else:
            stack.pop()
            if arcinfo is not None:
                path.append(arcinfo)
    path.reverse()
    return path

def can_return_to_charge(graph, current, charge_station, remaining_battery):
    dist = dijkstra(graph, current)
    return dist.get(charge_station, float('inf'))<=remaining_battery

def segment_itinerary(euler_arcs, graph, batteryCapacity, numDays, charge_station):
    final_itinerary = []
    current_day = 1
    current_battery = batteryCapacity

    if not euler_arcs:
        # Aucun arc, juste retourner la station de charge si pas déjà présent
        if not final_itinerary or final_itinerary[-1] != charge_station:
            final_itinerary.append(charge_station)
        return charge_station, final_itinerary

    i = 0
    current_pos = euler_arcs[0][0]  # Premier arc part de ce nœud
    final_itinerary.append(current_pos)

    total_arcs = len(euler_arcs)

    while i < total_arcs:
        (u,v,length) = euler_arcs[i]

        # Vérifier si on est bien au noeud u, sinon trouver un chemin pour y aller
        if u != current_pos:
            dist, prev = dijkstra_with_path(graph, current_pos)
            if dist[u] == float('inf'):
                # Pas de chemin pour rejoindre u
                break
            path_to_u = reconstruct_path(prev, current_pos, u)
            # Ajouter tous les noeuds du chemin sauf le premier (déjà dans itinerary)
            for node in path_to_u[1:]:
                final_itinerary.append(node)
            current_pos = u
            # Maintenant on est au bon nœud

        # Avant d'emprunter l'arc u->v, vérifier la batterie
        if length > current_battery:
            # Pas assez de batterie pour cet arc
            if current_day < numDays:
                # On tente de rentrer à la station
                dist, prev = dijkstra_with_path(graph, current_pos)
                if dist[charge_station] <= current_battery:
                    # On rentre se recharger
                    path_to_charge = reconstruct_path(prev, current_pos, charge_station)
                    for node in path_to_charge[1:]:
                        final_itinerary.append(node)
                    current_day += 1
                    current_battery = batteryCapacity
                    current_pos = charge_station
                    # On retentera cet arc plus tard
                    continue
                else:
                    # Impossible de rentrer, on ne peut ni avancer ni rentrer, on arrête.
                    break
            else:
                # Dernier jour, pas assez de batterie, on s'arrête immédiatement
                break

        # On sait maintenant qu'on a assez de batterie pour cet arc
        future_battery = current_battery - length

        # Si ce n'est pas le dernier jour, vérifier si on pourra rentrer plus tard
        if current_day < numDays:
            if not can_return_to_charge(graph, v, charge_station, future_battery):
                # On ne pourra pas rentrer plus tard, donc on rentre maintenant
                dist, prev = dijkstra_with_path(graph, current_pos)
                if dist[charge_station] <= current_battery:
                    # On rentre maintenant
                    path_to_charge = reconstruct_path(prev, current_pos, charge_station)
                    for node in path_to_charge[1:]:
                        final_itinerary.append(node)
                    current_day += 1
                    current_battery = batteryCapacity
                    current_pos = charge_station
                    # On retentera cet arc plus tard
                    continue
                else:
                    # Pas de solution parfaite, on continue quand même
                    # (Non optimal, mais on respecte la logique initiale)
                    pass

        # Parcourir l'arc (u->v)
        final_itinerary.append(v)
        current_pos = v
        current_battery = future_battery
        i += 1  # arc suivant

        # Si on a tout parcouru et qu'on est au dernier jour, on termine
        if i == total_arcs and current_day == numDays:
            break

    return charge_station, final_itinerary



if __name__=="__main__":
    # Vous pouvez tester avec le défi 1 et le défi 2
    # Par exemple :
    # input_file = "starter_kit/datasets/1_example.json"
    # input_file = "starter_kit/datasets/2_pacman.json"
    input_file = "starter_kit/datasets/2_pacman.json" # Modifiez ici selon le défi

    data=load_data(input_file)
    batteryCapacity = data["batteryCapacity"]
    numDays = data["numDays"]
    roads = data["roads"]
    charge_station=0

    graph=build_graph(roads)
    graph=eulerize_graph(graph)  # Eulerisation si nécessaire
    euler_arcs=hierholzer_arcs(graph, start=charge_station)
    charge_station_id, final_itinerary = segment_itinerary(euler_arcs, graph, batteryCapacity, numDays, charge_station)

    output={
        "chargeStationId": charge_station_id,
        "itinerary": final_itinerary
    }

    with open("output2.json","w") as f:
        json.dump(output,f,indent=4)
