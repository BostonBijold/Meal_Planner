# An individual item with a weight and value
class Item:
    def __init__(self, item_weight, item_value):
        self.weight = item_weight
        self.value = item_value
        self.fraction = 1.0


# The knapsack that contains a list of items and a maximum
# total weight
class mealplan:
    def __init__(self, weight, items):
        self.max_weight = weight
        self.item_list = items


# A key function to be used to sort the items
def value_to_weight_ratio(item):
    return item.value / item.weight


# The Fractional Knapsack algorithm.
def fractional_knapsack(knapsack, item_list):
    # Sort the items in descending order based on value/weight
    item_list.sort(key=value_to_weight_ratio, reverse=True)

    remaining = knapsack.max_weight
    for item in item_list:
        # Check if the full item can fit into the knapsack or
        # only a fraction
        if item.weight <= remaining:
            # The full item will fit. Add the item to item_list with
            # a fraction of 1.0
            item.fraction = 1.0
            knapsack.item_list.append(item)
            remaining = remaining - item.weight

        else:
            # Only a fractional part of the item will fit. Add that
            # fraction of the item, and then exit.
            item.fraction = remaining / item.weight
            knapsack.item_list.append(item)
            break


# Main program to test the fractional knapsack algorithm.
item_1 = Item(6, 25)
item_2 = Item(8, 42)
item_3 = Item(12, 60)
item_4 = Item(18, 95)
item_list = [item_1, item_2, item_3, item_4]
initial_knapsack_list = []

# Ask the user for the knapsack's maximum capacity.
max_weight = int(input('Enter maximum weight the knapsack can hold: '))
print()

# Construct the knapsack object, then run the fractional_knapsack
# algorithm on it.
plan = mealplan(max_weight, initial_knapsack_list)
fractional_knapsack(plan, item_list)

# Output the information about the knapsack. Show the contents
# of the knapsack, and the fraction of each item.
print('Objects in knapsack')
i = 1
sum_weight = 0
sum_value = 0
for item in plan.item_list:
    sum_weight += item.weight * item.fraction
    sum_value += item.value * item.fraction
    print('%d: %0.1f of weight %0.1f, value %0.1f' %
          (i, item.fraction, item.weight, item.value * item.fraction))
    i += 1
print()

# Display the total weight of the items as well as the total value.
print('Total weight of items in knapsack: %d' % sum_weight)
print('Total value of items in knapsack: %d' % sum_value)
