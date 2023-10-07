def minimum_cost(numGroup, group1, numGroup2, group2):
    minimum_cost = 0

    for share_position in group1:
        if share_position in group2:
            min_cost_operation = float('inf')
            for new_position in group1:
                if new_position != share_position:
                    cost = share_position + new_position
                    min_cost_operation = min(min_cost_operation, cost)
            minimum_cost += min_cost_operation

    if minimum_cost == 0:
        return -1
    else:
        return minimum_cost

# Read input values
numGroup = int(input())
group1 = list(map(int, input().split()))
numGroup2 = int(input())
group2 = list(map(int, input().split()))

# Call the function and print the result
result = minimum_cost(numGroup, group1, numGroup2, group2)
print(result)
