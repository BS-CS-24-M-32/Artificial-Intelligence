from collections import deque
# TASK 1: Graph (image 1) using adjacency lists + BFS using lists
# Edges: 0-1, 0-4, 1-2, 1-3, 1-4, 2-3, 3-4
graph = [
    [1, 4],        # 0
    [0, 2, 3, 4],  # 1
    [1, 3],        # 2
    [1, 2, 4],     # 3
    [0, 1, 3],     # 4
]


def bfs_list(graph, start):
    visited = [False] * len(graph)
    queue = []                 # plain list used as a queue
    order = []

    queue.append(start)
    visited[start] = True

    while queue:
        node = queue.pop(0)    # remove from the front
        order.append(node)
        for neighbour in graph[node]:
            if not visited[neighbour]:
                visited[neighbour] = True
                queue.append(neighbour)
    return order


print("TASK 1: BFS on graph (list based)")
print("BFS order from 0:", bfs_list(graph, 0))

# TASK 2: Tree (image 2), BFS using Queue, stop at goal G
tree = {
    'A': ['B', 'F', 'D', 'E'],
    'B': ['K', 'J'],
    'F': [],
    'D': ['G'],
    'E': ['C', 'H', 'I'],
    'K': ['N', 'M'],
    'J': [],
    'G': [],
    'C': [],
    'H': [],
    'I': ['L'],
    'N': [],
    'M': [],
    'L': [],
}


def bfs_queue(tree, start, goal):
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        if node == goal:                     # stop when goal is achieved
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return order, path[::-1]

        for child in tree[node]:
            if child not in visited:
                visited.add(child)
                parent[child] = node
                queue.append(child)
    return order, None


print("\nTASK 2: BFS using Queue (Start = A, Goal = G)")
order, path = bfs_queue(tree, 'A', 'G')
print("Nodes visited:", " -> ".join(order))
print("Path to goal :", " -> ".join(path))

# TASK 3: Priority Queue (lower number = higher priority)
class PriorityQueue:
    def __init__(self):
        self.items = []        # list of (priority, item)

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item, priority):
        # insert so the list stays sorted by priority
        index = 0
        while index < len(self.items) and self.items[index][0] <= priority:
            index += 1         # '<=' keeps FIFO order for equal priorities
        self.items.insert(index, (priority, item))

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items.pop(0)[1]

    def peek(self):
        return None if self.is_empty() else self.items[0][1]

    def size(self):
        return len(self.items)

    def display(self):
        print([(item, pr) for pr, item in self.items])


print("\nTASK 3: Priority Queue")
pq = PriorityQueue()
pq.enqueue("Task C", 3)
pq.enqueue("Task A", 1)
pq.enqueue("Task B", 2)
pq.enqueue("Task D", 1)
print("Queue (item, priority):", end=" ")
pq.display()
print("Peek    :", pq.peek())
while not pq.is_empty():
    print("Dequeued:", pq.dequeue())
