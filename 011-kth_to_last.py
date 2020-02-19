from linked_list import LinkedList


class MyLinkedList(LinkedList):

    def kth_to_last_elem(self, k):
        if self.head is None:
            return None
        fast = self.head
        slow = self.head

        # Give fast a headstart, incrementing it
        # once for k = 1, twice for k = 2, etc
        for _ in range(k):
            fast = fast.next
            # If k >= num elements, return None
            if fast is None:
                return None

        # Increment both pointers until fast reaches the end
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        return slow.data