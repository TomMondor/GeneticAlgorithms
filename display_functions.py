from constants import *


def find_and_present_best_solution(solutions : list[list[bool]], solutions_scores : list[float], items : list[int]) -> tuple[float, list[bool], list[int]]:
    """Finds the best solution among given solutions.

    Args:
        solutions (list[list[bool]]): a list of solutions, each solution being a list of booleans
        solutions_scores (list[float]): a list of scores for provided solutions
        items (list[int]): a list of items (weights)

    Returns:
        best_score, solution, selected items
    """
    best_score = max(solutions_scores)
    best_solution_index = solutions_scores.index(best_score)
    best_solution = solutions[best_solution_index]
    best_solution_items = []
    for index, is_present in enumerate(best_solution):
        if is_present:
            best_solution_items.append(items[index])
    
    return best_score, best_solution, best_solution_items


def print_solutions(solutions : list[list[bool]]):
    for solution in solutions:
        print_solution(solution)


def print_solution(solution : list[bool]):
    for item in solution:
        print(int(item), end="")
    print()

def print_stats(scores, best_score, best_solution, best_solution_items):
    print()
    print("scores:", scores)
    print("best score:", best_score)
    print("best_genetics:", end="")
    print_solution(best_solution)
    print("best_items:", best_solution_items)
    print()
