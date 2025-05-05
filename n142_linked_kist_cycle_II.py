class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                entry = head
                while entry != slow:
                    entry = entry.next
                    slow = slow.next
                return entry

        return None


# Створення списку: 3 -> 2 -> 0 -> -4 -> (назад до 2)
head = ListNode(3)
node1 = ListNode(2)
node2 = ListNode(0)
node3 = ListNode(-4)

head.next = node1
node1.next = node2
node2.next = node3
node3.next = node1  # цикл до node1 (значення 2)

solution = Solution()
cycle_start = solution.detectCycle(head)
print(cycle_start.val if cycle_start else "no cycle")  # Очікується: 2
