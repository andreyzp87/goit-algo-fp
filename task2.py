import turtle


def draw_tree(level: int, size: float, angle: float = 30):
    if level < 1:
        return
    branch_size = 2 * size / 3
    turtle.forward(size)
    turtle.left(angle)
    draw_tree(level - 1, branch_size, angle)
    turtle.right(angle * 2)
    draw_tree(level - 1, branch_size, angle)
    turtle.left(angle)
    turtle.backward(size)


if __name__ == "__main__":
    level = int(input("Рівень рекурсії (7): ").strip() or 7)
    size = int(input("Розмір дерева (300): ").strip() or 300)
    angle = int(input("Кут відхилення гілок (30): ").strip() or 30)
    turtle.speed(0)
    turtle.left(90)
    draw_tree(level, size, angle)
    turtle.done()
