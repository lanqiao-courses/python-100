from linked_list import LinkedList


class MyLinkedList(LinkedList):

    def find_loop_start(self):
        if self.head is None or self.head.next is None:
            return None
        slow = self.head
        fast = self.head
        while fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast is None:
                return None
            if slow == fast:
                break
        slow = self.head
        while slow != fast:
            slow = slow.next
            fast = fast.next
            if fast is None:
                return None
        return slow