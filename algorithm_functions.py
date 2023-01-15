from random import randint, choice
from copy import copy

from constants import *
from genetic_types import *


def generate_random_items() -> list[Item]:
    items = []
    for _ in range(AVAILABLE_ITEMS_NUMBER):
        items.append(randint(MIN_ITEM_WEIGHT, MAX_ITEM_WEIGHT))
    return items


def generate_gen0_possible_solutions() -> list[Solution]:
    solutions = []
    for _ in range(POPULATION_SIZE):
        solution = Solution([choice([True, False]) for _ in range(AVAILABLE_ITEMS_NUMBER)])
        solutions.append(solution)
    return solutions


def calculate_solutions_scores(solutions : list[Solution], items: list[Item]) -> list[Solution]:
    solutions_with_scores = [copy(solution) for solution in solutions]
    for solution in solutions_with_scores:
        solution_weight = 0
        for index, is_present in enumerate(solution.genes):
            solution_weight += items[index] if is_present else 0
        solution.score = (solution_weight / GOAL_WEIGHT) if (solution_weight <= GOAL_WEIGHT) else 0
    return solutions_with_scores


def find_best_solution(solutions : list[Solution]) -> Solution:
    return max(solutions, key=lambda solution: solution.score)

def find_solution_items(solution : Solution, items : list[Item]) -> list[Item]:
    """Returns the items that are present in the solution."""
    return [item for index, item in enumerate(items) if solution.genes[index]]


def select_solutions_to_reproduce(solutions : list[Solution]) -> list[Solution]:
    """Selects the top solutions, which will be used to generate the next generation."""
    solutions = [copy(solution) for solution in solutions]
    sorted_solutions = sorted(solutions, key=lambda solution: solution.score, reverse=True)
    return sorted_solutions[:int(POPULATION_SIZE * SURVIVING_RATIO)]


def breed_new_generation(prev_gen_selected_solutions : list[Solution]) -> list[Solution]:
    """Creates the new generation of solutions, by elitism, mutations, breeding of the last generation's best."""
    new_generation = select_elite_solutions(prev_gen_selected_solutions)

    while len(new_generation) < POPULATION_SIZE:
        parent1, parent2 = choice(prev_gen_selected_solutions), choice(prev_gen_selected_solutions)
        child1, child2 = single_point_crossover(parent1, parent2)
        new_generation.append(mutate(child1))
        new_generation.append(mutate(child2))

    return new_generation


def select_elite_solutions(solutions : list[Solution]) -> list[Solution]:
    """The best solutions from the previous generation are kept."""
    sorted_solutions = sorted(solutions, key=lambda solution: solution.score, reverse=True)
    return sorted_solutions[:ELITE_SOLUTIONS_NUMBER]


def single_point_crossover(parent_solution1 : Solution, parent_solution2 : Solution) -> tuple[Solution, Solution]:
    """Creates two new solutions by crossing over the genes of the two provided solutions."""
    crossover_point = randint(0, len(parent_solution1.genes) - 1)
    child_solution1 = Solution(parent_solution1.genes[:crossover_point] + parent_solution2.genes[crossover_point:])
    child_solution2 = Solution(parent_solution2.genes[:crossover_point] + parent_solution1.genes[crossover_point:])
    return child_solution1, child_solution2


def mutate(solution : Solution) -> Solution:
    """Mutates a solution randomly."""
    mutated_solution = copy(solution)
    for _ in range(MUTATIONS_NUMBER_BY_SOLUTION):
        gene_to_modify = randint(0, len(solution.genes) - 1)
        mutated_solution.genes[gene_to_modify] = not solution.genes[gene_to_modify]
    return mutated_solution
