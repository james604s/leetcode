"""

項目	  遞迴 DFS	         迴圈 DFS
實作方式    使用遞迴函式堆疊	手動管理 stack
可控性	   不易控制順序或深度	可明確控制 stack 行為
stack overflow？	 是（Python recursion limit）	否（受限於記憶體）
較容易理解	是（寫法簡潔）	     中（結構清楚但多一層堆疊管理）
"""

def iterative_dfs(graph, start_node):
    visited = set()
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            # Add neighbors to the stack
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
    return visited


def recursive_dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            recursive_dfs(graph, neighbor, visited)
    
    return visited

# Define a simple graph using an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Test case 1: Iterative DFS
iterative_result = iterative_dfs(graph, 'A')
print("Iterative DFS:", iterative_result)

# Test case 2: Recursive DFS
recursive_result = recursive_dfs(graph, 'A')
print("Recursive DFS:", recursive_result)

# Test case 3: Both methods should produce the same result for the same graph and start node
assert iterative_result == recursive_result, "Iterative and Recursive DFS results should match"

# Test case 4: Start from a different node
iterative_result_b = iterative_dfs(graph, 'B')
recursive_result_b = recursive_dfs(graph, 'B')
print("Iterative DFS from B:", iterative_result_b)
print("Recursive DFS from B:", recursive_result_b)

assert iterative_result_b == recursive_result_b, "Iterative and Recursive DFS results should match"



