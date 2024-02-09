import random
import matplotlib.pyplot as plt


def get_rolls(n):
    return [random.randint(1, 6) + random.randint(1, 6) for _ in range(n)]


def get_probabilities(rolls):
    counts = {k: 0 for k in range(2, 13)}

    for roll in rolls:
        counts[roll] += 1

    probabilities = {}

    for roll in counts:
        probabilities[roll] = counts[roll] / len(rolls)

    return probabilities


def plot_probabilities(probabilities):
    plt.bar(probabilities.keys(), probabilities.values())
    plt.xlabel('Сума гральних кубиків')
    plt.ylabel('Вірогідність')
    plt.show()


def print_probabilities(probabilities):
    print(f"{'Сума':<4} | {'Вірогідність':<12}")
    print(f"{'-' * 4:<4} | {'-' * 12:<12}")
    for roll, probability in probabilities.items():
        print(f"{roll:<4} | {probability:<12.4f}")


if __name__ == '__main__':
    n = 1_000_000
    rolls = get_rolls(n)
    probabilities = get_probabilities(rolls)
    print_probabilities(probabilities)
    plot_probabilities(probabilities)
