from algorithm_functions import *


# Algorithm Initialization

items = generate_random_items()
solutions = generate_gen0_possible_solutions()
solutions = calculate_solutions_scores(solutions, items)
best_solution = find_best_solution(solutions)

generation_number = 0
print(f"Generation {generation_number}")
print(f"Best solution: {best_solution}")

# Algorithm Loop
while best_solution.score < SATISFYING_THRESHOLD_FOR_SOLUTIONS:
    parents = select_solutions_to_reproduce(solutions)
    solutions = breed_new_generation(parents)
    solutions = calculate_solutions_scores(solutions, items)
    best_solution = find_best_solution(solutions)

    print(f"Generation {generation_number}")
    print(f"Best solution: {best_solution}")
    generation_number += 1

print()
print("All available items:")
print(items)
print("Best solution items:")
print(find_solution_items(best_solution, items))

#TODO essayer d'ajouter les elites, mais aussi les elites avec mutation