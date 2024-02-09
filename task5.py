import heapq
from collections import deque
from colour import Color
from task4 import draw_tree, get_heap_tree, Node


def dfs(node: Node, callback: callable(Node)):
    if node is None:
        return

    callback(node)

    dfs(node.left, callback)
    dfs(node.right, callback)


def bfs(node: Node, callback: callable(Node)):
    queue = deque([node])

    while queue:
        node = queue.popleft()
        callback(node)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


if __name__ == '__main__':
    nodes = [99, 0, 4, 5, 6, 10, 1, 3]
    heapq.heapify(nodes)
    heap_tree = get_heap_tree(nodes, 0)

    dfs_colors = list(Color("grey").range_to(Color("green"), len(nodes)))
    bfs_colors = list(Color("grey").range_to(Color("red"), len(nodes)))

    dfs(heap_tree, lambda node: setattr(node, "color", dfs_colors.pop().hex))
    draw_tree(heap_tree, "DFS")

    bfs(heap_tree, lambda node: setattr(node, "color", bfs_colors.pop().hex))
    draw_tree(heap_tree, "BFS")
