from itertools import combinations

p = 6
n = pow(p, 2) + p + 1

def CycDiff(input_list):
    difference_set = set()
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            difference1 = (input_list[i] - input_list[j]) % n
            difference2 = (input_list[j] - input_list[i]) % n
            difference_set.add(difference1)
            difference_set.add(difference2)
    return difference_set

cyc_diff_tuples = []  # Initialize as an empty list

def four_element_subsets():
    Z_elements = list(range(2, n))
    
    for combo in combinations(Z_elements, p-1):
        combo_list = list(combo) + [0, 1]  # Convert combo to a list and add 0 and 1
        combo_tuple = tuple(combo_list)  # Convert back to a tuple
        if CycDiff(combo_tuple) == set(range(1, n)):
            cyc_diff_tuples.append(combo_tuple)
    
    return cyc_diff_tuples

result = four_element_subsets()

for i, subset in enumerate(result):
    print(f"Subset {i + 1}: {subset}")






