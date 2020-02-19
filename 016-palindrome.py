from linked_list import LinkedList


class MyLinkedList(LinkedList):

    def is_palindrome(self):
        if self.head is None or self.head.next is None:
            return False
        curr = self.head
        reversed_list = MyLinkedList()
        length = 0

        # Reverse the linked list
        while curr is not None:
            reversed_list.insert_to_front(curr.data)
            length += 1
            curr = curr.next

        # Compare the reversed list with the original list
        # Only need to compare the first half
        iterations = length // 2
        curr = self.head
        curr_reversed = reversed_list.head
        for _ in range(iterations):
            if curr.data != curr_reversed.data:
                return False
            curr = curr.next
            curr_reversed = curr_reversed.next
        return True