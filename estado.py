#conterá a lógica do estado, a função de transição entre estados e a função sucessora, assim como o custo.

from itertools import combinations

TIMES = {
    'A': 1,
    'B': 2,
    'C': 5,
    'D': 10
}

START = (frozenset({'A', 'B', 'C', 'D'}), frozenset(), 'I')  # (conjunto de pessoas lado inicial, conjunto de pessoas lado final), posição da tocha
GOAL = (frozenset(), frozenset({'A', 'B', 'C', 'D'}), 'F')  # (conjunto de pessoas lado inicial, conjunto de pessoas lado final), posição da tocha


def is_goal(state):
    return state == GOAL


def get_torch_group(state):
    """Retorna o grupo de pessoas que estão com a tocha no estado atual."""
    initial_side, final_side, torch_position = state
    if torch_position == 'I':
        return initial_side
    else:
        return final_side

def get_possible_groups(state):
    group = get_torch_group(state)
    return list(combinations(group, 1)) + list(combinations(group, 2)) # retorna todas as combinações possíveis de 1 ou 2 pessoas do grupo que está com a tocha

def apply_action(state, group):
    initial_side, final_side, torch_position = state
    group = frozenset(group)
    
    if torch_position == 'I':
        new_initial = initial_side - group
        new_final = final_side | group
        new_torch = 'F'
    else:
        new_initial = initial_side | group
        new_final = final_side - group
        new_torch = 'I'
    
    new_state = (new_initial, new_final, new_torch)
    cost = max(TIMES[pessoa] for pessoa in group)  # maior tempo entre as pessoas do grupo
    
    return new_state, cost

def successors(state):
    results = []
    for group in get_possible_groups(state):
        new_state, cost = apply_action(state, group)
        results.append((group, new_state, cost))
    return results


    
if __name__ == "__main__":
    result = successors(START)
    for action, new_state, cost in result:
        print(action, "->", new_state, "custo:", cost)


