from typing import List
from bisect import bisect_left
def closestCost(n,m,base_costs, topping_costs, target):

    def dfs(index, total_cost):
        if index >= len(topping_costs):
            possible_toppings_costs.append(total_cost)
            return
        dfs(index + 1, total_cost)
        dfs(index + 1, total_cost + topping_costs[index])
    possible_toppings_costs = []
    dfs(0, 0)
    possible_toppings_costs.sort()
    closest_difference = 1000000000
    closest_cost = 1000000000
    for base_cost in base_costs:
        for toppings_cost in possible_toppings_costs:
            current_cost = base_cost + toppings_cost
            index = bisect_left(possible_toppings_costs, target - current_cost)
            for check_index in (index, index - 1):
                if 0 <= check_index < len(possible_toppings_costs):
                    total_cost = current_cost + possible_toppings_costs[check_index]
                    difference = abs(total_cost - target)
                    if closest_difference > difference or (closest_difference == difference and closest_cost > total_cost):
                        closest_difference = difference
                        closest_cost = total_cost
    return closest_cost

n=2
m=2
base_costs=[1,7]
topping_costs=[3,4]
target=10
print(closestCost(n,m,base_costs,topping_costs,target))
