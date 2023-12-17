import random
class NodeLL:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = NodeLL(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
    def find(self, valor):
        cur_node = self.head
        while cur_node:
            if cur_node.data == valor:
                return cur_node.data
            cur_node = cur_node.next
        return None

    def get_value(self):
        cur_node = self.head
        values = []
        while cur_node:
            values.append(cur_node.data.get_value())
            cur_node = cur_node.next
           
        return values
    
    def get_grandeza(self):
        cur_node = self.head
        total_grandeza = 0
        while cur_node:
            total_grandeza += cur_node.data.get_grandeza()
            cur_node = cur_node.next
        return total_grandeza
    
    def get_value_counts(self):
        cur_node = self.head
        value_counts = {}
        while cur_node:
            value = tuple(cur_node.data.get_value())  # Convierte la lista en una tupla
            if value in value_counts:
                value_counts[value] += 1
            else:
                value_counts[value] = 1
            cur_node = cur_node.next

        return value_counts



    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
    
    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def size(self):
        temp = 0
        cur_node = self.head
        while cur_node:
            temp += 1
            cur_node = cur_node.next

    def merge_sort(self):
        self.head = self._merge_sort_rec(self.head)

    def _merge_sort_rec(self, head):
        if head is None or head.next is None:
            return head

        middle = self._get_middle(head)
        next_to_middle = middle.next

        middle.next = None

        left = self._merge_sort_rec(head)
        right = self._merge_sort_rec(next_to_middle)

        sorted_list = self._sorted_merge(left, right)
        return sorted_list

    def _get_middle(self, head):
        if head is None:
            return head

        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        return slow

    def _sorted_merge(self, a, b):
        result = None

        if a is None:
            return b
        if b is None:
            return a

        if a.data.get_grandeza() <= b.data.get_grandeza():
            result = a
            result.next = self._sorted_merge(a.next, b)
        else:
            result = b
            result.next = self._sorted_merge(a, b.next)

        return result
    
    def shuffle(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(current.data)
            current = current.next
        
        random.shuffle(nodes)

        self.head = None
        for data in nodes:
            self.append(data)

    def pop_head(self):
        if self.head is None:
            return None  
        else:
            popped_node = self.head 
            self.head = self.head.next  
            return popped_node.data
        
    def get_animal_mas_menos_repetido(self):
        cur_node = self.head
        animales = []
        while cur_node:
            animales.append(cur_node.data.get_animal_mas_repetido())
            cur_node = cur_node.next
        return animales