import heapq
from estado import START, is_goal, successors


def reconstruct_path(parent, state):
    path = [state]
    total_cost = 0
    while path[-1] in parent:
        prev_state, cost = parent[path[-1]]
        total_cost += cost
        path.append(prev_state)
    path.reverse()
    return path, total_cost

def uniform_cost():
    counter = 0
    frontier = [(0, counter, START)]
    visited = set()
    parent = {}
    best_cost = {START: 0} 

    while frontier:
        cost_so_far, _, current = heapq.heappop(frontier)

        if current in visited:
            continue
        visited.add(current)

        if is_goal(current):
            return reconstruct_path(parent, current)

        for action, new_state, cost in successors(current):
            new_cost = cost_so_far + cost
            if new_state not in best_cost or new_cost < best_cost[new_state]:
                best_cost[new_state] = new_cost
                parent[new_state] = (current, cost)
                counter += 1
                heapq.heappush(frontier, (new_cost, counter, new_state))

    return None


if __name__ == "__main__":
    path, total_cost = uniform_cost()
    print("Caminho encontrado:")
    for state in path:
        print(state)
    print("Total de passos:", len(path) - 1)
    print("Custo total:", total_cost)