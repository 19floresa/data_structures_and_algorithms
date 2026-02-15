import math

class Node:
    def __init__(self, cost, x, y, heuristic):
        self.cost = cost
        self.x = x
        self.y = y
        self.heuristic = heuristic
    
    def get_position(self):
        return (self.x, self.y)

    def get_cost(self):
        return self.cost
    
    def get_heuristic(self):
        return self.heuristic
    
    def get_data(self):
        return (self.cost, self.x, self.y, self.heuristic)

    def compare_cost(self, node_b):
        return self.cost - node_b.cost

    def __str__(self):
        return f"{self.cost}"

class MinHeap():
    def __init__(self):
        self.nodes = []

    def peek(self):
        pass
    
    def push(self, node):
        nodes = self.nodes
        nodes.append(node)
        index = len(nodes) -1
        self.sift_up(index)
    
    def remove(self):
        pass
    
    def sift_up(self, node_index):
        nodes = self.nodes
        child = nodes[node_index]
        while True:
            parent_index = self.find_parent_index(node_index)
            parent = nodes[parent_index]
            cost_dif = child.compare_cost(parent)
            if cost_dif < 0:
                nodes[node_index] = parent
                nodes[parent_index] = child
                node_index = parent_index
                if (parent_index == 0): # new node is at the root
                    break
            else:
                break
        return node_index


    def find_parent_index(self, node_index):
        return math.floor((node_index - 1) / 2)
    
    def find_left_child_index(self, node_index):
        return (2 * node_index) + 1
    
    def find_right_child_index(self, node_index):
        return (2 * node_index) + 2

    def sift_down(self):
        pass

    def print(self):
        nodes = self.nodes
        temp = [ n.get_cost() for n in nodes]
        print(temp)

n1 = Node(10, 0, 0, 0)
n2 = Node(12, 0, 0, 0)
n3 = Node(14, 0, 0, 0)
n4 = Node(3, 0, 0, 0)

min_heap = MinHeap()
min_heap.push(n1)
min_heap.push(n2)
min_heap.push(n3)
min_heap.push(n4)
min_heap.print()
