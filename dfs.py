from collections import deque
from estado import START, is_goal, successors

def reconstruct_path(parent, state):
    path = [state]
    total_cost = 0
    while path[-1] in parent:
        previous_state, cost = parent[path[-1]]
        total_cost += cost
        path.append(previous_state)
    path.reverse()
    return path, total_cost

def bfs():
    frontier = deque([START])
    visited = {START}
    parent = {}

    while frontier:
        current = frontier.pop()

        if is_goal(current):
            return reconstruct_path(parent, current)

        for action, new_state, cost in successors(current):
            if new_state not in visited:
                visited.add(new_state)
                parent[new_state] = current, cost
                frontier.append(new_state)

    return None

if __name__ == "__main__":
    path, total_cost = bfs()
    print("Caminho encontrado:")
    for state in path:
        print(state)
    print("Total de passos:", len(path) - 1)
    print("Custo total:", total_cost)