class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(data)


def sort_linked_list(lst: LinkedList) -> LinkedList:
    sorted_list = LinkedList()
    current_node = lst.head
    while current_node:
        sorted_list = _insert_into_sorted_list(sorted_list, current_node.data)
        current_node = current_node.next

    return sorted_list


def _insert_into_sorted_list(lst: LinkedList, data) -> LinkedList:
    node = Node(data)

    if lst.head is None or lst.head.data >= node.data:
        node.next = lst.head
        lst.head = node
        return lst

    current_node = lst.head
    while current_node.next and current_node.next.data < node.data:
        current_node = current_node.next

    node.next = current_node.next
    current_node.next = node
    return lst


def reverse_linked_list(lst: LinkedList) -> LinkedList:
    if lst.head is None or lst.head.next is None:
        return lst

    prev_node = None
    current_node = lst.head
    while current_node:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node

    lst.head = prev_node

    return lst


def merge_sorted_lists(list1: LinkedList, list2: LinkedList) -> LinkedList:
    result = LinkedList()

    node1 = list1.head
    node2 = list2.head

    while node1 or node2:
        if node2 is None or node1.data < node2.data or node1.data == node2.data:
            result.push(node1.data)
            node1 = node1.next if node1 else None

        if node1 is None or node2.data < node1.data or node1.data == node2.data:
            result.push(node2.data)
            node2 = node2.next if node2 else None

    return result


def print_linked_list(lst: LinkedList, name: str = "") -> None:
    if (name):
        print(name + ": ")

    if lst.head is None:
        print("List is empty")
        return

    node = lst.head

    while node:
        print(node.data, end=" ")
        node = node.next

    print("\n")


if __name__ == "__main__":
    list1 = LinkedList()
    list1.push('c')
    list1.push('a')
    list1.push('f')

    list2 = LinkedList()
    list2.push('g')
    list2.push('b')
    list2.push('d')

    print_linked_list(list1, 'List 1')
    print_linked_list(list2, 'List 2')

    list1 = sort_linked_list(list1)
    print_linked_list(list1, 'Sorted list 1')

    list2 = sort_linked_list(list2)
    print_linked_list(list2, 'Sorted list 2')

    merged_list = merge_sorted_lists(list1, list2)
    print_linked_list(merged_list, 'Merged list')

    reversed_list = reverse_linked_list(merged_list)
    print_linked_list(reversed_list, 'Reversed list')

    sorted_reversed_list = sort_linked_list(reversed_list)
    print_linked_list(sorted_reversed_list, 'Sorted reversed list')
