class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def find_max(head):
    max_val = head.value

    while head:
        if head.value > max_val:
            max_val = head.value
        
        head = head.next
    
    return max_val


def remove_tail(head):
    if head is None:
        return None
    if head.next is None:
        return None 
        
    current = head
    while current.next.next: 
        current = current.next

    current.next = None 
    return head

def delete_dupes(head):
    freq = {}

    curr = head
    curr2 = head

    while curr:
        if curr.value not in freq:
            freq[curr.value] = 0
        
        freq[curr.value] += 1
        curr = curr.next
    
    while curr2 and curr2.next:
        while freq[curr2.next.value] > 1:
            curr2.next = curr2.next.next
        
        curr2 = curr2.next
    
    return head

    


head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))

# Linked List: 1 -> 2 -> 3 -> 3 -> 4 -> 5
print_linked_list(delete_dupes(head))