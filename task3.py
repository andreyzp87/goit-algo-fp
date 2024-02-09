import heapq


def find_min_distances(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    min_heap = [(0, start)]

    while min_heap:
        current_distance, current_vertex = heapq.heappop(min_heap)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))

    return distances


if __name__ == '__main__':
    graph = {
        "Академмістечко": {"Театральна": 30},
        "Театральна": {"Академмістечко": 30, "Золоті ворота": 5, "Хрещатик": 3},
        "Хрещатик": {"Театральна": 3, "Лісова": 30, "Майдан Незалежності": 5},
        "Лісова": {"Хрещатик": 30},
        "Виноградар": {"Золоті ворота": 20},
        "Золоті ворота": {"Виноградар": 20, "Палац спорту": 3, "Театральна": 5},
        "Палац спорту": {"Золоті ворота": 3, "Червоний хутір": 40, "Площа Льва Толстого": 5},
        "Червоний хутір": {"Палац спорту": 40},
        "Героїв Дніпра": {"Майдан Незалежності": 30},
        "Майдан Незалежності": {"Героїв Дніпра": 30, "Площа Льва Толстого": 3, "Хрещатик": 5},
        "Площа Льва Толстого": {"Майдан Незалежності": 3, "Одеська": 30, "Палац спорту": 5},
        "Одеська": {"Площа Льва Толстого": 30},
    }

    for vertex, neighbors in graph.items():
        print(f"{vertex}: {find_min_distances(graph, vertex)}")
