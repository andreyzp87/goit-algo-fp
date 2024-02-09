def greedy_algorithm(items: dict, budget: int) -> list:
    keys_sorted = sorted(items.keys(), key=lambda x: items[x]['calories'] / items[x]['cost'], reverse=True)

    selected_items = []
    total_cost = 0
    for key in keys_sorted:
        if total_cost + items[key]['cost'] <= budget:
            selected_items.append(key)
            total_cost += items[key]['cost']

    return selected_items


def dynamic_programming(items: dict, budget: int) -> list:
    keys = list(items.keys())
    n = len(keys)
    K = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            prev_key = keys[i - 1]
            if items[prev_key]['cost'] > w:
                K[i][w] = K[i - 1][w]
            else:
                K[i][w] = max(K[i - 1][w], K[i - 1][w - items[prev_key]['cost']] + items[prev_key]['calories'])

    selected_items = []
    for i in range(len(items), 0, -1):
        if K[i][budget] != K[i - 1][budget]:
            prev_key = keys[i - 1]
            selected_items.append(prev_key)
            budget -= items[prev_key]['cost']

    return selected_items


if __name__ == '__main__':
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    budget = int(input("Enter your budget (100): ").strip() or 100)

    selected_items = greedy_algorithm(items, budget)
    print("Greedy items:", selected_items)

    selected_items = dynamic_programming(items, budget)
    print("Dynamic items:", selected_items)
