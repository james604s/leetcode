"""
Breadth-First Search (BFS) 廣度優先搜尋

📌 BFS 的原理
BFS 是一種 層級遍歷（level-order traversal） 方法：

從起始節點開始，一層一層地拜訪相鄰節點。

使用 佇列（queue） 維護待拜訪節點的順序。

一個節點被訪問後，它的鄰居會被依序加入佇列，直到所有可達節點都被訪問。
"""

from collections import deque

# 迭代實作
def iterative_bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            # Add neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return visited

# 遞迴實作
def recursive_bfs_aux(graph, queue, visited):
    if not queue:
        return visited
    
    node = queue.popleft()
    visited.add(node)
    
    for neighbor in graph[node]:
        if neighbor not in visited and neighbor not in queue:
            queue.append(neighbor)
    
    return recursive_bfs_aux(graph, queue, visited)

def recursive_bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])
    return recursive_bfs_aux(graph, queue, visited)

# Define a simple graph using an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Test case 1: Iterative BFS
iterative_result = iterative_bfs(graph, 'A')
print("Iterative BFS:", iterative_result)

# Test case 2: Recursive BFS
recursive_result = recursive_bfs(graph, 'A')
print("Recursive BFS:", recursive_result)

# Test case 3: Both methods should produce the same result for the same graph and start node
assert iterative_result == recursive_result, "Iterative and Recursive BFS results should match"

# Test case 4: Start from a different node
iterative_result_b = iterative_bfs(graph, 'B')
recursive_result_b = recursive_bfs(graph, 'B')
print("Iterative BFS from B:", iterative_result_b)
print("Recursive BFS from B:", recursive_result_b)

assert iterative_result_b == recursive_result_b, "Iterative and Recursive BFS results should match"
