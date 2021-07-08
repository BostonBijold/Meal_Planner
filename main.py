import sys, operator, random
from nutrition import Food, MealPlan
from test import sort_food_listp

# Constants to be used by the greedy algorithm.
NUTRIENT_THRESHOLD = 0.001
FRACTION_THRESHOLD = 0.05
CALORIE_THRESHOLD = 0.1
MAX_CALORIES = 2000


def load_nutrient_data(filename):
    # Open file, read food items one line at a time,
    file = open(filename, 'r')
    # create Food objects and append them to a list.
    meallist = []
    for x in file:
        colon = x.find(':')
        name = x[:colon]
        numbers = x[colon + 1:]
        test = numbers.split(',')
        protein = float(test[0])
        fat = float(test[1])
        carbs = float(test[2])
        calories = float(test[3])
        x = Food(name, protein, fat, carbs, calories)

        meallist.append(x)

    # Return the list once the entire file is processed.

    return meallist


def sort_food_list(foods, nutrient):
    # Sort the food list based on the percent-by-calories of the
    # given nutrient ('protein', 'carbs' or 'fat')
    # The list is sorted in-place; nothing is returned.
    quicksort(foods, 0, len(foods)-1, nutrient)
    pass


def partition(foods, start_index, end_index, nutrient):
    mid_point = start_index + (end_index - start_index) // 2
    pivot = getattr(foods[mid_point], nutrient)
    # low and high start at the end of th segmentlist and move towards eachother
    low = start_index
    high = end_index

    done = False
    while not done:
        # Increment low while foods[low] < pivot
        while getattr(foods[low], nutrient) < pivot:
            low = low + 1


        # Decrement high while picot < foods[high]
        while pivot < getattr(foods[high], nutrient):
            high = high - 1

        # If low and High have crossed, the loop is done.
        # If not the elements are swapped, low is incremented and high is decremented
        if low >= high:
            done = True
        else:
            temp = foods[low]
            foods[low] = foods[high]
            foods[high] = temp
            low = low + 1
            high = high - 1

    return high

def quicksort(foods, start_index, end_index, nutrient):
    # Only attempt to sort the list segment if the are +2
    if end_index <= start_index:
        return

    # partition the list
    high = partition(foods, start_index, end_index, nutrient)

    # recursive sort the left segment
    quicksort(foods, start_index, high, nutrient)

    # recursive sort the right segment
    quicksort(foods, high + 1, end_index, nutrient)


def create_meal_plan(foods, nutrient, goal):
    # A greedy algorithm to create a meal plan that has MAX_CALORIES
    # calories and the goal amount of the nutrient (e.g. 30% protein)
    plan = MealPlan()

    for food in foods:
        if food.calories == 0 and getattr(food, nutrient) == 0: continue

        # Calculate the calorie_fraction of food allowed to fit the calorie limit;
        calorie_fraction = plan.fraction_to_fit_calories_limit(food, MAX_CALORIES)

        # Check portion amount.
        if calorie_fraction >= 1.0:
            # If whole ammount fits in calories, Check if portion surpasses nutrient goal.
            if plan.percent_nutrient_with_food(food, nutrient) <= goal + NUTRIENT_THRESHOLD:
                # If whole meal fits, added and continue
                plan.add_food(food)
            else:
                # If only a calorie_fraction will fit calculate the calorie_fraction amount by nutrient.
                nutrient_fraction = plan.fraction_to_fit_nutrient_goal(food,nutrient, goal)

                # Set the calorie_fraction and add.
                if nutrient_fraction > FRACTION_THRESHOLD:
                    food.set_fraction(nutrient_fraction)
                    plan.add_food(food)
        else:
            # If calorie in a single proportion is too high, check if a calorie_fraction will meet requirements.
            if calorie_fraction > CALORIE_THRESHOLD:

                # calculate the portion needed to hit calorie goal
                nutrient_fraction = plan.fraction_to_fit_nutrient_goal(food, nutrient, goal)
                if nutrient_fraction > FRACTION_THRESHOLD:
                    # Set foods fraction to the smaller of total calorie or nutrient fraction and add.
                    food.set_fraction(min(calorie_fraction, nutrient_fraction))
                    plan.add_food(food)
        # Check if both goals are reached, exit loop if true.
        if plan.meets_calorie_limit(MAX_CALORIES, CALORIE_THRESHOLD) and plan.meets_nutrient_goal(nutrient, goal, NUTRIENT_THRESHOLD):
            break
    return plan

    """
    remaining = MAX_CALORIES
    for meal in foods:
        # Check if full meal can fit in plan.
        if meal.calories <= remaining:
            # add full meal to plan.

            caloriecheck = plan.calories_with_food(meal)
            nutrient_check = plan.percent_nutrient_with_food(meal, nutrient)
            #print(nutrient_check)
            check = plan.fraction_to_fit_nutrient_goal(meal, nutrient, goal)
            if check > 0:
                plan.add_food(meal)
            remaining = remaining - meal.calories


        else:
            # Only a calorie_fraction will be added of the chosen meal
            #meal.set_fraction(remaining / meal.calories)
            plan.fraction_to_fit_calories_limit(meal, remaining)
            plan.add_food(meal)
            break

    return plan

"""

def print_menu():
    print()
    print("\t1 - Set maximum protein")
    print("\t2 - Set maximum carbohydrates")
    print("\t3 - Set maximum fat")
    print("\t4 - Exit program")
    print()


if __name__ == "__main__":
    # 1. Load the food data from the file (change this to a user
    # prompt for the filename)
    filename = 'food_data_small.txt'
    #filename = input('Enter name of food data file: ')
    foods = load_nutrient_data(filename)

    # 2. Display menu and get user's choice. Repeat menu until a
    # valid choice is entered by the user (1-4, inclusive).
    choice = -1
    while choice < 1 or choice > 3:
        print_menu()
        try:
            choice = int(input('Enter choice (1-4): '))
        except:
            choice = -1
        if choice == 1:
            nutrient = 'protein'
        elif choice == 2:
            nutrient = 'carbs'
        elif choice == 3:
            nutrient = 'fat'
        elif choice == 4:
            print('GoodBye!')
            sys.exit()
        else:
            print('Invalid choice! Enter an integer from 1-4!')

    sort_food_list(foods, nutrient)
    foods.reverse()

    # 3. Prompt user for goal nutrient percent value. Repeat prompt
    # until a valid choice is entered by the user (0-100, inclusive)
    goal = None
    while goal is None:
        try:
            goal = float(input('What percentage of calories from %s is the goal? ' % nutrient)) / 100.0
            if goal < 0.0 or goal > 1.0: goal = None
        except:
            pass

    # 4. Run greedy algorithm to create the meal plan.
    plan = create_meal_plan(foods, nutrient, goal)
    # 5. Display plan.
    print(plan)
