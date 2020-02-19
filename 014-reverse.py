from linked_list import LinkedList,Node


class MyLinkedList(LinkedList):

    def add_reverse(self, first_list, second_list):
        # See constraints
        if first_list is None or second_list is None:
            return None
        head = self._add_reverse(first_list.head, second_list.head, 0)
        return MyLinkedList(head)

    def _add_reverse(self, first_node, second_node, carry):
        # Base case
        if first_node is None and second_node is None and not carry:
            return None

        # Recursive case
        value = carry
        value += first_node.data if first_node is not None else 0
        value += second_node.data if second_node is not None else 0
        carry = 1 if value >= 10 else 0
        value %= 10
        node = Node(value)
        node.next = self._add_reverse(
            first_node.next if first_node is not None else None,
            second_node.next if first_node is not None else None,
            carry)
        return node